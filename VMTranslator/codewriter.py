from functools import wraps
from contextlib import contextmanager
from pathlib import Path

from .command import Command, CommandType


FILENAME = None


def set_filename(filename):
    global FILENAME
    FILENAME = filename


class StackPointer:
    def __init__(self):
        self.address = 0
        self.value = 256 # TODO: Should not keep track of the value here
                         # Should be done exclusively in assembly
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


def _clsvariable(obj):
    return f'{type(obj).__name__}'


class VMCommand: pass


class BooleanVMCommand(VMCommand):
    def __init__(self, name, jump_condition):
        self.labelcount = 0
        self.name = name
        self._jmp_cond = jump_condition

    @decrement_sp_on_call
    def __call__(self):
        text = f'// {self.name}\n'
        text += self._compare_op()
        text += self._put_label_reference()
        text += self._jmp_cond
        text += self._condition_result()

        self.labelcount += 1
        return text

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
        text =  f'// if not {self.name}\n'
        text += f'@{SP.value - 2}\n'
        text +=  'M=0\n'
        return text

    def _true_branch(self):
        text = (
            f'// if {self.name}\n'
            f'@{SP.value - 2}\n'
             'M=-1\n' # Word of ones (true)
        )
        return text

    @staticmethod
    def _put_uncond_jump():
        return f'0;JMP\n'

    def _label_and_count(self):
        return f'{self.name}{self.labelcount}'

    def _put_label_reference(self):
        return f'@{self._label_and_count()}\n'

    def _put_label(self):
        return f'({self._label_and_count()})\n'

    def _put_end_label_reference(self):
        return f'@END_{self._label_and_count()}\n'

    def _put_end_label(self):
        return f'(END_{self._label_and_count()})\n'


# TODO: Maybe refactor these out into plain functions ? 
class ArithmeticVMCommand(VMCommand):
    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.__name__ != 'Not' and cls.__name__ != 'Neg':
            cls.__call__ = decrement_sp_on_call(cls.__call__)
    

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


