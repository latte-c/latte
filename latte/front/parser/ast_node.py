from typing import Any


class ASTNode:
    def __init__(self, name: str, children: list) -> None:
        self.name = name
        self.children = children

    def __getitem__(self, key: int) -> Any:
        return self.children[key]

    def __len__(self) -> int:
        return len(self.children)
