from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class VarObj:
    def __init__(self, obj: VarDecl, varType: Type = None):
        self.obj = obj
        self.varType = varType
    def __str__(self):
        return f"VarObj({str(self.obj)}, {str(self.varType)})"

class FuncObj:
    def __init__(self, obj: FuncDecl, returnType: Type = VoidType()):
        self.obj = obj
        self.returnType = returnType
    def __str__(self):
        return f"FuncObj({str(self.obj)}, {str(self.returnType)})"

class StmtObj:
    def __init__(self, obj: Stmt, level: int, returnType: Type = VoidType()):
        self.obj = obj
        self.level = level
        self.returnType = returnType
    def __str__(self):
        return f"StmtObj({str(self.obj)}, {str(self.level)}, {str(self.returnType)})"

class StaticChecker(BaseVisitor, Utils):
    declared = [[]] # symbol table
    level = 0 # scope for variable and function
    stmtList = [] # list of statements in a function, reset in each function, use for checking return type
    checkLoop = [] # list of statements in a function, reset in each function, use for checking whether break and continue are in loop
    depth = 0 # scope for statement in a function
    def __init__(self, asttree: Program):
        self.asttree = asttree
    def check(self):
        self.visit(self.asttree, object)
    # 2.1. Redeclared variable / parameter / function
    def detectRedeclared(self, ctx: Decl, o: object):
        # self.declared: including VarObj(obj: VarDecl, varType: Type) and FuncObj(func: FuncDecl, returnType: Type)
        for item in self.declared[self.level]:
            if type(item.obj) == type(ctx) and item.obj.name.name == ctx.name.name:
                # Redeclared variable
                if type(ctx) == VarDecl:
                    raise Redeclared(Variable(), ctx.name.name)
                # Redeclared function
                elif type(ctx) == FuncDecl:
                    # if item.obj.param == ctx.param and item.obj.body is None and ctx.body is not None:
                    #     item.obj.body = ctx.body
                    # raise Redeclared(Function(), ctx.name.name)
                    if len(item.obj.param) != len(ctx.param):
                        raise Redeclared(Function(), ctx.name.name)
                    for i in range(len(item.obj.param)):
                        if type(ctx.param[i].varType) != type(item.obj.param[i].varType):
                            raise Redeclared(Function(), ctx.name.name)
                    if (item.obj.body is not None and type(item.obj.body) != Continue) or ctx.body is None:
                        raise Redeclared(Function(), ctx.name.name)
                    if type(item.obj.body) != Continue:
                        item.obj.body = ctx.body
                    if type(item.returnType) == VoidType:
                        returnType = self.visit(ctx.body, o)
                        if returnType is None:
                            returnType = VoidType()
                        item.returnType = returnType
                    return False
        if type(ctx) == FuncDecl:
            # FuncDecl(name: Id, param: List[VarDecl], body: Stmt)
            for i in range(len(ctx.param)):
                for j in range (len(ctx.param)):
                    if i != j:
                        if ctx.param[i].name.name == ctx.param[j].name.name:
                            raise Redeclared(Parameter(), ctx.param[j].name.name)
            
    # 2.2. Undeclared identifier / function
    def detectUndeclared(self, ctx, o: object):
        # ctx: Id or CallStmt
        if isinstance(ctx, Id):
            for i in range(self.level, -1, -1):
                for item in self.declared[i]:
                    # 2.2.1. Undeclared identifier
                    if isinstance(item, VarObj) and item.obj.name.name == ctx.name:
                        return item.varType
            raise Undeclared(Identifier(), ctx.name)
        elif isinstance(ctx, CallStmt) or isinstance(ctx, CallExpr):
            for i in range(self.level, -1, -1):
                for item in self.declared[i]:
                    # 2.2.2. Undeclared function
                    if isinstance(item, FuncObj) and item.obj.name.name == ctx.name.name:
                        return item
            raise Undeclared(Function(), ctx.name.name)
    # 2.3. Type mismatch in expression
    def detectTypeMismatchInExpression(self, ctx, o: object):
        # ctx: ArrayCell, BinaryOp, UnaryOp, CallExpr
        #############
        # 2.3.1. ArrayCell(arr Expr, idx: List[Expr])
        # E1[E2]: E1: ArrayType, E2: List[NumberLiteral]
        if type(ctx) == ArrayCell:
            e1 = self.visit(ctx.arr, o)
            if e1 is not None and type(e1) != VoidType:
                if type(e1) != ArrayType:
                    raise TypeMismatchInExpression(ctx)
                for item in ctx.idx:
                    if type(self.visit(item, o)) != NumberType:
                        raise TypeMismatchInExpression(ctx)
        # 2.3.2. Binary and Unary expressions
        # 2.3.2.1. Binary expressions
        # BinaryOp(op: str, left: Expr, right: Expr)
        if isinstance(ctx, BinaryOp):
            e1 = self.visit(ctx.left, o)
            e2 = self.visit(ctx.right, o)
            if e1 is not None and e2 is not None:
                if ctx.op in ["+", "-", "*", "/", "%", "=", "!=", "<", ">", "<=", ">="]:
                    if type(e1) != NumberType or type(e2) != NumberType:
                        raise TypeMismatchInExpression(ctx)
                elif ctx.op in ["and", "or"]:
                    if type(e1) != BoolType or type(e2) != BoolType:
                        raise TypeMismatchInExpression(ctx)
                elif ctx.op in ["...", "=="]:
                    if type(e1) != StringType or type(e2) != StringType:
                        raise TypeMismatchInExpression(ctx)
        # 2.3.2.2. Unary expressions
        # UnaryOp(op: str, operand: Expr)
        if isinstance(ctx, UnaryOp):
            e = self.visit(ctx.operand, o)
            if ctx.op == "-" and type(e) != NumberType:
                raise TypeMismatchInExpression(ctx)
            elif ctx.op == "not" and type(e) != BoolType:
                raise TypeMismatchInExpression(ctx)
        # 2.3.3. Function call expressions
        # CallExpr(name: Id, args: List[Expr])
        if isinstance(ctx, CallExpr):
            for i in range(self.level, -1, -1):
                for item in self.declared[i]:
                    if type(item) == FuncObj and item.obj.name.name == ctx.name.name:
                        if type(item.returnType) == VoidType and item.obj.body is not None:
                            raise TypeMismatchInExpression(ctx)
                        if len(item.obj.param) != len(ctx.args):
                            raise TypeMismatchInExpression(ctx)
                        for j in range(len(ctx.args)):
                            arg = self.visit(ctx.args[j], o)
                            para = item.obj.param[j].varType
                            if type(para) == ArrayType:
                                if para.size != arg.size:
                                    raise TypeMismatchInExpression(ctx)
                                if type(para.eleType) != type(arg.eleType):
                                    raise TypeMismatchInExpression(ctx)
                            if type(arg) != type(para):
                                raise TypeMismatchInExpression(ctx)
                        return item.returnType
    # 2.4. Type cannot be inferred
    # TypeCannotBeInferred(stmt: Stmt)
    def detectTypeCannotBeInferred(self, ctx, o: object):
        # Stmt: VarDecl, Assign, If, For, Return, CallStmt, Block
        if isinstance(ctx, VarDecl):
            if ctx.varInit is not None:
                initType = self.visit(ctx.varInit, o)
                if type(initType) == VoidType:
                    initType = None
                if initType is None:
                    raise TypeCannotBeInferred(ctx)
        if isinstance(ctx, Assign):
            left = self.visit(ctx.lhs, o)
            right = self.visit(ctx.rhs, o)
            if left is None or type(left) == VoidType or right is None or type(right) == VoidType:
                raise TypeCannotBeInferred(ctx)
        elif isinstance(ctx, If):
            visitType = self.visit(ctx.expr, o)
            if visitType is None or type(visitType) == VoidType:
                raise TypeCannotBeInferred(ctx)
            for item in ctx.elifStmt:
                visitType = self.visit(item[0], o)
                if visitType is None or type(visitType) == VoidType:
                    raise TypeCannotBeInferred(ctx)
        elif isinstance(ctx, For):
            visitType = self.visit(ctx.name, o)
            if visitType is None or type(visitType) == VoidType:
                raise TypeCannotBeInferred(ctx)
            visitType = self.visit(ctx.condExpr, o)
            if visitType is None or type(visitType) == VoidType:
                raise TypeCannotBeInferred(ctx)
            visitType = self.visit(ctx.updExpr, o)
            if visitType is None or type(visitType) == VoidType:
                raise TypeCannotBeInferred(ctx)
        elif isinstance(ctx, Return):
            if ctx.expr is not None:
                visitType = self.visit(ctx.expr, o)
                if visitType is None or type(visitType) == VoidType:
                    raise TypeCannotBeInferred(ctx)
        elif isinstance(ctx, CallStmt):
            for arg in ctx.args:
                visitType = self.visit(arg, o)
                if visitType is None or type(visitType) == VoidType:
                    raise TypeCannotBeInferred(ctx)
    # 2.5. Type mismatch in statement
    # TypeMismatchInStatement(stmt: Stmt)
    def detectTypeMismatchInStatement(self, ctx: Stmt, o: object):
        # Variable declaration
        if isinstance(ctx, VarDecl):
            if ctx.varType is not None and ctx.varInit is not None:
                initType = self.visit(ctx.varInit, o)
                if type(ctx.varType) == ArrayType and type(initType) == ArrayType:
                    if initType.size != ctx.varType.size:
                        raise TypeMismatchInStatement(ctx)
                    if type(initType.eleType) != type(ctx.varType.eleType):
                        raise TypeMismatchInStatement(ctx)
                if type(initType) != type(ctx.varType):
                    raise TypeMismatchInStatement(ctx)
        # Assign statement
        elif isinstance(ctx, Assign):
            # Assign(lhs: Expr, rhs: Expr)
            left = self.visit(ctx.lhs, o)
            right = self.visit(ctx.rhs, o)
            # Lhs can be any type except VoidType
            if type(left) != VoidType:
                if type(left) == ArrayType and type(right) == ArrayType:
                    if left.size == right.size and type(left.eleType) == type(right.eleType):
                        return
                elif type(left) == type(right):
                    return
            raise TypeMismatchInStatement(ctx)
        # If statement
        elif isinstance(ctx, If):
            # If(expr: Expr, thenStmt: Stmt, elifStmt: List[Tuple(Expr, Stmt)], elseStmt: Stmt)
            visitType = self.visit(ctx.expr, o)
            if type(visitType) != BoolType:
                raise TypeMismatchInStatement(ctx)
            for item in ctx.elifStmt:
                visitType = self.visit(item[0], o)
                if type(visitType) != BoolType:
                    raise TypeMismatchInStatement(ctx)
        # For statement
        elif isinstance(ctx, For):
            # For(name: Id, condExpr: Expr, updExpr: Expr, body: Stmt)
            visitType = self.visit(ctx.name, o)
            if type(visitType) != NumberType:
                raise TypeMismatchInStatement(ctx)
            visitType = self.visit(ctx.condExpr, o)
            if type(visitType) != BoolType:
                raise TypeMismatchInStatement(ctx)
        # Call statement
        elif isinstance(ctx, CallStmt):
            # CallStmt(name: Id, args: List[Expr])
            # FuncDecl(name: Id, param: List[Expr], body: Stmt)
            for i in range(self.level, -1, -1):
                for item in self.declared[i]:
                    if type(item) == FuncObj and item.obj.name.name == ctx.name.name:
                        if type(item.returnType) != VoidType:
                            raise TypeMismatchInStatement(ctx)
                        if len(item.obj.param) != len(ctx.args):
                            raise TypeMismatchInStatement(ctx)
                        for j in range(len(ctx.args)):
                            arg = self.visit(ctx.args[j], o)
                            para = item.obj.param[j].varType
                            if type(arg) != type(para):
                                raise TypeMismatchInStatement(ctx)
                        # Corce type for function
                        if type(item.returnType) == VoidType and item.obj.body is None:
                            item.obj.body = Continue()
    # 2.6. No definition for a function
    def detectNoDefinition(self, ctx: FuncObj, o: object):
        if ctx.obj.body is None:
            raise NoDefinition(ctx.obj.name.name)
    # 2.7. Break / Continue not in loop
    def detectMustInLoop(self, ctx: Stmt):
        depth = self.depth
        for item in self.checkLoop[::-1]:
            if depth < 0:
                break
            if type(item.obj) == For and item.level == depth:
                return
            depth = depth - 1
        raise MustInLoop(ctx)
    # 2.8. No entry point
    def detectNoEntryPoint(self):
        for i in range(self.level, -1, -1):
            for item in self.declared[i]:
                if type(item) == FuncObj:
                    if item.obj.name.name == "main" and len(item.obj.param) == 0 and type(item.returnType) == VoidType:
                        return
        raise NoEntryPoint()
                    
    def visitProgram(self, ctx: Program, o: object):
        # Reset self.declared and self.level
        self.declared = [[]]
        self.level = 0
        # Built-in functions
        read_Number = FuncObj(FuncDecl(Id("readNumber"), [], Return()), NumberType())
        write_Number = FuncObj(FuncDecl(Id("writeNumber"), [VarDecl(Id("anArg"), NumberType(), None, None)], Return()), VoidType())
        read_Bool = FuncObj(FuncDecl(Id("readBool"), [], Return()), BoolType())
        write_Bool = FuncObj(FuncDecl(Id("writeBool"), [VarDecl(Id("anArg"), BoolType(), None, None)], Return()), VoidType())
        read_String = FuncObj(FuncDecl(Id("readString"), [], Return()), StringType())
        write_String = FuncObj(FuncDecl(Id("writeString"), [VarDecl(Id("anArg"), StringType(), None, None)], Return()), VoidType())
        self.declared[self.level] += [read_Number, write_Number, read_Bool, write_Bool, read_String, write_String]
        # Visit elements in Decl list
        for item in ctx.decl:
            self.visit(item, o)
        for i in range(self.level, -1, -1):
            for item in self.declared[i]:
                if type(item) == FuncObj:
                    self.detectNoDefinition(item, o)
        self.detectNoEntryPoint()

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.varInit is not None:
            initType = self.visit(ctx.varInit, o)
            if ctx.varType is not None and initType is None:
                if type(ctx.varInit) == Id:
                    self.corceVarType(ctx.varInit, ctx.varType)
            if ctx.varType is not None and type(initType) == VoidType:
                if type(ctx.varInit) == CallExpr:
                    self.corceFuncType(ctx.varInit, ctx.varType)
            if ctx.varType is not None and type(ctx.varType) == ArrayType and type(initType) == ArrayType:
                # if type(initType.eleType) == VoidType:
                #     for item in ctx.varInit.value:
                #         if type(self.visit(item, o)) == VoidType:
                #             while(type(item) != CallExpr):
                #                 item = self.visit(item, o)
                #             if len(ctx.varType.size) == 1:
                #                 self.corceFuncType(item, ctx.varType.eleType)
                #             else:
                #                 self.corceFuncType(item, ArrayType(ctx.varType.size[len(ctx.varType.size) - 1: ], ctx.varType.eleType))
                self.corceArrCellType(ctx.varInit, ctx.varType)
        self.detectRedeclared(ctx, o)
        self.detectTypeCannotBeInferred(ctx, o)
        self.detectTypeMismatchInStatement(ctx, o)
        if ctx.varInit is not None:
            initType = self.visit(ctx.varInit, o)
            var = VarObj(ctx, initType)
            self.declared[self.level].append(var)
            return initType
        else:
            var = VarObj(ctx, ctx.varType)
            self.declared[self.level].append(var)
            return ctx.varType
    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        flagPush = self.detectRedeclared(ctx, o)
        self.level = self.level + 1
        self.declared.append([])

        if len(self.stmtList) != 0:
            self.stmtList.clear()
        if len(self.checkLoop) != 0:
            self.checkLoop.clear()
        self.depth = 0
        returnType = None

        for para in ctx.param:
            par = VarObj(para, para.varType)
            self.declared[self.level].append(par)
        # Add function object into symbol table
        if flagPush is None:
            func = FuncObj(FuncDecl(ctx.name, ctx.param, None), VoidType())
            self.declared[self.level - 1].append(func)
            
        if type(ctx.body) == Block:
            self.level = self.level + 1
            self.declared.append([])
            returnType = self.visit(ctx.body, o)
            # Check type mismatch in return statement
            countReturn = 0
            for i in range(self.level, -1, -1):
                for item in self.declared[i]:
                    if type(item) == FuncObj and item.obj.name.name == ctx.name.name:
                        if returnType is not None and type(returnType) != VoidType and type(item.returnType) != VoidType:
                            if type(returnType) == ArrayType and type(item.returnType) == ArrayType:
                                if returnType.size != item.returnType.size:
                                    raise TypeMismatchInStatement(ctx.body)
                                if type(returnType.eleType) != type(item.returnType.eleType):
                                    raise TypeMismatchInStatement(ctx.body)
                            elif type(returnType) != type(item.returnType):
                                for stmt in self.stmtList:
                                    if type(stmt.obj) == Return:
                                        raise TypeMismatchInStatement(stmt.obj)    
                            

                        for bodyStmt in self.stmtList:
                            if type(bodyStmt) == Return:
                                countReturn = countReturn + 1
                                if type(self.visit(bodyStmt.obj, o)) != type(item.returnType) and countReturn > 1:
                                    raise TypeMismatchInStatement(bodyStmt.obj)
                        if type(returnType) == VoidType and type(item.returnType) != VoidType:
                            returnType = item.returnType

            # returnType = None
            self.declared.pop(self.level)
            self.level = self.level - 1
        elif type(ctx.body) == Return:
            if ctx.body.expr is not None:
                returnType = self.visit(ctx.body.expr, o)
            else:
                returnType = VoidType()
            if ctx.body.expr is not None and (returnType is None or type(returnType) == VoidType):
                raise TypeCannotBeInferred(ctx.body)
            # Check type mismatch in return statement
            if returnType is not None:
                for i in range(self.level, -1, -1):
                    for item in self.declared[i]:
                        if type(item) == FuncObj and item.obj.name.name == ctx.name.name:
                            if type(returnType) == ArrayType and type(item.returnType) == ArrayType:
                                if returnType.size != item.returnType.size:
                                    raise TypeMismatchInStatement(ctx.body)
                                if type(returnType.eleType) != type(item.returnType.eleType):
                                    raise TypeMismatchInStatement(ctx.body)
                            if type(returnType) != type(item.returnType) and type(item.returnType) != VoidType and item.obj.body is not None:
                                raise TypeMismatchInStatement(ctx.body)
                            if type(item.obj.body) == Continue:
                                if type(returnType) != type(item.returnType):
                                     raise TypeMismatchInStatement(ctx.body)
                                else:
                                    item.obj.body = ctx.body
        self.declared.pop(self.level)
        self.level = self.level - 1
        
        if returnType is not None:
            for i in range(self.level, -1, -1):
                for item in self.declared[i]:
                    if type(item) == FuncObj and item.obj.name.name == ctx.name.name:
                        item.obj.body = ctx.body
                        item.returnType = returnType
                        # print(item)
                        return returnType
        else:
            return VoidType()

    # corce type for variable
    def corceVarType(self, var: Id, varType: Type):
        for i in range(self.level, -1, -1):
            for item in self.declared[i]:
                if type(item) == VarObj:
                    if item.obj.name.name == var.name and item.varType is None:
                        item.varType = varType
                        break
            else:
                continue
            break
    # corce return type for function
    def corceFuncType(self, func: CallExpr, returnType: Type):
        for i in range(self.level, -1, -1):
            for item in self.declared[i]:
                if type(item) == FuncObj:
                    if item.obj.name.name == func.name.name and type(item.returnType) == VoidType and item.obj.body is None:
                        item.returnType = returnType
                        break
            else:
                continue
            break
    def corceArrCellType(self, arrLit, arrType):
        for item in arrLit.value:
            visitType = self.visit(item, arrLit)
            if type(visitType) == VoidType:
                while type(item) != CallExpr:
                    self.visit(item, arrLit)
                if len(arrType.size) == 1:
                    self.corceFuncType(item, arrType.eleType)
                else:
                    self.corceFuncType(item, ArrayType(arrType.size[len(arrType.size) - 1: ], arrType.eleType))
            if visitType is None:
                while type(item) != Id:
                    self.visit(item, arrLit)
                if len(arrType.size) == 1:
                    self.corceVarType(item, arrType.eleType)
                else:
                    self.corceVarType(item, ArrayType(arrType.size[len(arrType.size) - 1: ], arrType.eleType))
    def visitBinaryOp(self, ctx: BinaryOp, o: object):
        # BinaryOp(op: str, left: Expr, right: Expr)

        e1 = self.visit(ctx.left, o)
        if e1 is None or type(e1) == VoidType:
            if ctx.op in ['+', '-', '*', '/', '%', '=', '!=', '<', '>', '<=', '>=']:
                if e1 is None and type(ctx.left) == Id:
                    self.corceVarType(ctx.left, NumberType())
                elif type(e1) == VoidType and type(ctx.left) == CallExpr:
                    self.corceFuncType(ctx.left, NumberType())
            elif ctx.op in ['and', 'or']:
                if e1 is None and type(ctx.left) == Id:
                    self.corceVarType(ctx.left, BoolType())
                elif type(e1) == VoidType and type(ctx.left) == CallExpr:
                    self.corceFuncType(ctx.left, BoolType())
            elif ctx.op in ['...', '==']:
                if e1 is None and type(ctx.left) == Id:
                    self.corceVarType(ctx.left, StringType())
                elif type(e1) == VoidType and type(ctx.left) == CallExpr:
                    self.corceFuncType(ctx.left, StringType())
        
        e2 = self.visit(ctx.right, o)
        if e2 is None or type(e2) == VoidType:
            if ctx.op in ['+', '-', '*', '/', '%', '=', '!=', '<', '>', '<=', '>=']:
                if e2 is None and type(ctx.right) == Id:
                    self.corceVarType(ctx.right, NumberType())
                elif type(e2) == VoidType and type(ctx.right) == CallExpr:
                    self.corceFuncType(ctx.right, NumberType())
            elif ctx.op in ['and', 'or']:
                if e2 is None and type(ctx.right) == Id:
                    self.corceVarType(ctx.right, BoolType())
                elif type(e2) == VoidType and type(ctx.right) == CallExpr:
                    self.corceFuncType(ctx.right, BoolType())
            elif ctx.op in ['...', '==']:
                if e2 is None and type(ctx.right) == Id:
                    self.corceVarType(ctx.right, StringType())
                elif type(e2) == VoidType and type(ctx.right) == CallExpr:
                    self.corceFuncType(ctx.right, StringType())


        #################################
        #### Corce type - 1st version ###
        #################################

        # e1 = self.visit(ctx.left, o)
        # e2 = self.visit(ctx.right, o)
        # if e1 is None or type(e1) == VoidType or e2 is None or type(e2) == VoidType:
        #     if ctx.op in ['+', '-', '*', '/', '%', '=', '!=', '<', '>', '<=', '>=']:
        #         if e1 is None and type(ctx.left) == Id:
        #             self.corceVarType(ctx.left, NumberType())
        #         elif type(e1) == VoidType and type(ctx.left) == CallExpr:
        #             self.corceFuncType(ctx.left, NumberType())
        #         if e2 is None and type(ctx.right) == Id:
        #             self.corceVarType(ctx.right, NumberType())
        #         elif type(e2) == VoidType and type(ctx.right) == CallExpr:
        #             self.corceFuncType(ctx.right, NumberType())
        #     elif ctx.op in ['and', 'or']:
        #         if e1 is None and type(ctx.left) == Id:
        #             self.corceVarType(ctx.left, BoolType())
        #         elif type(e1) == VoidType and type(ctx.left) == CallExpr:
        #             self.corceFuncType(ctx.left, BoolType())
        #         if e2 is None and type(ctx.right) == Id:
        #             self.corceVarType(ctx.right, BoolType())
        #         elif type(e2) == VoidType and type(ctx.right) == CallExpr:
        #             self.corceFuncType(ctx.right, BoolType())
        #     elif ctx.op in ['...', '==']:
        #         if e1 is None and type(ctx.left) == Id:
        #             self.corceVarType(ctx.left, StringType())
        #         elif type(e1) == VoidType and type(ctx.left) == CallExpr:
        #             self.corceFuncType(ctx.left, StringType())
        #         if e2 is None and type(ctx.right) == Id:
        #             self.corceVarType(ctx.right, StringType())
        #         elif type(e2) == VoidType and type(ctx.right) == CallExpr:
        #             self.corceFuncType(ctx.right, StringType())
        self.detectTypeMismatchInExpression(ctx, o)
        if type(e1) is not None and type(e2) is not None and type(e1) == type(e2):
            if ctx.op in ['+', '-', '*', '/', '%']:
                return NumberType()
            elif ctx.op in ['and', 'or', '=', '!=', '<', '>', '<=', '>=', '==']:
                return BoolType()
            elif ctx.op == '...':
                return StringType()
                                        
    def visitUnaryOp(self, ctx: UnaryOp, o: object):
        # UnaryOp(op: str, operand: Expr)
        e = self.visit(ctx.operand, o)
        if e is None or type(e) == VoidType:
            if ctx.op == '-':
                if e is None and type(ctx.operand) == Id:
                    self.corceVarType(ctx.operand, NumberType())
                elif type(e) == VoidType and type(ctx.operand) == CallExpr:
                    self.corceFuncType(ctx.operand, NumberType())
            elif ctx.op == 'not':
                if e is None and type(ctx.operand) == Id:
                    self.corceVarType(ctx.operand, BoolType())
                elif type(e) == VoidType and type(ctx.operand) == CallExpr:
                    self.corceFuncType(ctx.operand, BoolType())
        self.detectTypeMismatchInExpression(ctx, o)
        if ctx.op == '-':
            return NumberType()
        elif ctx.op == 'not':
            return BoolType()
    def visitCallExpr(self, ctx: CallExpr, o: object):
        func = self.detectUndeclared(ctx, o)
        if len(func.obj.param) == len(ctx.args):
            for i in range(len(ctx.args)):
                arg = self.visit(ctx.args[i], o)
                if arg is None or type(arg) == Id:
                    self.corceVarType(ctx.args[i], func.obj.param[i].varType)
                elif type(arg) == VoidType and type(ctx.args[i]) == CallExpr:
                    self.corceFuncType(ctx.args[i], func.obj.param[i].varType)
        returnType = self.detectTypeMismatchInExpression(ctx, o)
        return returnType

    def visitAssign(self, ctx: Assign, o: object):
        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)
        if left is None or type(left) == VoidType:
            if right is not None and type(right) != VoidType:
                if left is None and type(ctx.lhs) == Id:
                    self.corceVarType(ctx.lhs, right)
                elif type(left) == VoidType and type(ctx.lhs) == CallExpr:
                    self.corceFuncType(ctx.lhs, right)
        if right is None or type(right) == VoidType:
            if left is not None and type(left) != VoidType:
                if right is None and type(ctx.rhs) == Id:
                    self.corceVarType(ctx.rhs, left)
                elif type(right) == VoidType and type(ctx.rhs) == CallExpr:
                    self.corceFuncType(ctx.rhs, left)
        self.detectTypeCannotBeInferred(ctx, o)
        self.detectTypeMismatchInStatement(ctx, o)
        return None

    def visitId(self, ctx: Id, o: object):
        varType = self.detectUndeclared(ctx, o)
        return varType
    def visitArrayCell(self, ctx: ArrayCell, o: object):
        # ArrayCell(arr: Expr, idx: List[Expr])
        # ArrayType(size: List[float], Type)
        self.detectTypeMismatchInExpression(ctx, o)
        arrType = self.visit(ctx.arr, o)
        if arrType is not None and type(arrType) == ArrayType:
            if len(ctx.idx) == len(arrType.size):
                return arrType.eleType
            else:
                return ArrayType(arrType.size[len(ctx.idx):], arrType.eleType)
    def visitIf(self, ctx: If, o: object):
        # If(expr: Expr, thenStmt Stmt, elifStmt: List[Tuple(Expr, Stmt)], elseStmt: Stmt)
        visitType = self.visit(ctx.expr, o)
        if visitType is None and type(ctx.expr) == Id:
            self.corceVarType(ctx.expr, BoolType())
        if type(visitType) == VoidType and type(ctx.expr) == CallExpr:
            self.corceFuncType(ctx.expr, BoolType())
        for item in ctx.elifStmt:
            visitType = self.visit(item[0], o)
            if visitType is None and type(item[0]) == Id:
                self.corceVarType(item[0], BoolType())
            if type(visitType) == VoidType and type(item[0]) == CallExpr:
                self.corceFuncType(item[0], BoolType())
        self.detectTypeCannotBeInferred(ctx, o)
        self.detectTypeMismatchInStatement(ctx, o)
        self.depth = self.depth + 1
        # Visit thenStmt
        self.visit(ctx.thenStmt, o)
        self.stmtList.append(StmtObj(ctx.thenStmt, self.depth))
        # Visit elifStmt
        for item in ctx.elifStmt:
            self.visit(item[1], o)
            self.stmtList.append(StmtObj(item[1], self.depth))
        if ctx.elseStmt is not None:
            self.visit(ctx.elseStmt, o)
            self.stmtList.append(StmtObj(ctx.elseStmt, self.depth))
        self.depth = self.depth - 1
        return None

    def visitFor(self, ctx: For, o: object):
        # For(name: Id, condExpr: Expr, updExpr: Expr, body: Stmt)
        # corce type for name
        visitType = self.visit(ctx.name, o)
        if visitType is None:
            self.corceVarType(ctx.name, NumberType())
        # corce type for condExpr
        visitType = self.visit(ctx.condExpr, o)
        if visitType is None and type(ctx.condExpr) == Id:
            self.corceVarType(ctx.condExpr, BoolType())
        elif type(visitType) == VoidType and type(ctx.condExpr) == CallExpr:
            self.corceFuncType(ctx.condExpr, BoolType())
        # corce type for updExpr
        visitType = self.visit(ctx.updExpr, o)
        if visitType is None and type(ctx.updExpr) == Id:
            self.corceVarType(ctx.updExpr, NumberType())
        elif type(visitType) == VoidType and type(ctx.updExpr) == CallExpr:
            self.corceFuncType(ctx.updExpr, NumberType())
        self.detectTypeCannotBeInferred(ctx, o)
        self.detectTypeMismatchInStatement(ctx, o)
        # Visit body stmt
        self.depth = self.depth + 1
        self.visit(ctx.body, o)
        self.stmtList.append(StmtObj(ctx.body, self.depth))
        self.depth = self.depth - 1
        return None

    def visitBreak(self, ctx: Break, o: object):
        self.detectMustInLoop(ctx)
        return None
    def visitContinue(self, ctx: Continue, o: object):
        self.detectMustInLoop(ctx)
        return None
    def visitReturn(self, ctx: Return, o: object):
        # Return (expr: Expr)
        if ctx.expr is None:
            return VoidType()
        else:
            returnType = self.visit(ctx.expr, o)
            flagReturn = False
            for item in self.stmtList:
                if type(item.obj) == Return:
                    flagReturn = True
            if returnType is not None and flagReturn == True:
                return returnType
            if returnType is None:
                for item in self.stmtList:
                    # Finally
                    if type(item.obj) == Return:
                        flagReturn = True
                        objReturn = VoidType()
                        if item.obj.expr is not None:
                            objReturn = self.visit(item.obj.expr, o)
                        returnType = objReturn
                        if type(ctx.expr) == Id and type(objReturn) != VoidType:
                            self.corceVarType(ctx.expr, returnType)
                        elif type(ctx.expr) == CallExpr:
                            self.corceFuncType(ctx.expr, returnType)
                        break
            if flagReturn == True:
                return returnType
        self.detectTypeCannotBeInferred(ctx, o)
    def visitCallStmt(self, ctx: CallStmt, o: object):
        # FuncDecl(name: Id, param: List[VarDecl]. body: Stmt = None)
        # CallStmt(name: Id, args: List[Expr])
        func = self.detectUndeclared(ctx, o)
        if len(func.obj.param) == len(ctx.args):
            for i in range(len(ctx.args)):
                arg = self.visit(ctx.args[i], o)
                if arg is None and type(ctx.args[i]) == Id:
                    self.corceVarType(ctx.args[i], func.obj.param[i].varType)
                if type(arg) == VoidType and type(ctx.args[i]) == CallExpr:
                    self.corceFuncType(ctx.args[i], func.obj.param[i].varType)
        self.detectTypeMismatchInStatement(ctx, o)
        self.detectTypeCannotBeInferred(ctx, o)
        return None
    def visitBlock(self, ctx: Block, o: object):
        # Block(stmt: List[Stmt])
        self.stmtList.append(StmtObj(ctx, self.depth))
        self.checkLoop.append(StmtObj(ctx, self.depth))
        self.depth = self.depth + 1
        for item in ctx.stmt:
            self.checkLoop.append(StmtObj(item, self.depth))
            returnType = self.visit(item, o)
            if returnType is not None and type(item) == Return:
                self.stmtList.append(StmtObj(item, self.depth, returnType))
            else:
                self.stmtList.append(StmtObj(item, self.depth))
            # self.visit(item, o)
        self.depth = self.depth - 1
        returnList = []

        for item in self.stmtList:
            if type(item.obj) == Return:
                if len(returnList) == 0:
                    returnList.append(item.obj)
                else:
                    ret = self.visit(returnList[0], o)
                    nextRet = self.visit(item.obj, o)
                    if type(nextRet) != VoidType and type(ret) != type(nextRet):
                        raise TypeMismatchInStatement(item.obj)
        if len(returnList) != 0:
            return self.visit(returnList[0], o)
        return VoidType()
    def visitNumberType(self, ctx: NumberType, o: object):
        pass
    def visitBoolType(self, ctx: BoolType, o: object):
        pass
    def visitStringType(self, ctx: StringType, o: object):
        pass
    def visitArrayType(self, ctx: ArrayType, o: object):
        pass
    def visitVoidType(self, ctx: ArrayType, o: object):
        pass
    def visitNumberLiteral(self, ctx: NumberLiteral, o: object):
        return NumberType() 
    def visitStringLiteral(self, ctx: StringLiteral, o: object):
        return StringType()
    def visitBooleanLiteral(self, ctx: BooleanLiteral, o: object):
        return BoolType()
    def visitArrayLiteral(self, ctx: ArrayLiteral, o: object):
        # ArrayLiteral(value: List[Expr])
        # ArrayType(size: List[float], eleType: Type)
        firstEle = ctx.value[0]
        sizeList = [float(len(ctx.value))]
        visitType = self.visit(firstEle, o)
        if type(visitType) == VoidType:
            funcCall = firstEle
            while type(funcCall) != CallExpr:
                funcCall = self.visit(funcCall, o)
            # if len(ctx.value) > 1:
            for item in ctx.value:
                ele = self.visit(item, o)
                if ele is None or type(ele) == VoidType:
                    continue
                self.corceFuncType(funcCall, ele)
                visitType = ele
        if visitType is None:
            iden = firstEle
            while type(iden) != Id:
                iden = self.visit(iden, o)
            # if len(ctx.value) > 1:
            for item in ctx.value:
                ele = self.visit(item, o)
                if ele is None or type(ele) == VoidType:
                    continue
                self.corceVarType(iden, ele)
                visitType = ele
        for item in ctx.value:
            visitEle = self.visit(item, o)
            if visitEle is None and type(item) == Id:
                self.corceVarType(item, visitType)
            elif type(visitEle) == VoidType and type(item) == CallExpr:
                self.corceFuncType(item, visitType)
        if type(visitType) != ArrayType:
            for item in ctx.value[1:]:
                ele = self.visit(item, o)
                if ele is None and type(item) == Id and visitType is not None:
                    self.corceVarType(item, visitType)
                elif type(ele) == VoidType and type(item) == CallExpr and visitType is not None:
                    self.corceFuncType(item, visitType)
                elif type(ele) != type(visitType):
                    raise TypeMismatchInExpression(ctx)
            return ArrayType(sizeList, visitType)
        else:
            ##### Corce type for array cell #####
            cellType = None
            for item in ctx.value:
                cellType = self.visit(item, o)
                if cellType is None or type(cellType) == VoidType:
                    continue
                if type(cellType) == ArrayType and (cellType.eleType is None or type(cellType.eleType) == VoidType):
                    continue
                break
            for item in ctx.value:
                if self.visit(item, o) is None:
                    self.corceVarType(item, cellType)
                elif type(self.visit(item, o)) == VoidType:
                    self.corceFuncType(item, cellType)
                elif type(self.visit(item, o) == ArrayType) and self.visit(item, o).eleType is None or type(self.visit(item, o).eleType) == VoidType:
                    self.corceArrCellType(item, cellType)

            for i in range(len(ctx.value) - 1):
                type1 = self.visit(ctx.value[i], o)
                type2 = self.visit(ctx.value[i + 1], o)
                if type(type1) == ArrayType and type(type2) == ArrayType:
                    if type1.size != type2.size:
                        raise TypeMismatchInExpression(ctx)
                    if type(type1.eleType) != type(type2.eleType):
                        raise TypeMismatchInExpression(ctx)
                if type(type1) != type(type2):
                    raise TypeMismatchInExpression(ctx)
            innerArray = self.visit(firstEle, o)
            sizeList += innerArray.size
            visitType = innerArray.eleType
            return ArrayType(sizeList, visitType)