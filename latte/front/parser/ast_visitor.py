from typing import cast

from .ast_node import ASTNode
from .LatteVisitor import LatteVisitor
from .LatteParser import LatteParser
import codecs


def list_map(function, l):
    return list(map(function, l))


class ASTVisitor(LatteVisitor):
    def getText(self, t):
        if hasattr(t, 'text'):
            return t.text
        else:
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
            # access modifier?
            ctx.EXPORT() != None,
            # type
            self.visit(ctx.latteType()),
            # name
            self.getText(ctx.IDENTIFIER()),
            # initialization
            self.visitOptional(ctx.expression())])

    def visitProcedureDeclaration(self, ctx: LatteParser.ProcedureDeclarationContext):
        return ASTNode('procedure_declaration', [
            # access modifier?
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
        # condition, if-branch, else-branch?
        return ASTNode('if_statement', [self.visit(ctx.expression()), self.visit(ctx.statement(0)), self.visitOptional(ctx.statement(1))])

    def visitLoopStatement(self, ctx: LatteParser.LoopStatementContext):
        # loop-label?, loop-body
        return ASTNode('loop_statement', [self.visitOptional(ctx.IDENTIFIER()), self.visit(ctx.statement())])

    def visitBreakStatement(self, ctx: LatteParser.BreakStatementContext):
        # break-label?
        return ASTNode('break_statement', [self.visitOptional(ctx.IDENTIFIER())])

    def visitContinueStatement(self, ctx: LatteParser.ContinueStatementContext):
        # continue-label?
        return ASTNode('continue_statement', [self.visitOptional(ctx.IDENTIFIER())])

    def visitReturnStatement(self, ctx: LatteParser.ReturnStatementContext):
        # return-expression
        return ASTNode('return_statement', [self.visit(ctx.expression())])

    def visitExpressionStatement(self, ctx: LatteParser.ExpressionStatementContext):
        # expression
        return ASTNode('expression_statement', [self.visit(ctx.expression())])

    def visitAssignStatement(self, ctx: LatteParser.AssignStatementContext):
        # left-hand right-hand
        return ASTNode('assign_statement', [self.visit(ctx.accessExpression()), self.visit(ctx.expression())])

    def visitVarStatement(self, ctx: LatteParser.VarStatementContext):
        # type vars
        return ASTNode('var_statement', [self.visit(ctx.latteType()), list_map(self.visit, ctx.varInitialization())])

    def visitVarInitialization(self, ctx: LatteParser.VarInitializationContext):
        # (name, initialization-expression)
        return (self.getText(ctx.IDENTIFIER()), self.visitOptional(ctx.expression()))

    def visitUnaryExpr(self, ctx: LatteParser.UnaryExprContext):
        return ASTNode('unary_expression', [self.getText(ctx.op), self.visit(ctx.expression())])

    def visitBinaryMulExpr(self, ctx: LatteParser.BinaryMulExprContext):
        return ASTNode('binary_expression', [self.visit(ctx.expression(0)), self.getText(ctx.op), self.visit(ctx.expression(1))])

    def visitBinaryAddExpr(self, ctx: LatteParser.BinaryAddExprContext):
        return ASTNode('binary_expression', [self.visit(ctx.expression(0)), self.getText(ctx.op), self.visit(ctx.expression(1))])

    def visitBinaryModExpr(self, ctx: LatteParser.BinaryModExprContext):
        return ASTNode('binary_expression', [self.visit(ctx.expression(0)), self.getText(ctx.op), self.visit(ctx.expression(1))])

    def visitBinaryCompExpr(self, ctx: LatteParser.BinaryCompExprContext):
        return ASTNode('binary_expression', [self.visit(ctx.expression(0)), self.getText(ctx.op), self.visit(ctx.expression(1))])

    def visitBinaryEqExpr(self, ctx: LatteParser.BinaryEqExprContext):
        return ASTNode('binary_expression', [self.visit(ctx.expression(0)), self.getText(ctx.op), self.visit(ctx.expression(1))])

    def visitBinaryAndExpr(self, ctx: LatteParser.BinaryAndExprContext):
        return ASTNode('binary_expression', [self.visit(ctx.expression(0)), '&&', self.visit(ctx.expression(1))])

    def visitBinaryOrExpr(self, ctx: LatteParser.BinaryOrExprContext):
        return ASTNode('binary_expression', [self.visit(ctx.expression(0)), '||', self.visit(ctx.expression(1))])

    def visitParenExpr(self, ctx: LatteParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitArrayExpr(self, ctx: LatteParser.ArrayExprContext):
        return ASTNode('array_expression', list_map(self.visit, ctx.expression()))

    def visitCallExpr(self, ctx: LatteParser.CallExprContext):
        # call-procedure, arguments
        return ASTNode('call_expression', [self.getText(ctx.IDENTIFIER()), list_map(self.visit, ctx.expression())])

    def visitAccessExpr(self, ctx: LatteParser.AccessExprContext):
        return self.visit(ctx.accessExpression())

    def visitIntConstExpr(self, ctx: LatteParser.IntConstExprContext):
        return int(ctx.getText())

    def visitRealConstExpr(self, ctx: LatteParser.RealConstExprContext):
        return float(ctx.getText())

    def visitCharConstExpr(self, ctx: LatteParser.CharConstExprContext):
        return ord(codecs.getdecoder('unicode_escape')(ctx.getText()[1:-1].encode('utf-8'))[0])

    def visitStringConstExpr(self, ctx: LatteParser.StringConstExprContext):
        string_literal = codecs.getdecoder('unicode_escape')(
            ctx.getText()[1:-1].encode('utf-8'))[0]
        # transform it into array_expression since it is alise for array
        string_array = list_map(ord, string_literal)
        string_array.append(0)  # C-style string terminal
        return ASTNode('call_expression', string_array)

    def visitAccessExpression(self, ctx: LatteParser.AccessExpressionContext):
        # variable, index?
        return ASTNode('access_expression', [self.getText(ctx.IDENTIFIER()), list_map(self.visit, ctx.expression())])

    def visitLatteType(self, ctx: LatteParser.LatteTypeContext):
        # (native_type, native_width), array_shape?
        native_type = (self.getText(ctx.nativeType()),
                       int(self.getText(ctx.INT_CONST())))
        # array_shape could be None (not a array), [] (Any shape) or [...] (Certain shape)
        return ASTNode('latte_type', [native_type, self.visitOptional(ctx.arrayShape())])

    def visitArrayShape(self, ctx: LatteParser.ArrayShapeContext):
        int_literals = list_map(self.getText, ctx.INT_CONST())
        return int_literals
