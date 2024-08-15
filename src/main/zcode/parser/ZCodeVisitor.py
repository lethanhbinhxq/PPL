# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#program_line.
    def visitProgram_line(self, ctx:ZCodeParser.Program_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#compulsory_newline.
    def visitCompulsory_newline(self, ctx:ZCodeParser.Compulsory_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_newline.
    def visitOptional_newline(self, ctx:ZCodeParser.Optional_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_type.
    def visitDecl_type(self, ctx:ZCodeParser.Decl_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explicit_decl.
    def visitExplicit_decl(self, ctx:ZCodeParser.Explicit_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_type.
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_decl.
    def visitImplicit_decl(self, ctx:ZCodeParser.Implicit_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_var.
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_dynamic.
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_decl.
    def visitArray_decl(self, ctx:ZCodeParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#size_decl.
    def visitSize_decl(self, ctx:ZCodeParser.Size_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#size_list.
    def visitSize_list(self, ctx:ZCodeParser.Size_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#tail_size.
    def visitTail_size(self, ctx:ZCodeParser.Tail_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#passed_para.
    def visitPassed_para(self, ctx:ZCodeParser.Passed_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para_list.
    def visitPara_list(self, ctx:ZCodeParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#tail_para.
    def visitTail_para(self, ctx:ZCodeParser.Tail_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body_func.
    def visitBody_func(self, ctx:ZCodeParser.Body_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_type.
    def visitStmt_type(self, ctx:ZCodeParser.Stmt_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_stmt.
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_stmt.
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_stmt.
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#tail_expr.
    def visitTail_expr(self, ctx:ZCodeParser.Tail_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#body_block.
    def visitBody_block(self, ctx:ZCodeParser.Body_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt_list.
    def visitBlock_stmt_list(self, ctx:ZCodeParser.Block_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call_expr.
    def visitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_lit.
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#comp_expr_list.
    def visitComp_expr_list(self, ctx:ZCodeParser.Comp_expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expr.
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operator.
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#mul_div_rem.
    def visitMul_div_rem(self, ctx:ZCodeParser.Mul_div_remContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_subtr.
    def visitAdd_subtr(self, ctx:ZCodeParser.Add_subtrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#and_or.
    def visitAnd_or(self, ctx:ZCodeParser.And_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_op.
    def visitRelational_op(self, ctx:ZCodeParser.Relational_opContext):
        return self.visitChildren(ctx)



del ZCodeParser