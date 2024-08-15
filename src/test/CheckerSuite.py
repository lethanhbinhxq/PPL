import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = """string b
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_2(self):
        input = """bool b
        bool b
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_3(self):
        input = """
        func main() 
            return
        
        func main() 
            return
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_4(self):
        input = """
        func main(bool b, bool b) 
            return 0
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 404))
    
    def test_5(self):
        input = """
            string a
            bool b
            string c <- "2"
            bool d <- false
        
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_6(self):
        input = """
            string a <- "b" ... "c"
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_7(self):
        input = """
            string a <- "b" ... 5
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., StringLit(b), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_8(self):
        input = """
            number s2 <- "1" ... "2"
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(s2), NumberType, None, BinaryOp(..., StringLit(1), StringLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_9(self):
        input = """
            bool a <- ("b" ... "c") == ("a" ... "a") 
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """
            bool a <- false
            bool b <- true and a
            bool c <- (false and not a) and b
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """
            bool a <- (false and not a)
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """
            bool a <- false
        
            func main()
            begin 
                bool b <- a and (10 >= 10)
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """
            string j <- "100"
            string k <- "200" ... "300"
            string l <- j ... k
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """
            func greeting(string hi, string bye)
                return "Hello"

            func main() 
                return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """
            func hello(string hi, string hi)
                return "Hello"

            func main() 
                return
        """
        expect = "Redeclared Parameter: hi"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """
            func hello(string x, string y)
            
            func main() 
                return

            func hello(string z, string t)
                return "Hello world"
               """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
            func hello(string hi, string bye)
            
            func main() 
                return "Hello"

            func hello(number abc, string xyz)
                return 1
               """

        expect = "Redeclared Function: hello"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
            func hello(string day, string night)
            
            func main() 
                return 

            func hello(string day, string noon, string night)
                return "Hello"
               """
        expect = "Redeclared Function: hello"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
            func zero(number j, number k)
            
            func main() 
                return 0

            func zero(number j, number k)
                return 0

            func zero(number j, number k)
                return 0
               """
        expect = "Redeclared Function: zero"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """
            func zero(number x, number y)
            
            func main() 
                return 0

            func zero(number x, number y)
               """
        expect = "Redeclared Function: zero"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """
            var x <- -9 + 10
            func main()
                return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """
            var x <- 219 - false
            func main()
                return
        """
        expect = "Type Mismatch In Expression: BinaryOp(-, NumLit(219.0), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """
            var x <- 6
            var y <- 15 + x
            var z <- -y <= x
            var t <- y or not z
            
            func main()
                return
            
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, Id(y), UnaryOp(not, Id(z)))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """
            var x <- 3
            var z <- y > x
            var t <- 8 + z
                
            func main()
            begin            
                return
            end
        """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
            var x <- 0
            var y <- x = 0
            var z <- 100 * y
                
            func main()
            begin            
                return
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(*, NumLit(100.0), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """
            func f(string s, bool b)
                
            func main() 
                return
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """
            func hello() 
            
        """
        expect = "No Function Definition: hello"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """
            number x
            func main()
            string y <- "Hello"
            bool z <- true
            func main() 
                return 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))
    
    def test_29(self):
        input = """
            dynamic x
            dynamic y
            dynamic z <- x / y
            func main()
                return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """
            dynamic x
            dynamic y <- x
            number a
            func main()
                return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, dynamic, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """
            dynamic x
            dynamic y
            dynamic z <- x ... y
            dynamic t <- z and false

            func main()
                return
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(z), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """
            bool flag1
            bool flag2
            func main()
            begin
                flag1 <- flag2
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """
            string x
            var y <- 1
            func main()
            begin
                x <- "Hello " ... "world"
                x <- false
                return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """
            dynamic x
            dynamic y
            func main()
            begin
                x <- true
                x <- y
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """
            dynamic x
            dynamic y
            func main()
            begin
                x <- true or false
                y <- x
                y <- 100
                return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), NumLit(100.0))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """
            number x
            number y
            func main()
            begin
                if (x = y) 
                    return
                elif (x > y) 
                    return
                else
                    return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """
            dynamic x
            dynamic y
            func main()
            begin
                if (x) 
                    return
                elif (y) 
                    return
                else
                    x <- y
                    y <- 456
                    return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), NumLit(456.0))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """
            func hello()
                return
            func main()
            begin
                hello()
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """
            func f(string s)
                return
            func main()
            begin
                dynamic x
                f(x)
                x <- false
                return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """
            func f()
                return
            func main()
            begin
                dynamic f
                f()
                var x <- 1
                return
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """
            func f()
                return
            func main()
            begin
                number x
                f(x)
                dynamic a
                return
            end
        """       
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """
            func hello()
                return "Hello World"
            func main()
            begin
                hello()
                return
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(hello), [])"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
            func f()
                return "a"
            func main()
            begin
                dynamic x <- f()
                x <- false
            end
        """       
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
            func f()
                return "abc"
            func main()
            begin
                number x <- f()
            end
        """        
        
        expect = "Type Mismatch In Statement: VarDecl(Id(x), NumberType, None, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
            func f()
            
            func main()
            begin
                dynamic x <- f()
                x <- false
            end

            func f()
                return "abc"
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """
            func f1()
                return "2"
            func f2()
                return "1"
            func main()
            begin
                dynamic c <- f2() - f1()

            end
        """       
        expect = "Type Mismatch In Expression: BinaryOp(-, CallExpr(Id(f2), []), CallExpr(Id(f1), []))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """
            func f(string x)
            
            func main()
            begin
                number a <- f("1")
            end

            func f(string x)
                return false
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_48(self):
        input = """
            func f()
            begin
                if (true) 
                    return "true"
                else 
                    return true
                number x <- 1 + 1
            end
            func main()
            begin
                var x <- f()
            end
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_49(self):
        input = """
            func f()
            begin
                return f()
            end
            func main()
            begin
                number y <- 1
                var x <- f()
                string z <- ""
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
            func f(number x)
            begin
                if (x = 1)
                    return 1
                else
                    return f(x * 2)        
            end

            func main()
            begin
                var x <- f(9)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """
            func f(number x)
    
            func main()
            begin
                number a <- f(9)
                string x
                string y
                string z
            end
    
            func f(number y)
            begin
                if (y > 0)
                    return f(1 / y)
                elif (y = 0)
                    return 0
                else
                    return false
    
            end
    
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_52(self):
        input = """
            func f(number x)
    
            func main()
            begin
                dynamic x <- f(1) or false
            end
    
            func f(number x)
            begin
                if (x = 1)
                    return f(x - 1)
                elif (x = 2)
                    return true
                else
                    return 1
    
            end
    
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """
            func main()
            begin
                number i <- 1
                for i until i >= 9 by 2
                    return 1
            end
        """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """
            func main()
            begin
                dynamic i
                var x <- 1
                x <- x + 1
                for i until i > 100 by 20
                    break 
                break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_55(self):
        input = """
            func main()
            begin
                if (true)
                    var x <- 1
                for i until i >= 5 by 2
                    break
            end
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_56(self):
        input = """
            func main()
            begin
                number x <- 1 + 1
                dynamic i
                string s <- "Hello"
                for i until i >= 100 by 10
                    continue
                continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_57(self):
        input = """
            func main()
            begin
                number i <- 10
                for i until i >= 50 by 10
                begin
                    for i until i >= 30 by 1
                    begin
                        break
                        break
                    end
                    continue
                    continue
                end
                break                
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_58(self):
        input = """
            func f1()
            func f2()
            func f3()

            func main()
            begin
                dynamic a
                dynamic b
                dynamic c
                dynamic d
                for a until b >= c by d
                begin
                    continue
                end
                var x <- a + b + c + d

                for a until f1() by f2()
                begin
                    f3()
                end

                number y <- f2()
                bool z <- f1()
                
            end

            func f()
                return true
            func f2()
                return 0
            func f3()
                return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_59(self):
        input = """
            func main()
            begin
                if (false)
                    return 1
                else
                    return false
            end
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_60(self):
        input = """
            func f()
                return 1
            
            func main()
            begin
                if (f())
                    return 1
                else
                    return 0
            end
        """
        expect = "Type Mismatch In Statement: If((CallExpr(Id(f), []), Return(NumLit(1.0))), [], Return(NumLit(0.0)))"
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_61(self):
        input = """
            func f()
            
            func main()
            begin
                dynamic x
                if (f())
                    return false
                elif (x)
                    return x
                else
                    return f()
            end

            func f()
                return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_62(self):
        input = """
            func main()
            begin
                number arr[10]
                arr[3] <- 0
                arr[4] <- 2
                arr[5] <- 4
                arr[6] <- 6
                arr[7] <- 8
                arr[8] <- 10
                arr[9] <- false
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr), [NumLit(9.0)]), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_63(self):
        input = """
            func main()
            begin
                number arr[9]
                arr[1] <- 2
                arr[3] <- 4
                arr[5] <- 6
                arr[7] <- 8
                arr[2] <- 10
                arr[4] <- 12
                arr <- 14
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(arr), NumLit(14.0))"
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_64(self):
        input = """
            func main()
            begin
                dynamic y
                number arr[6]
                arr[0] <- 8
                arr[1] <- 7
                arr[2] <- 6
                arr[3] <- 5
                arr[4] <- 4
                arr[5] <- 3
                y <- arr[2]
                y <- false
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_65(self):
        input = """
            func main()
            begin
                dynamic x
                number arr[3]
                arr[0] <- 11
                arr[1] <- 12
                arr[2] <- 13
                x <- arr
                x <- 100
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), NumLit(100.0))"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_66(self):
        input = """
            func f1()
            func f2()
            func main()
            begin
                dynamic x
                number arr[3]
                arr[0] <- f1()
                x <- arr
                x <- f2()
            end

            func f1()
                return 1
            func f2()
                return false
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_67(self):
        input = """
            func f()
            func f2()
                return [1,2,3]
            func main()
            begin
                dynamic x
                number a[3]
                x <- a
                x <- f2()
                x[1] <- f()

            end

            func f()
                return f2()

        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(f2), []))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """
            func foo(number arr[10])
                return arr[10]
            func main()
            begin
                number x[10]
                dynamic y <- foo(x)
                y <- false
            end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_69(self):
        input = """
        
            func main()
            begin
                number arr[2] <- [5, 6, 7, 8]
 
            end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(5.0), NumLit(6.0), NumLit(7.0), NumLit(8.0)))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """
            func main()
            begin
                number x <- [9,8,7,6,5]
                
            end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), NumberType, None, ArrayLit(NumLit(9.0), NumLit(8.0), NumLit(7.0), NumLit(6.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test_71(self):
        input = """
            func f()
                return [6,7,8,9,0]
            func main()
            begin
                
                dynamic x <- [2,3,4,5,6]
                number y[5] <- [4,5,6,7,8]
                dynamic z <- y 
                dynamic t <- f()
            end
        """
        
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    def test_72(self):
        input = """
            func f(number a[6])
                return 0
            func main()
            begin
                number a[5] <- [2,3,4,5,6]
                a[1] <- f(a) 
            end

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = """
            func f()
                return 0
            func f2()
            func f3()
            func main()
            begin
                dynamic y
                number x[5] <- [2 + 3, f(), f2(), y, f3()]
                x[3] <- y
            end

            func f2()
                return 1
            func f3()
                return false
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        input = """
            func main()
            begin
                number arr[3,2] <- [[2,3],[4,5],[6,8]]
                arr[0,1] <- 2
                arr[2] <- [7,9]
                arr[1] <- 0
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr), [NumLit(1.0)]), NumLit(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = """
            func main()
            begin
                number x[3,2] <- [[9,8],[7,6],[5]]
                
            end
        """       
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(9.0), NumLit(8.0)), ArrayLit(NumLit(7.0), NumLit(6.0)), ArrayLit(NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = """
            func f()
            func main()
            begin
                number arr[3,2] <- [f(), f(), f()]
                arr[0] <- f()
            end

            func f()
                return [7,8,9]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(7.0), NumLit(8.0), NumLit(9.0)))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = """
            func f()
            func main()
            begin
                number arr[3,2] <- [f(), [1,2], [3,4]]
                arr[0,0] <- f()
            end

            func f()
                return [5,6]
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr), [NumLit(0.0), NumLit(0.0)]), CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_78(self):
        input = """
            func f()
            func main()
            begin
                dynamic x
                number arr[3,2] <- [f(), x, [1,2]]
                x <- arr[2]
                arr[0,1] <- x
            end

            func f()
                return [4,5,6]
        """       
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(arr), [NumLit(0.0), NumLit(1.0)]), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """
            number x <- 2 % "Hi"
            func main()
                return
            """               
        expect = "Type Mismatch In Expression: BinaryOp(%, NumLit(2.0), StringLit(Hi))"
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test_80(self):
        input = """
            func f1()

            func main()
            begin
                string s <- f2(5)
            end
            """
        expect = "Undeclared Function: f2"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """
            func hello()

            number hello
            dynamic a  <- "Hello"
            func main()
                return
            """
        expect = "No Function Definition: hello"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_82(self):
        input = """
            func g(bool x)
            begin
                return g(x)
            end

            func main()
            begin
                var a <- g(true)
            end
            """     
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(g), [Id(x)]))"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_83(self):
        input = """
            func f(string s)
            begin
                return true
            end

            func main()
            begin
                f("Hello")
            end
            """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [StringLit(Hello)])"
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test_84(self):
        input = """
            func main()
            begin
                break
            end
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_85(self):
        input = """
            func main()
            begin
                var x <- 1
                var y <- 2
                var z <- 3
                continue
            end
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 485))
    
    def test_86(self):
        input = """
            string s1
            string s2
            func concat()
                return s1 ... s2

            func main()
            begin
                s1 <- readString()
                s2 <- readString()
                writeString(concat())
            end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """
            func f(bool x)

            func main()
            begin
                var x <- f(true)
            end

            func f(bool x)
            begin
                return f(x)
            end
            """               
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, CallExpr(Id(f), [BooleanLit(True)]))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """
            func absDiff(number a, number b)
            begin
                if (a > b) return (a - b)
                return (b - a)
            end
            func main()
            begin
                number a <- readNumber()
                number b <- readNumber()
                number c <- readNumber()
                writeNumber(absDiff(absDiff(a,b),c))
            end
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))
    
    def test_89(self):
        input = """
            func g(number f)
            begin
                if (f < 0) return 0
                elif (f = 3) return 3
                else return g(f) * g(f / 2)
            end

            func main()
            begin 
                dynamic x
                number y <- g(x)
                x[1] <- [4,8,0]
            end
            """               
        expect = "Type Mismatch In Expression: ArrayCell(Id(x), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """
            func main()
            begin 
                dynamic x
                dynamic y
                number arr[2,2] <- [x, y]
                x <- [1,2]
                y <- [3,4]
                writeNumber(x[1] + y[1])
            end
            """               
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
            func main()
                begin
                    var a <- 1
                    var b <- 2
                    print(a, b)
                end
            """               
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """
            func main()
            begin
                dynamic o
                dynamic m
                dynamic n
                number arr[2,2] <- [o,[m,3]]
                o <- 1
                m <- 2
                n <- true
            end
            """               
        expect = "Type Mismatch In Statement: AssignStmt(Id(o), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """
            dynamic arr
            func main()
            begin
                var x <- arr[40,90] - 100
            end
            """               
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, BinaryOp(-, ArrayCell(Id(arr), [NumLit(40.0), NumLit(90.0)]), NumLit(100.0)))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """
            func f()
            var f <- f()

            func main()
                return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(f), None, var, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_95(self):
        input = """
            func f()
                return 123
            
            func main()
                string s <- "Hello" ... " world!"
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
            func f(number f)
                return f()
            
            func main()
            begin
                number f <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = """
            func main()
            begin
                dynamic x
                dynamic y <- x[3, 4, 5] 

            end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, dynamic, ArrayCell(Id(x), [NumLit(3.0), NumLit(4.0), NumLit(5.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """
            func main()
            begin
                dynamic x
                var y <- 1 + 1 + 1 + 1 + 1
                string s
                bool a[4, 5] <- x[4, 5]
            end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), ArrayType([4.0, 5.0], BoolType), None, ArrayCell(Id(x), [NumLit(4.0), NumLit(5.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
            func main()
            begin
                dynamic x
                dynamic y
                dynamic z
                var array <-[[x],[y],[z],["Hello"]]
            end             

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_500(self):
        input = """
            func g(number x[5], number y[5])
                return 
            func main()
            begin
                g([10,9,8,7,6], [5,4,3,2,"1"])
            end             

        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(5.0), NumLit(4.0), NumLit(3.0), NumLit(2.0), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 500))