from collections import ChainMap
from typing import NamedTuple
from enum import Enum, auto

class CommandType(Enum):
    C_ARITHMETIC = auto()
    C_PUSH = auto()

class EOF:
    type = 'EOF'

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

_arithmetics_dict = {arith: CommandType.C_ARITHMETIC for arith in _arithmetics}

_push = ('push',)

_push_dict = {'push': CommandType.C_PUSH}

_arg0s = ChainMap(_arithmetics_dict, _push_dict)

def _get_command_type(arg0):
    return _arg0s.get(arg0, None)

class Command:
    def __init__(self, line):
        self.type = _get_command_type(line)






class Parser:
    def __init__(self, file):
        self.file = open(file, 'rt')
        self.current_command = None

    def _peek(self, *cmdtypes):
        if self.current_command is None:
            self.current_command = next(self.file, EOF)
        if self.current_command.type in cmdtypes:
            return self.current_command
        else:
            return None

    def advance(self, *cmdtypes):
        command = self._peek(*cmdtypes)
        if command:
            self.current_command = None # Consume
        return command

    def command_type(self, command):
        pass

    def arg1(self):
        pass

    def arg2(self):
        pass


if __name__ == '__main__':
    parser = Parser('../StackArithmetic/SimpleAdd/SimpleAdd.vm')
