from enum import Enum, auto
from contextlib import contextmanager


_arithmetics = (
    'add',
    'sub',
    'neg',
    'eq',
    'gt',
    'lt',
    'and',
    'or',
    'not'
)

SP = 0

class CommandType:
    C_PUSH = auto()
    C_POP = auto()

def increment_SP():
    global SP
    s = f'@{SP}\nM=M+1\n'
    SP += 1
    return s

def constant(value):
   s1 = f'@{value}\nD=A\n' 
   s2 = f'@{SP}\nA=M\nM=D\n'
   s3 = increment_SP()
   return s1 + s2 + s3

_segments = {'constant': constant}

def push(segment, value):
    return _segments[segment](value)

def pop(segment, value): pass

class CodeWriter:
    method_dict = {'push': push,
                   'pop': pop}

    def __init__(self, filename):
        self.file = open(filename, 'w')

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