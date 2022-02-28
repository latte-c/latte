# Generated from latte/front/antlr4/Latte.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LatteParser import LatteParser
else:
    from LatteParser import LatteParser

# This class defines a complete generic visitor for a parse tree produced by LatteParser.

class LatteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatteParser#compilationUnit.
    def visitCompilationUnit(self, ctx:LatteParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#importDeclaration.
    def visitImportDeclaration(self, ctx:LatteParser.ImportDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#topDeclaration.
    def visitTopDeclaration(self, ctx:LatteParser.TopDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#varDeclaration.
    def visitVarDeclaration(self, ctx:LatteParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#procedureDeclaration.
    def visitProcedureDeclaration(self, ctx:LatteParser.ProcedureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#procedureArgument.
    def visitProcedureArgument(self, ctx:LatteParser.ProcedureArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#statement.
    def visitStatement(self, ctx:LatteParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#blockStatement.
    def visitBlockStatement(self, ctx:LatteParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ifStatement.
    def visitIfStatement(self, ctx:LatteParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#loopStatement.
    def visitLoopStatement(self, ctx:LatteParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#breakStatement.
    def visitBreakStatement(self, ctx:LatteParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#continueStatement.
    def visitContinueStatement(self, ctx:LatteParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#returnStatement.
    def visitReturnStatement(self, ctx:LatteParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#expressionStatement.
    def visitExpressionStatement(self, ctx:LatteParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#assignStatement.
    def visitAssignStatement(self, ctx:LatteParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#varStatement.
    def visitVarStatement(self, ctx:LatteParser.VarStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#binaryOrExpr.
    def visitBinaryOrExpr(self, ctx:LatteParser.BinaryOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#arrayExpr.
    def visitArrayExpr(self, ctx:LatteParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#binaryMulExpr.
    def visitBinaryMulExpr(self, ctx:LatteParser.BinaryMulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#binaryModExpr.
    def visitBinaryModExpr(self, ctx:LatteParser.BinaryModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#intConstExpr.
    def visitIntConstExpr(self, ctx:LatteParser.IntConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#parenExpr.
    def visitParenExpr(self, ctx:LatteParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#charConstExpr.
    def visitCharConstExpr(self, ctx:LatteParser.CharConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#unaryExpr.
    def visitUnaryExpr(self, ctx:LatteParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#binaryAddExpr.
    def visitBinaryAddExpr(self, ctx:LatteParser.BinaryAddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#realConstExpr.
    def visitRealConstExpr(self, ctx:LatteParser.RealConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#stringConstExpr.
    def visitStringConstExpr(self, ctx:LatteParser.StringConstExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#binaryCompExpr.
    def visitBinaryCompExpr(self, ctx:LatteParser.BinaryCompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#binaryEqExpr.
    def visitBinaryEqExpr(self, ctx:LatteParser.BinaryEqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#binaryAndExpr.
    def visitBinaryAndExpr(self, ctx:LatteParser.BinaryAndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#callExpr.
    def visitCallExpr(self, ctx:LatteParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#accessExpr.
    def visitAccessExpr(self, ctx:LatteParser.AccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#accessExpression.
    def visitAccessExpression(self, ctx:LatteParser.AccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#latteType.
    def visitLatteType(self, ctx:LatteParser.LatteTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#nativeType.
    def visitNativeType(self, ctx:LatteParser.NativeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#arrayShape.
    def visitArrayShape(self, ctx:LatteParser.ArrayShapeContext):
        return self.visitChildren(ctx)



del LatteParser