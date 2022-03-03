from .base import Function, Label
from .instruction import Instruction, Branch, CondBranch, Return, Terminator, NOP
from typing import List, Dict, Set, Sequence, Tuple, Optional

class BasicBlock:
    def __init__(self, label: Optional[Label], code: List[Instruction]):
        self.label = label
        self.code = code
    
    def __getitem__(self, index: int) -> Instruction:
        return self.code[index]
    
    def __len__(self):
        return len(self.code)

class CFG:
    def __init__(self, nodes: List[BasicBlock]):
        self.nodes = nodes
        self.edges = []
        for i in range(len(nodes)):
            self.edges.append((set(), set()))
    
    def __getitem__(self, index: int) -> BasicBlock:
        return self.nodes[index]
    
    def add_edge(self, u: int, v: int):
        n = len(self.nodes)
        assert 0 <= u < n and 0 <= v < n
        self.edges[u][0].add(v)
        self.edges[v][1].add(u)
    
    def succ(self, u: int) -> Set[int]:
        return self.edges[u][0]

    def succ_blocks(self, u: int) -> Sequence[BasicBlock]:
        return (self.nodes[v] for v in self.succ(u))
    
    def succ_items(self, u: int) -> Sequence[Tuple[int, BasicBlock]]:
        return ((v, self.nodes[v]) for v in self.succ(u))
    
    def print(self):
        for i, bb in enumerate(self.nodes):
            print('BB{} {}'.format(i, '' if bb.label is None else bb.label))
            for instr in bb.code:
                print('   ', instr)
        for i in range(len(self.edges)):
            for j in self.edges[i][0]:
                print('({}, {})'.format(i, j))
    
def remove_redundant_labels(f: Function):
    label_info = { str(label): [i, False] for i, label in enumerate(f.body) if isinstance(label, Label) }
    for branch in f.body:
        if isinstance(branch, Branch):
            label = branch.target
            label_info[str(label)][1] = True
        elif isinstance(branch, CondBranch):
            label_info[str(branch.true_label)][1] = True
            label_info[str(branch.false_label)][1] = True
    
    # original indices of labels to be removed 
    indices = sorted([i for i, referenced in label_info.values() if not referenced])
    for i in reversed(indices):
        f.body.pop(i)

def build_cfg(f: Function) -> CFG:
    remove_redundant_labels(f)

    entry = BasicBlock(Label('entry'), [NOP])
    exit = BasicBlock(Label('exit'), [NOP])

    bbs: List[BasicBlock] = [entry]
    code: List[Instruction] = []
    label = None

    for item in f.body:
        if isinstance(item, Label):
            if len(code) > 0:
                bbs.append(BasicBlock(label, code))
            label = item
            code = []
        elif isinstance(item, Instruction):
            code.append(item)
            if isinstance(item, Terminator):
                bbs.append(BasicBlock(label, code))
                label = None
                code = []
    if label is not None or len(code) > 0:
        bbs.append(BasicBlock(label, code))
    bbs.append(exit)

    label2node = { str(bb.label): i for i, bb in enumerate(bbs) if bb.label is not None }
    cfg = CFG(bbs)
    n = len(bbs)
    for i, bb in enumerate(bbs):
        instr = bb[-1] if len(bb) > 0 else NOP
        if isinstance(instr, Branch):
            j = label2node[str(instr.target)]
            cfg.add_edge(i, j)
        elif isinstance(instr, CondBranch):
            j = label2node[str(instr.true_label)]
            k = label2node[str(instr.false_label)]
            cfg.add_edge(i, j)
            cfg.add_edge(i, k)
        elif isinstance(instr, Return):
            cfg.add_edge(i, n - 1) # add an edge to $exit
        else:
            if i + 1 < n:
                cfg.add_edge(i, i + 1)
    return cfg
