from typing import TypeVar, Optional, List, Dict

T = TypeVar('T')

class SymbolTable:
    def __init__(self):
        self.scopes: List[Dict[str, T]] = []
    
    def open_scope(self):
        self.scopes.append({})
        return self.current_scope()
    
    def close_scope(self):
        self.scopes.pop()
    
    def current_scope(self) -> Dict[str, T]:
        return self.scopes[-1]
    
    def lookup(self, name: str) -> Optional[T]:
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None
