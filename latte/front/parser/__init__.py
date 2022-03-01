# this package serves as building the tree with antlr4 visitor
# and re-export this tree for further usage

from .ast_node import ASTNode
from .ast_visitor import ASTVisitor
from . import LatteLexer
from . import LatteParser
from antlr4 import FileStream, CommonTokenStream

# only use this class to parse latte file


def print_tree(node, indent: int = 0):
    print(' ' * indent, end='')
    if isinstance(node, ASTNode):
        print(f'{{{node.name}}} [')
        for item in node.children:
            print_tree(item, indent + 2)
        print(' ' * indent + ']')
    elif isinstance(node, list):
        print('<list> [')
        for item in node:
            print_tree(item, indent + 2)
        print(' ' * indent + ']')
    else:
        print(node)


class LatteFront:
    def __init__(self, filename: str) -> None:
        self.filename = filename

        input_filestream = FileStream(filename, encoding='utf-8')
        lexer = LatteLexer.LatteLexer(input_filestream)
        stream = CommonTokenStream(lexer)
        parser = LatteParser.LatteParser(stream)
        tree = parser.compilationUnit()

        visitor = ASTVisitor()
        self.ast_tree: ASTNode = visitor.visitCompilationUnit(tree)

    def print(self):
        print_tree(self.ast_tree)


        # only expose this only
__all__ = ['LatteFront', 'ASTNode']
