from .base import Value, Reg, Constant, Directive, Label
from typing import List
from enum import Enum, unique, auto

class Instruction(Directive):
    def __init__(self, dsts: List[Reg], srcs: List[Value]):
        self.srcs = srcs
        self.dsts = dsts
    
    def get_name(self) -> str:
        raise NotImplementedError

class Unary(Instruction):
    def __init__(self, dst: Reg, src: Value):
        super().__init__([dst], [src])
    
    def __str__(self):
        dst = self.dsts[0]
        return '{} = {}.{} {}'.format(dst, self.get_name(), dst.type, self.srcs[0])

class Binary(Instruction):
    def __init__(self, dst: Reg, src0: Value, src1: Value):
        super().__init__([dst], [src0, src1])
    
    def __str__(self):
        dst = self.dsts[0]
        return '{} = {}.{} {}, {}'.format(dst, self.get_name(), dst.type, self.srcs[0], self.srcs[1])

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
    
    def get_name(self) -> str:
        op2name = {
            ArithmeticOp.ADD: 'add',
            ArithmeticOp.SUB: 'sub',
            ArithmeticOp.MUL: 'mul',
            ArithmeticOp.DIV: 'div',
            ArithmeticOp.MOD: 'mod',
        }
        return op2name[self.op]

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
    
    def get_name(self) -> str:
        op2name = {
            IntCompareOp.EQ: 'eq',
            IntCompareOp.NE: 'ne',
            IntCompareOp.LT: 'lt',
            IntCompareOp.LE: 'le',
            IntCompareOp.GT: 'gt',
            IntCompareOp.GE: 'ge'
        }
        return 'icmp.{}'.format(op2name[self.op])

class Terminator(Instruction):
    pass

class Branch(Terminator):
    def __init__(self, target: Label):
        super().__init__([], [])
        self.target = target
    
    def __str__(self):
        return 'br {}'.format(self.target)

class CondBranch(Terminator):
    def __init__(self, cond: Value, true_label: Label, false_label: Label):
        super().__init__([], [cond])
        self.true_label = true_label
        self.false_label = false_label

    def __str__(self):
        return 'br i1 {}, {}, {}'.format(self.srcs[0], self.true_label, self.false_label)

class Return(Terminator):
    def __init__(self, value: Value):
        super().__init__([], [value])
    
    def __str__(self):
        val = self.srcs[0]
        return 'ret.{} {}'.format(val.type, val)

class LoadImm(Unary):
    def __init__(self, dst: Reg, imm: Constant):
        super().__init__(dst, imm)
    
    def get_name(self) -> str:
        return 'load_imm'

class Move(Unary):
    def __init__(self, dst: Reg, src: Reg):
        super().__init__(dst, src)
    
    def get_name(self) -> str:
        return 'mov'