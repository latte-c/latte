from .base import Value, Reg, Directive
from typing import List

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
