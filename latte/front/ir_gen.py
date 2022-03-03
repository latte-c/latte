from .parser import LatteFront, ASTNode
from ..ir.base import *
from ..ir.instruction import *
from ..utils.sym_tab import SymbolTable

# a virtual reg allocator 
class RegAllocator:
    def __init__(self):
        self.index = 0
    
    def new(self, type: Type) -> Reg:
        reg = Reg(type, str(self.index))
        self.index += 1
        return reg

class LabelAllocator:
    def __init__(self):
        self.index = 0
    
    def new(self) -> Label:
        label = Label('L{}'.format(self.index))
        self.index += 1
        return label

class IRGenerator:
    def __init__(self, module_name: str):
        self.module_name = module_name

    def __call__(self, ast: ASTNode):
        self.ir_module = Module(self.module_name)
        self.sym_tab = SymbolTable()
        self.visit(ast)
        return self.ir_module
    
    def enter_procedure(self, ir_func: Function):
        self.reg_alloc = RegAllocator()
        self.label_alloc = LabelAllocator()
        self.ir_func = ir_func
        scope = self.sym_tab.open_scope()
        for param in ir_func.params:
            scope[param.name] = param
    
    def leave_procedure(self):
        self.ir_module.add_function(self.ir_func)
        self.ir_func = None
        self.sym_tab.close_scope()
    
    def add_var(self, name: str, reg: Reg):
        self.sym_tab.current_scope()[name] = reg
    
    def emit(self, directive: Directive):
        self.ir_func.add(directive)
    
    def visit_compilation_unit(self, node: ASTNode):
        # TODO: import_declarations
        for child in node[1]:
            self.visit(child)
    
    def visit_procedure_declaration(self, node: ASTNode):
        # TODO: EXPORT qualifier
        ret_type = self.visit(node[1])
        fn_name = node[2]
        params = list(map(lambda t: Reg(self.visit_latte_type(t[0]), t[1]), node[3]))
        ir_func = Function(fn_name, ret_type, params, [])
        self.enter_procedure(ir_func)
        for stmt in node[4]:
            self.visit(stmt)
        self.leave_procedure()

    def visit_block_statement(self, node: ASTNode):
        self.sym_tab.open_scope()
        for stmt in node:
            self.visit(stmt)
        self.sym_tab.close_scope()
    
    def visit_var_statement(self, node: ASTNode):
        var_type = self.visit_latte_type(node[0])
        for var_name, expr in node[1]:
            lhs = self.reg_alloc.new(var_type)
            self.add_var(var_name, lhs)
            # TODO: optimize for r-valued rhs？
            if isinstance(expr, ASTNode):
                rhs = self.visit(expr)
                self.emit(Move(lhs, rhs))
            else:
                imm = Constant(expr)
                self.emit(LoadImm(lhs, imm))
    
    def visit_assign_statement(self, node: ASTNode):
        lhs = self.visit_access_expression(node[0])
        rhs = self.visit_expression(node[1])
        # TODO: emit store instruction
        if isinstance(rhs, Constant):
            self.emit(LoadImm(lhs, rhs))
        else:
            self.emit(Move(lhs, rhs))
    
    def visit_return_statement(self, node: ASTNode):
        val = self.visit_expression(node[0])
        self.emit(Return(val))
    
    def visit_if_statement(self, node: ASTNode):
        cond = self.visit_expression(node[0])
        has_else = node[2] is not None
        true_label = self.label_alloc.new()
        end_label = self.label_alloc.new()
        false_label = self.label_alloc.new() if has_else else end_label

        self.emit(CondBranch(cond, true_label, false_label))
        self.emit(true_label)
        self.visit(node[1])
        if has_else:
            self.emit(Branch(end_label))
            self.emit(false_label)
            self.visit(node[2])
        self.emit(end_label)
    
    def visit_binary_expression(self, node: ASTNode) -> Reg:
        op = node[1]
        src0 = self.visit_expression(node[0])
        src1 = self.visit_expression(node[2])
        # assert type of src0 and type of src1 is compatible
        dst_type = src0.type + src1.type
        dst = self.reg_alloc.new(dst_type)

        arith_map = {
            '+': ArithmeticOp.ADD,
            '-': ArithmeticOp.SUB,
            '*': ArithmeticOp.MUL,
            '/': ArithmeticOp.DIV,
            '%': ArithmeticOp.MOD,
        }
        cmp_map = {
            '==': IntCompareOp.EQ,
            '!=': IntCompareOp.NE,
            '<' : IntCompareOp.LT,
            '<=': IntCompareOp.LE,
            '>' : IntCompareOp.GT,
            '>=': IntCompareOp.GE,
        }
        if op in arith_map:
            self.emit(Arithmetic(arith_map[op], dst, src0, src1))
        elif op in cmp_map:
            # TODO: distinguish between int and other types
            self.emit(IntCompare(cmp_map[op], dst, src0, src1))
        return dst

    def visit_access_expression(self, node: ASTNode) -> Reg:
        # TODO: add array support
        reg = self.sym_tab.lookup(node[0])
        assert reg is not None
        return reg

    def visit_expression(self, expr: ASTNode | int | float) -> Value:
        return self.visit(expr) if isinstance(expr, ASTNode) else Constant(expr)

    def visit_latte_type(self, node: ASTNode) -> Type:
        # TODO: char, string, array shape
        type_str, width = node[0]
        match type_str:
            case 'int':
                return int_type(width)
            case 'real':
                return float_type(width)
            case _:
                return ERR_T

    def visit(self, node: ASTNode):
        attrs = dir(self)
        fn_name = 'visit_{}'.format(node.name)

        if fn_name in attrs:
            visit_fn = getattr(self, fn_name)
            return visit_fn(node)
        
        # for child in node.children:
        #     if isinstance(child, ASTNode):
        #         self.visit(child)
