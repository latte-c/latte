from typing import List, Dict, Optional
from enum import unique, auto, Enum

@unique
class BaseType(Enum):
    INT = auto()
    FP = auto()
    ERR = auto()

INT_T = BaseType.INT
FP_T = BaseType.FP

class Type:
    def __init__(self, type: BaseType, width: int):
        self.type = type
        self.width = width
    
    def __str__(self):
        match self.type:
            case BaseType.INT:
                s = 'i{}'.format(self.width)
            case BaseType.FLOAT:
                s = 'f{}'.format(self.width)
            case _:
                s = '<err-type>'
        return s

def int_type(width: int=32) -> Type:
    return Type(INT_T, width)

def float_type(width: int=32) -> Type:
    return Type(FP_T, width)

I32 = int_type(32)
F32 = float_type(32)
ERR_T = Type(BaseType.ERR, 0)

def infer_type(value: int | float) -> Type:
    if isinstance(value, int):
        return I32
    elif isinstance(value, float):
        return F32
    return ERR_T

class Value:
    def __init__(self, type):
        self.type = type

class Constant(Value):
    def __init__(self, value: int | float, type: Optional[Type]=None):
        super().__init__(infer_type(value) if type is None else type)
        self.value = value

class Reg(Value):
    def __init__(self, type: Type, index: int):
        super().__init__(type)
        self.index = index

class Directive:
    pass

class Label(Directive):
    def __init__(self, name: str):
        self.name = name

class Function:
    def __init__(self, name: str, ret_type: Type, params: List[Reg], body: List[Directive]):
        self.name = name
        self.ret_type = ret_type
        self.params = params
        self.body = body

class Module:
    def __init__(self, name: str):
        self.name = name
        self.directives: List[Directive] = []
        self.functions: Dict[str, Function] = {}

    def add_directive(directive: Directive):
        self.directives.append(directive)
    
    def add_function(function: Function):
        self.functions[function.name] = function
