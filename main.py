from latte.front import LatteFront
from latte.front.ir_gen import IRGenerator

frontend = LatteFront('testcases/test.lt')
# frontend.print()

gen = IRGenerator('test')
mod = frontend.transform(gen)
mod.print()