class Add(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        text = '// add\n'
        text += f'@{SP.value - 1}\nD=M\n'
        text += f'@{SP.value - 2}\nM=D+M\n'
        return text


class Sub(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        text = '// sub\n'
        text += f'@{SP.value - 1}\nD=M\n'
        text += f'@{SP.value - 2}\nM=M-D\n'
        return text


class Neg(ArithmeticVMCommand):
    def __init__(self):
        super().__init__()

    def __call__(self):
        text = '// neg\n'
        text += f'@{SP.value - 1}\nM=-M'
        return text
        

class MemorySegment:
    def __init__(self, address, base, name):
        self.address = address
        self.base = base
        self.name = name

        self.labelcount = 1

    def _put_variable_ref(self):
        return f'@{_clsvariable(self) + str(self.labelcount)}\n'

    def _save_segment_address(self, offset):
        text = f'@{offset}\n'
        text += 'D=A\n' # Set D to offset
        text += f'@{self.address}\n'
        text += 'D=D+M\n'
        text += self._put_variable_ref()
        text += 'M=D\n' # Save base + offset in variable
        return text

    def _push_from_segment(self, offset):
        text = f'@{offset}\n'
        text += 'D=A\n' # Set D to offset
        text += f'@{self.address}\n'
        text += 'A=D+M\n'
        text += 'D=M\n'
        return text

    def _set_value(self):
        text = self._put_variable_ref()
        text += 'A=M\n' # Go to base + offset
        text += 'M=D\n' # Set base + offset to value from stack
        return text

    # TODO: Refactor push/pop
    def push(self, offset):
        text = f'// push {self.name} {offset}\n'
        text += self._push_from_segment(offset)
        text += f'@{SP.value}\n'
        text += 'M=D\n' # Push segment value to stack
        text += SP.increment()

        self.labelcount += 1
        return text

    def pop(self, offset):
        text = f'// pop {self.name} {offset}\n'
        text += self._save_segment_address(offset)
        text += f'@{SP.value - 1}\n'
        text += f'D=M\n'
        text += self._set_value()
        text += SP.decrement()

        self.labelcount += 1
        return text

    def change_base(self, newvalue):
        text = f'// Change base of {self.name} to {newvalue}\n'
        text += f'@{newvalue}\n'
        text += 'D=M\n'
        text += f'@{self.address}\n'
        text += 'M=D\n'
        return text
        


class TempSegment: # TODO: Refactor
    def __init__(self):
        self.base = 5
        self.name = 'temp'

    def push(self, offset):
        text = f'// push {self.name} {offset}\n'
        text += f'@{self.base + int(offset)}\n'
        text +=  'D=M\n'
        text += f'@{SP.value}\n'
        text +=  'M=D\n'
        text += SP.increment()
        return text

    def pop(self, offset):
        text = f'// pop {self.name} {offset}\n'
        text += f'@{SP.value - 1}\n'
        text += 'D=M\n'
        text += f'@{self.base + int(offset)}\n'
        text += 'M=D\n'
        text += SP.decrement()
        return text


class StaticSegment:
    def __init__(self):
        self.name = 'static'

    def push(self, offset):
        text = f'@{FILENAME}.{offset}\n'
        text += 'D=M\n'
        text += f'@{SP.value}\n'
        text += 'M=D\n'

        text += SP.increment()
        return text

    def pop(self, offset):
        text = f'@{SP.value - 1}\n'
        text += 'D=M\n'
        text += f'@{FILENAME}.{offset}\n'
        text += 'M=D\n'

        text += SP.decrement()
        return text


class PointerSegment:
    def __init__(self, this_segment, that_segment):
        self.name = 'pointer'
        self.base = 3 # Same as THIS
        self.this_segment = this_segment
        self.that_segment = that_segment
        self.labelcount = 0

    def push(self, offset):
        text = f'// push {self.name} {offset}\n'
        text += f'@{self.base + int(offset)}\n'
        text +=  'D=M\n'
        text += f'@{SP.value}\n'
        text +=  'M=D\n'
        text += SP.increment()
        return text

    def pop(self, offset):
        text = f'// pop {self.name} {offset}\n'
        text += f'@{SP.value - 1}\n'
        text += 'D=M\n'
        text += f'@{self.base + int(offset)}\n'
        text += 'M=D\n'
        text += SP.decrement()
        return text


# TODO: Not a fan of this way of doing it
this_segment = MemorySegment(3, 3000, 'this')
that_segment = MemorySegment(4, 3010, 'that')

_segment_dict = {
  'local': MemorySegment(1, 300, 'local'),
  'argument': MemorySegment(2, 400, 'argument'),
  'this': this_segment,
  'that': that_segment,
  'temp': TempSegment(),
  'static': StaticSegment(),
  'pointer': PointerSegment(this_segment, that_segment)
}


def push_constant(offset):
    comment = f'// push constant {offset}\n'
    text = comment + f'@{offset}\nD=A\n'
    text += f'@{SP.address}\nA=M\nM=D\n'
    return text + SP.increment()


def pushpop(f, segment, offset):
    if segment == 'constant':
        return push_constant(offset)
    segment = _segment_dict[segment]
    return getattr(segment, f)(offset)


_arithmetic_dict = {
    'add': Add(),
    'sub': Sub(),
    'neg': Neg(),
    'eq': BooleanVMCommand('eq', 'D;JNE'),
    'lt': BooleanVMCommand('lt', 'D-1;JLT'),
    'gt': BooleanVMCommand('gt', 'D+1;JGT'),
    'and': And(),
    'or': Or(),
    'not': Not()
}


class CodeWriter:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        set_filename(Path(filename).stem)

    def _write_arithmetic(self, command):
        f = _arithmetic_dict[command.arg0]
        self.file.write(f())

    def _write_push_pop(self, command):
        ctype, *args = command
        self.file.write(pushpop(ctype, *args))

    def _write_label(self, command):
        pass

    def _write_goto(self, command):
        pass

    def _write_if(self, command):
        pass

    def write_command(self, command):
        if command.type is CommandType.C_POP or command.type is CommandType.C_PUSH:
            f = self._write_push_pop
        elif command.type is CommandType.C_ARITHMETIC:
            f = self._write_arithmetic
        elif command.type.value == 'if-goto':
            f = self._write_if
        else:
            f = getattr(self, '_write_' + command.type.value)
        return f(command)

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


