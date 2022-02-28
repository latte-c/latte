# this package serves as building the tree with antlr4 visitor
# and re-export this tree for further usage

from .ast_node import ASTNode

# only use this class to parse latte file


class LatteFront:
    def __init__(self) -> None:
        pass


# only expose this only
__all__ = ['LatteFront', 'ASTNode']
