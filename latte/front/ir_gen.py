from .parser import LatteFront, ASTNode
from ..ir.base import *

# a virtual reg allocator 
class RegAllocator:
    def __init__(self):
        self.index = 0
    
    def new(self, type: Type) -> Reg:
        reg = Reg(type, str(self.index))
        self.index += 1
        return reg

class IRGenerator:
    def __init__(self, module_name: str):
        self.module_name = module_name

    def __call__(self, ast: ASTNode):
        self.module = Module(self.module_name)
        self.visit(ast)
        return self.module
    
    def visit_compilation_unit(self, node: ASTNode):
        # TODO: import_declarations
        for child in node[1]:
            self.visit(child)
    
    def visit_procedure_declaration(self, node: ASTNode):
        # TODO: EXPORT qualifier
        ret_type = self.visit(node[1])
        fn_name = node[2]
        ir_func = Function(fn_name, ret_type, [], [])
        self.module.add_function(ir_func)

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
        
        for child in node.children:
            if isinstance(child, ASTNode):
                self.visit(child)
