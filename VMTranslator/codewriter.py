from functools import wraps
from contextlib import contextmanager

from .command import Command

#_arithmetics = (
#    'add',
#    'sub',
#    'neg',
#    'eq',
#    'gt',
#    'lt',
#    'and',
#    'or',
#    'not'
#)

class StackPointer:
    def __init__(self):
        self.address = 0
        self.value = 256

    def increment(self):
        self.value += 1
        comment = '// increment stack pointer\n'
        return comment + f'@{SP.address}\nM=M+1\n'

    def decrement(self):
        self.value -= 1
        comment = '// decrement stack pointer\n'
        return comment + f'@{SP.address}\nM=M-1\n'

SP = StackPointer()


class VMCommand: pass


def decrement_sp_on_call(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    res = f(*args, **kwargs)
    SP.decrement()
    return res
  return wrapper


class LogicalVMCommand(VMCommand):
  def __init__(self):
    self.labelcount = 0

class Eq(LogicalVMCommand):
    def __init__(self):
        super().__init__()

    @decrement_sp_on_call
    def __call__(self):
        return (
          '// eq\n'
         f'@{SP.value - 1}\n'
          'D=M\n'
         f'@{SP.value - 2}\n'
          'D=D-M\n'
         f'@EQ{self.labelcount}\n'
          'D;JNE\n'
          '// if equal:\n'
          '@{SP.value - 2}\n'
          'M=-1\n'
         f'(EQ{self.labelcount})\n'
          '// if not equal\n'
         f'@{SP.value - 2}\n'
          'M=1\n'
        )

class Gt(LogicalVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return ()












def constant(value):
    comment = f'// push constant {value}\n'
    s1 = f'@{value}\nD=A\n' 
    s2 = f'@{SP.address}\nA=M\nM=D\n'
    s3 = SP.increment()
    return comment + s1 + s2 + s3


def add(): 
    comment = '// add\n'
    s1 = f'@{SP.value - 1}\nD=M\n'
    s2 = f'@{SP.value - 2}\nM=D+M\n'
    s3 = SP.decrement()
    return comment + s1 + s2 + s3

def sub():
    comment = '// sub\n'
    s1 = f'@{SP.value - 1}\nD=M\n'
    s2 = f'@{SP.value - 2}\nM=D-M\n'
    s3 = SP.decrement()
    return comment + s1 + s2 + s3

def neg():
    comment = '// neg\n'
    s1 = f'@{SP.value - 1}\nM=-M'
    return comment + s1

def eq():
    comment = '// eq\n'
    s1 = f'@{SP.value - 1}\nD=M\n'
    s2 = f'@{SP.value - 2}\nM=D&M\n'
    s3 = SP.decrement()
    return comment + s1 + s2 + s3

def gt(): pass

_segments = {'constant': constant}

def push(segment, value):
    return _segments[segment](value)

def pop(segment, value): pass

class CodeWriter:
    method_dict = {
        'push': push,
        'pop': pop
    }

    arithmetic_dict = {
        'add': add,
        'sub': sub,
        'neg': neg,
        'eq': eq,

    }

    def __init__(self, filename):
        self.file = open(filename, 'w')

    def _write_arithmetic(self, command):
        f = self.arithmetic_dict[command.arg0]
        self.file.write(f())

    def _write_push_pop(self, command):
        ctype, *args = command
        f = self.method_dict[ctype]
        self.file.write(f(*args))

    def write_command(self, command):
        if command.type.value == 'push':
            self._write_push_pop(command)
        else:
            self._write_arithmetic(command)

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
    with new_codewriter('testfile.asm') as cw:
        string = Command('push constant 7'.split())
        cw.write_command(string)
        string = Command('push constant 8'.split())
        cw.write_command(string)
        cw.write_command(Command('sub'.split()))
