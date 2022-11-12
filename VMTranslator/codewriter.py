from collections import deque, namedtuple
from enum import Enum, auto
from contextlib import contextmanager


#'add',
#'sub',
#'neg',
#'eq',
#'gt',
#'lt',
#'and',
#'or',
#'not'

class CommandType:
    C_PUSH = auto()
    C_POP = auto()


def register_ram_slot(address, value):
    _registry.append(RAMSlot(address, value))

RAMSlot = namedtuple('RAMSlot', ['address', 'value'])
_registry = deque()


class StackPointer:
    def __init__(self):
        self.address = 0
        self.value = 256

    def increment(self):
        self.value += 1
        return f'@{SP.address}\nM=M+1\n'

    def decrement(self):
        self.value -= 1
        return f'@{SP.address}\nM=M-1\n'

SP = StackPointer()

def constant(value):
    s1 = f'@{value}\nD=A\n' 
    s2 = f'@{SP.address}\nA=M\nM=D\n'
    register_ram_slot(SP.value, value)
    s3 = SP.increment()
    return s1 + s2 + s3

def add(): 
    slot1 = _registry.pop()
    slot2 = _registry.pop()
    s1 = f'@{slot1.address}\nD=M\n'
    s2 = f'@{slot2.address}\nM=D+M\n'
    register_ram_slot(slot2.address, slot1.value + slot2.value)
    s3 = SP.decrement()
    return s1 + s2 + s3

_segments = {'constant': constant}

def push(segment, value):
    return _segments[segment](value)

def pop(segment, value): pass

class CodeWriter:
    method_dict = {'push': push,
                   'pop': pop}

    arithmetic_dict = {'add': add}

    def __init__(self, filename):
        self.file = open(filename, 'a')

    def write_arithmetic(self, command):
        f = self.arithmetic_dict[command.arg0]
        self.file.write(f())

    def write_push_pop(self, command):
        ctype, *args = command
        f = self.method_dict[ctype]
        self.file.write(f(*args))

    def close(self):
        self.file.close()

@contextmanager
def new_codewriter(filename):
    cw = CodeWriter(filename)
    try:
        yield cw
    finally:
        cw.close()

if __name__ == '__main__':
    from parser import Command

    with new_codewriter('testfile.asm') as cw:
        string = Command('push constant 7'.split())
        cw.write_push_pop(string)
        string = Command('push constant 8'.split())
        cw.write_push_pop(string)
        cw.write_arithmetic(Command('add'.split()))