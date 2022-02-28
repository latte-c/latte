from ast import AST
from .ast_node import ASTNode
from .LatteVisitor import LatteVisitor
from .LatteParser import LatteParser


def list_map(function, l):
    return list(map(function, l))


class ASTVisitor(LatteVisitor):
    def getText(self, t):
        return t.getText()

    def visitOptional(self, t):
        return None if t is None else self.visit(t)

    def visitCompilationUnit(self, ctx: LatteParser.CompilationUnitContext):
        import_declarations = list_map(self.visit, ctx.importDeclaration())
        top_declarations = list_map(self.visit, ctx.topDeclaration())
        return ASTNode('compilation_unit',  [import_declarations, top_declarations])

    def visitImportDeclaration(self, ctx: LatteParser.ImportDeclarationContext):
        import_path = list_map(self.getText, ctx.IDENTIFIER())
        return ASTNode('import_declaration', import_path)

    def visitTopDeclaration(self, ctx: LatteParser.TopDeclarationContext):
        return self.visitChildren(ctx)

    def visitVarDeclaration(self, ctx: LatteParser.VarDeclarationContext):
        return ASTNode('var_declaration', [
            # access modifier
            ctx.EXPORT() != None,
            # type
            self.visit(ctx.latteType()),
            # name
            self.getText(ctx.IDENTIFIER()),
            # initialization
            self.visitOptional(ctx.expression())])

    def visitProcedureDeclaration(self, ctx: LatteParser.ProcedureDeclarationContext):
        return ASTNode('procedure_declaration', [
            # access modifier
            ctx.EXPORT() != None,
            # return type
            self.visit(ctx.latteType()),
            # procedure name
            self.getText(ctx.IDENTIFIER()),
            # arguments
            list_map(self.visit, ctx.procedureArgument()),
            # function body
            list_map(self.visit, ctx.statement())])

    def visitProcedureArgument(self, ctx: LatteParser.ProcedureArgumentContext):
        # type, name
        return (self.visit(ctx.latteType()), self.getText(ctx.IDENTIFIER()))

    def visitStatement(self, ctx: LatteParser.StatementContext):
        return self.visitChildren(ctx)

    def visitBlockStatement(self, ctx: LatteParser.BlockStatementContext):
        # statements
        return ASTNode('block_statement', list_map(self.visit, ctx.statement()))

    def visitIfStatement(self, ctx: LatteParser.IfStatementContext):
        # condition, if-branch, else-branch
        return ASTNode('if_statement', [self.visit(ctx.expression()), self.visit(ctx.statement(0)), self.visitOptional(ctx.statement(1))])

    