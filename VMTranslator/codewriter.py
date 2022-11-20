from functools import wraps
from contextlib import contextmanager

from .command import Command


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

def decrement_sp_on_call(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    res = f(*args, **kwargs)
    return res + SP.decrement()
  return wrapper


class VMCommand: pass


class BooleanVMCommand(VMCommand):
    def __init__(self):
        self.labelcount = 0

    @staticmethod
    def _compare_op():
        return (
           f'@{SP.value - 1}\n'
            'D=M\n'
           f'@{SP.value - 2}\n'
            'D=D-M\n'
        )

    def _condition_result(self):
        # True part
        text = self._true_branch()
        text += self._put_end_label_reference()
        text += self._put_uncond_jump()

        # False part
        text += self._put_label()
        text += self._false_branch()
        text += self._put_end_label()
        return text

    def _false_branch(self):
        text =  f'// if not {self._clslabel}\n'
        text += f'@{SP.value - 2}\n'
        text +=  'M=0\n'
        return text

    def _true_branch(self):
        text = (
            f'// if {self._clslabel}\n'
            f'@{SP.value - 2}\n'
             'M=-1\n' # Word of ones (true)
        )
        return text

    @property
    def _clslabel(self):
        return f'{type(self).__name__.upper()}'

    @staticmethod
    def _put_uncond_jump():
        return f'0;JMP\n'

    def _put_label_reference(self):
        return f'@{self._clslabel}{self.labelcount}\n'

    def _put_label(self):
        return f'({self._clslabel}{self.labelcount})\n'

    def _put_end_label_reference(self):
        return f'@END_{self._clslabel}{self.labelcount}\n'

    def _put_end_label(self):
        return f'(END_{self._clslabel}{self.labelcount})\n'

    def _assemble_boolean(self, jump_cond):
        text = f'// {self._clslabel}\n'
        text += self._compare_op()
        text += self._put_label_reference()
        text += jump_cond
        text += self._condition_result()

        self.labelcount += 1
        return text


class Eq(BooleanVMCommand):
    def __init__(self):
        super().__init__()

    @decrement_sp_on_call
    def __call__(self):
        return self._assemble_boolean('D;JNE\n')


class Gt(BooleanVMCommand):
    def __init__(self):
        super().__init__()

    @decrement_sp_on_call
    def __call__(self):
        return self._assemble_boolean('D;JLT\n')


class Lt(BooleanVMCommand):
    def __init__(self):
        super().__init__()

    @decrement_sp_on_call
    def __call__(self):
        return self._assemble_boolean('D;JGT\n')


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

_segments = {'constant': constant}

def push(segment, value):
    return _segments[segment](value)


class CodeWriter:
    method_dict = {
        'push': push,
    }

    arithmetic_dict = {
        'add': add,
        'sub': sub,
        'neg': neg,
        'eq': Eq(),
        'lt': Lt(),
        'gt': Gt(),
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


