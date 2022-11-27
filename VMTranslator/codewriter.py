from functools import wraps
from contextlib import contextmanager
from pathlib import Path

from .command import Command


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

def _clslabel(obj):
    return _clsvariable(obj).upper()



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
        text =  f'// if not {_clslabel}\n'
        text += f'@{SP.value - 2}\n'
        text +=  'M=0\n'
        return text

    def _true_branch(self):
        text = (
            f'// if {_clslabel}\n'
            f'@{SP.value - 2}\n'
             'M=-1\n' # Word of ones (true)
        )
        return text

    @staticmethod
    def _put_uncond_jump():
        return f'0;JMP\n'

    def _label_count(self):
        return f'{_clslabel}{self.labelcount}'

    def _put_label_reference(self):
        return f'@{self._label_count()}\n'

    def _put_label(self):
        return f'({self._label_count()})\n'

    def _put_end_label_reference(self):
        return f'@END_{self._label_count()}\n'

    def _put_end_label(self):
        return f'(END_{self._label_count()})\n'

    def _assemble_boolean(self, jump_cond):
        text = f'// {_clslabel}\n'
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
        

#def add(): 
#    comment = '// add\n'
#    s1 = f'@{SP.value - 1}\nD=M\n'
#    s2 = f'@{SP.value - 2}\nM=D+M\n'
#    s3 = SP.decrement()
#    return comment + s1 + s2 + s3

#def sub():
#    comment = '// sub\n'
#    s1 = f'@{SP.value - 1}\nD=M\n'
#    s2 = f'@{SP.value - 2}\nM=M-D\n'
#    s3 = SP.decrement()
#    return comment + s1 + s2 + s3

#def neg():
#    comment = '// neg\n'
#    s1 = f'@{SP.value - 1}\nM=-M'
#    return comment + s1


class Segment:
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


_segment_dict = {
  'local': Segment(1, 300, 'local'),
  'argument': Segment(2, 400, 'argument'),
  'this': Segment(3, 3000, 'this'),
  'that': Segment(4, 3010, 'that'), 
  'temp': TempSegment(),
  'static': StaticSegment()
}


class PointerSegment:
    def __init__(self):
        self.name = 'pointer'
        self._ref = {
            '0': _segment_dict['this'],
            '1': _segment_dict['that']
        }

    def push(self, offset):
        text = '// push {self.name} {offset}\n'
        return text + self._ref[offset].push(offset)
        
        #if offset:
        #    segment = _segment_dict['that']
        #else:
        #    segment = _segment_dict['this']




    def pop(self, offset): pass


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
        set_filename(Path(filename).stem)

    def _write_arithmetic(self, command):
        f = _arithmetic_dict[command.arg0]
        self.file.write(f())

    def _write_push_pop(self, command):
        ctype, *args = command
        self.file.write(pushpop(ctype, *args))

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


