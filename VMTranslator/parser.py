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

_push_dict = {'push': CommandType.C_PUSH}

_arg0s = ChainMap(_arithmetics_dict, _push_dict)

class EOF: pass
end_of_file = EOF()

def _get_command_type(tokens):
    typearg, *rest = tokens
    return _arg0s.get(typearg, None)

def _is_redundant(tokens):
    return not tokens or tokens[0].startswith('/')

class Command:
    def __init__(self, tokens):
        self.tokens = tokens
        self.type = _get_command_type(self.tokens)

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, i):
        return self.tokens[i]

    def __repr__(self):
        return f'Command({self.type}, {self.tokens!r})\n'

    @property
    def arg0(self):
        return self.line[0]

class Parser:
    def __init__(self, file):
        self.file = open(file, 'rt')
        self.current_command = None

    def __next__(self):
        line = next(self.file, end_of_file)
        if line is end_of_file:
            return False
        tokens = line.split()
        if _is_redundant(tokens):
            return next(self)
        return tokens

    def has_more_commands(self):
        if self.current_command is None:
            tokens = next(self)
            if not tokens:
                return False
            self.current_command = Command(tokens)
            return True

    def advance(self):
        if self.has_more_commands():
            command = self.current_command
            self.current_command = None # Consume
            return command
        else:
            raise StopIteration

    def command_type(self): return self.command.type

    def arg1(self): return self.current_command[1]

    def arg2(self): return self.current_command[2]

    def close(self): self.file.close()


if __name__ == '__main__':
    parser = Parser('../StackArithmetic/SimpleAdd/SimpleAdd.vm')
    for _ in range(1000):
        print(parser.advance())
    
