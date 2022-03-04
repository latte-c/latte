from .cfg import BasicBlock, CFG
from typing import List, Set, Any, Sequence
from functools import reduce

def set_intersect(sets: Sequence[Set[Any]]) -> Set[Any]:
    return set(reduce(lambda a, b: a & b, sets))

def compute_dominators(cfg: CFG) -> List[Set[int]]:
    '''
    compute dominators using the well-known iterative algorithm
    requires the first block to be the entry
    '''
    dom = [{0}]
    n = len(cfg)
    for i in range(1, n):
        dom.append(set(range(n)))
    
    changed = True
    while changed:
        changed = False
        for i in range(1, n):
            t = {i} | set_intersect(dom[j] for j in cfg.pred(i))
            if dom[i] != t:
                dom[i] = t
                changed = True
    return dom

def strict_dominators(dom: List[Set[int]]) -> List[Set[int]]:
    return [s - {i} for i, s in enumerate(dom)]

def naive_immediate_dominators(dom: List[Set[int]]) -> List[int]:
    '''
    this algorithm is adapted from the "whale book"
    however correctness is not guaranteed. use the fast dominance algorithm instead
    '''
    tmp = strict_dominators(dom)
    for i in range(1, len(dom)):
        removal = set()
        for j in tmp[i]:
            for k in tmp[i]:
                if j != k and k in tmp[j]:
                    removal.add(k)
        tmp[i] -= removal # correctness not proven

    # entry node n0 has no immediate dominator, we use 0 here to represent this
    tmp[0].add(0)
    return list(map(lambda s: s.pop(), tmp))

class Counter:
    def __init__(self):
        self.v = 0
    
    def inc(self):
        self.v += 1
    
    def get(self) -> int:
        return self.v

def compute_immediate_dominators(cfg: CFG) -> List[int]:
    '''
    fast algorithm by Keith D. Cooper et al.
    see "A Simple, Fast Dominance Algorithm" or "Engineering a Compiler" for more information
    '''
    # compute RPO (reverse postorder) for the graph
    n = len(cfg)
    counter = Counter()
    rpo = compute_rpo(cfg, [0] * n, [False] * n, 0, counter)
    inv_rpo = { v: i for i, v in enumerate(rpo) } # inverse mapping

    idoms = [-1] * n # use -1 instead of `undefined` in the literature
    idoms[0] = 0
    changed = True
    while changed:
        changed = False
        for i in range(1, n):
            b = inv_rpo[i]
            preds = iter(cfg.pred(b))
            new_idom = next(preds)
            for p in preds:
                if idoms[p] != -1:
                    new_idom = intersect(idoms, rpo, p, new_idom)
            if idoms[b] != new_idom:
                idoms[b] = new_idom
                changed = True
    return idoms

def intersect(idoms: List[int], rpo: List[int], u: int, v: int):
    '''
    returns LCA of node u and v in the dominance tree
    '''
    while u != v:
        while rpo[u] > rpo[v]:
            u = idoms[u]
        while rpo[v] > rpo[u]:
            v = idoms[v]
    return u

def compute_rpo(cfg: CFG, rpo: List[int], visited: List[bool], u: int, counter: int):
    '''
    post-order dfs
    '''
    visited[u] = True
    for v in cfg.succ(u):
        if not visited[v]:
            compute_rpo(cfg, rpo, visited, v, counter)
    rpo[u] = len(cfg) - 1 - counter.get()
    counter.inc()
    return rpo
