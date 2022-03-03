from latte.front import LatteFront
from latte.front.ir_gen import IRGenerator
from latte.ir.cfg import BasicBlock, CFG, build_cfg

frontend = LatteFront('testcases/test.lt')
# frontend.print()

gen = IRGenerator('test')
mod = frontend.transform(gen)
mod.print()

for f in mod.functions.values():
    cfg = build_cfg(f)
    cfg.print()
