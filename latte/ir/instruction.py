from .base import Value, Reg, Directive
from typing import List
from enum import Enum, unique, auto

class Instruction(Directive):
    def __init__(self, dsts: List[Reg], srcs: List[Value]):
        self.srcs = srcs
        self.dsts = dsts

class Unary(Instruction):
    def __init__(self, dst: Reg, src: Value):
        super().__init__([dst], [src])

class Binary(Instruction):
    def __init__(self, dst: Reg, src0: Value, src1: Value):
        super().__init__([dst], [src0, src1])

# TODO: add op, sub-op, qualifiers etc. for binary instruction

@unique
class ArithmeticOp(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()

class Arithmetic(Binary):
    def __init__(self, op: ArithmeticOp, dst: Reg, src0: Value, src1: Value):
        super().__init__(dst, src0, src1)
        self.op = op

@unique
class IntCompareOp(Enum):
    EQ = auto()
    NE = auto()
    LT = auto()
    LE = auto()
    GT = auto()
    GE = auto()

class IntCompare(Binary):
    def __init__(self, op: IntCompareOp, dst: Reg, src0: Value, src1: Value):
        super().__init__(dst, src0, src1)
        self.op = op

class Terminator(Instruction):
    pass

class Branch(Terminator):
    pass

class Return(Terminator):
    pass
