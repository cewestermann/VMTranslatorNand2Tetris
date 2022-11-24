from functools import wraps
from contextlib import contextmanager
from collections import namedtuple

from .command import Command


class StackPointer:
    def __init__(self):
        self.address = 0
        self.value = 256

    def increment(self):
        self.value += 1
        return self._put_comment() + f'@{self.address}\nM=M+1\n'

    def decrement(self):
        self.value -= 1
        return self._put_comment() + f'@{self.address}\nM=M-1\n'

    def _put_comment(self):
        return f'// increment {type(self).__name__}\n'


SP = StackPointer()


def decrement_sp_on_call(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    res = f(*args, **kwargs)
    return res + SP.decrement()
  return wrapper


class VMCommand: pass


class ArithmeticVMCommand(VMCommand):
    def __init__(self):
        self.labelcount = 0

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.__name__ != 'Not':
            cls.__call__ = decrement_sp_on_call(cls.__call__)

    @staticmethod
    def _compare_op():
        return (
           f'@{SP.value - 1}\n'
            'D=M\n'
           f'@{SP.value - 2}\n'
            'D=D-M\n'
        )

    @property
    def _clslabel(self):
        return f'{type(self).__name__.upper()}'

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


class Eq(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._assemble_boolean('D;JNE\n')


class Gt(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._assemble_boolean('D+1;JGT\n')


class Lt(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self._assemble_boolean('D-1;JLT\n')


class And(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        text = '// and\n'   
        text += f'@{SP.value - 1}\n'
        text += 'D=M\n'
        text += f'@{SP.value - 2}\n'
        text += 'M=D&M\n'
        return text


class Or(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        text = '// or\n'   
        text += f'@{SP.value - 1}\n'
        text += 'D=M\n'
        text += f'@{SP.value - 2}\n'
        text += 'M=D|M\n'
        return text


class Not(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        text = '// not\n'
        text += f'@{SP.value - 1}\n'
        text += 'M=!M\n'
        return text

def add(): 
    comment = '// add\n'
    s1 = f'@{SP.value - 1}\nD=M\n'
    s2 = f'@{SP.value - 2}\nM=D+M\n'
    s3 = SP.decrement()
    return comment + s1 + s2 + s3

def sub():
    comment = '// sub\n'
    s1 = f'@{SP.value - 1}\nD=M\n'
    s2 = f'@{SP.value - 2}\nM=M-D\n'
    s3 = SP.decrement()
    return comment + s1 + s2 + s3

def neg():
    comment = '// neg\n'
    s1 = f'@{SP.value - 1}\nM=-M'
    return comment + s1


Segment = namedtuple('Segment', ['address', 'base'])

LCL = Segment(1, 300)
ARG = Segment(2, 400)
THIS = Segment(3, 3000)
THAT = Segment(4, 3010)


class PushVMCommand(VMCommand):
    @staticmethod
    def constant(value):
        comment = f'// push constant {value}\n'
        text = comment + f'@{value}\nD=A\n'
        text += f'@{SP.address}\nA=M\nM=D\n'
        return text + SP.increment()

    @staticmethod
    def local(value):
        comment = f'// push local {value}\n'

    @staticmethod
    def that(value): pass

    @staticmethod
    def this(value): pass

    @staticmethod
    def temp(value): pass


def pushpop(obj, segment, value):
    return getattr(obj, segment)(value)


_method_dict = {
    'push': PushVMCommand,
    'pop': pushpop,
}

_arithmetic_dict = {
    'add': add,
    'sub': sub,
    'neg': neg,
    'eq': Eq(),
    'lt': Lt(),
    'gt': Gt(),
    'and': And(),
    'or': Or(),
    'not': Not()
}


class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, 'w')

    def _write_arithmetic(self, command):
        f = _arithmetic_dict[command.arg0]
        self.file.write(f())

    def _write_push_pop(self, command):
        ctype, *args = command
        obj = _method_dict[ctype]
        self.file.write(pushpop(obj, *args))

    def write_command(self, command):
        if command.type.value in ('push', 'pop'):
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


