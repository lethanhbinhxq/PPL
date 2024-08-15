from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.program_line()))
    def visitProgram_line(self, ctx:ZCodeParser.Program_lineContext):
        if ctx.decl_list():
            return self.visit(ctx.decl_list())
        return self.visit(ctx.stmt_list())
    def visitCompulsory_newline(self, ctx:ZCodeParser.Compulsory_newlineContext):
        return None
    def visitOptional_newline(self, ctx:ZCodeParser.Optional_newlineContext):
        return None
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visit(ctx.decl_type())
    def visitDecl_type(self, ctx:ZCodeParser.Decl_typeContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        return self.visit(ctx.func_decl())
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        if ctx.explicit_decl():
            return self.visit(ctx.explicit_decl())
        elif ctx.implicit_decl():
            return self.visit(ctx.implicit_decl())
        else:
            return self.visit(ctx.array_decl())
    def visitExplicit_decl(self, ctx:ZCodeParser.Explicit_declContext):
        # VarDecl(Id name, Type varType, string modifier, Expr VarInit)
        if ctx.ASSIGN():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.primitive_type()), None, self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.primitive_type()))
    def visitPrimitive_type(self, ctx:ZCodeParser.Primitive_typeContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        else:
            return StringType()
    def visitImplicit_decl(self, ctx:ZCodeParser.Implicit_declContext):
        if ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        return self.visit(ctx.implicit_dynamic())
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        # VarDecl(Id name, Type varType, string modifier, Expr VarInit)
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "var", self.visit(ctx.expr()))
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        if ctx.ASSIGN():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "dynamic", self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), None, "dynamic")
    def visitArray_decl(self, ctx:ZCodeParser.Array_declContext):
        # ArrayType(List[float] size, Type eleType)
        if ctx.ASSIGN():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.size_decl()), self.visit(ctx.primitive_type())), None, self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.size_decl()), self.visit(ctx.primitive_type())))
    def visitSize_decl(self, ctx:ZCodeParser.Size_declContext):
        return self.visit(ctx.size_list())
    def visitSize_list(self, ctx:ZCodeParser.Size_listContext):
        if ctx.getChildCount() == 1:
            # NumberLiteral(float value)
            return [float(ctx.NUM_LIT().getText())]
        return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.tail_size())
    def visitTail_size(self, ctx:ZCodeParser.Tail_sizeContext):
        if ctx.getChildCount() == 0:
            return []
        return [float(ctx.NUM_LIT().getText())] + self.visit(ctx.tail_size())
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        # FuncDecl(Id name, List[VarDecl], Stmt body)
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.passed_para()), self.visit(ctx.body_func()))
    def visitPassed_para(self, ctx:ZCodeParser.Passed_paraContext):
        return self.visit(ctx.para_list())
    def visitPara_list(self, ctx:ZCodeParser.Para_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.parameter())] + self.visit(ctx.tail_para())
    def visitTail_para(self, ctx:ZCodeParser.Tail_paraContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.parameter())] + self.visit(ctx.tail_para())
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        if ctx.size_decl():
            return VarDecl(Id(ctx.IDENTIFIER().getText()), ArrayType(self.visit(ctx.size_decl()), self.visit(ctx.primitive_type())))
        return VarDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.primitive_type()))
    def visitBody_func(self, ctx:ZCodeParser.Body_funcContext):
        # Body: Stmt = None
        if ctx.getChildCount() == 0:
            return None
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        else:
            return self.visit(ctx.block_stmt())
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.stmt_list())
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visit(ctx.stmt_type())
    def visitStmt_type(self, ctx:ZCodeParser.Stmt_typeContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.func_call_stmt():
            return self.visit(ctx.func_call_stmt())
        elif ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        else:
            return self.visit(ctx.continue_stmt())
    def visitAssign_stmt(self, ctx:ZCodeParser.Assign_stmtContext):
        # Assign(Expr lhs, Expr rhs)
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        # ArrayCell(Expr arr, List[Expr] idx)
        return ArrayCell(self.visit(ctx.expr()), self.visit(ctx.index_expr()))
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        # If(Expr expr, Stmt thenStmt, List[Tuple(Expr, Stmt)] elifStmt, Stmt elseStmt = None)
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt_type()), self.visit(ctx.elif_list()), self.visit(ctx.else_stmt()))
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.elif_stmt())] + self.visit(ctx.elif_list())
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return (self.visit(ctx.expr()), self.visit(ctx.statement()))
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visit(ctx.statement())
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        # For(Id name, Expr condExpr, Expr updExpr, Stmt body)
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.statement()))
    def visitBreak_stmt(self, ctx:ZCodeParser.Break_stmtContext):
        return Break()
    def visitContinue_stmt(self, ctx:ZCodeParser.Continue_stmtContext):
        return Continue()
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        # Return(Expr expr=None)
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)
    def visitFunc_call_stmt(self, ctx:ZCodeParser.Func_call_stmtContext):
        # CallStmt(Id name, List[Expr] args)
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr_list()))
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expr())] + self.visit(ctx.tail_expr())
    def visitTail_expr(self, ctx:ZCodeParser.Tail_exprContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expr())] + self.visit(ctx.tail_expr())
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        # Block(List[Stmt] stmt)
        return Block(self.visit(ctx.body_block()))
    def visitBody_block(self, ctx:ZCodeParser.Body_blockContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.block_stmt_list())
    def visitBlock_stmt_list(self, ctx:ZCodeParser.Block_stmt_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.block_stmt_list())
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        #BinaryOp(str op, Expr left, Expr right)
        return BinaryOp(ctx.SPREAD_OP().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        return BinaryOp(self.visit(ctx.relational_op()), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        return BinaryOp(self.visit(ctx.and_or()), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        return BinaryOp(self.visit(ctx.add_subtr()), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        return BinaryOp(self.visit(ctx.mul_div_rem()), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        # UnaryOp(str op, Expr operand)
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnaryOp(ctx.SUBTR_OP().getText(), self.visit(ctx.expr6()))
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        # ArrayCell(Expr arr, List[Expr] idx)
        return ArrayCell(self.visit(ctx.expr7()), self.visit(ctx.index_expr()))
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        return self.visit(ctx.expr())
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.IDENTIFIER():
            # Id(str name)
            return Id(ctx.IDENTIFER().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        else:
            return self.visit(ctx.func_call_expr())
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return self.visit(ctx.index_operator())
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        # ArrayCell(Expr, List[Expr])
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.index_operator())
    def visitMul_div_rem(self, ctx:ZCodeParser.Mul_div_remContext):
        if ctx.MUL_OP():
            return ctx.MUL_OP().getText()
        elif ctx.DIV_OP():
            return ctx.DIV_OP().getText()
        else:
            return ctx.REMAINDER_OP().getText()
    def visitAdd_subtr(self, ctx:ZCodeParser.Add_subtrContext):
        if ctx.ADD_OP():
            return ctx.ADD_OP().getText()
        return ctx.SUBTR_OP().getText()
    def visitAnd_or(self, ctx:ZCodeParser.And_orContext):
        if ctx.AND():
            return ctx.AND().getText()
        return ctx.OR().getText()
    def visitRelational_op(self, ctx:ZCodeParser.Relational_opContext):
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.EQUAL_STR():
            return ctx.EQUAL_STR().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()
        elif ctx.SMALLER():
            return ctx.SMALLER().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.SMALLER_OR_EQUAL():
            return ctx.SMALLER_OR_EQUAL().getText()
        else:
            return ctx.GREATER_OR_EQUAL().getText()
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        else:
            return self.visit(ctx.func_call_expr())
        
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        # NumberLiteral(float value)
        if ctx.NUM_LIT():
            return NumberLiteral(float(ctx.NUM_LIT().getText()))
        # BooleanLiteral(bool value)
        elif ctx.TRUE():
            return BooleanLiteral(bool(True))
        elif ctx.FALSE():
            return BooleanLiteral(bool(False))
        # StringLiteral(string value)
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        else:
            return self.visit(ctx.array_lit())
        
    def visitFunc_call_expr(self, ctx:ZCodeParser.Func_call_exprContext):
        # CallExpr(Id name, List[Expr] args)
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr_list()))
    def visitArray_lit(self, ctx:ZCodeParser.Array_litContext):
        # ArrayLiteral(List[Expr] value)
        return ArrayLiteral(self.visit(ctx.comp_expr_list()))
    def visitComp_expr_list(self, ctx:ZCodeParser.Comp_expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.tail_expr())