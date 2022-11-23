from collections import ChainMap
from enum import Enum

class CommandType(str, Enum):
    C_ARITHMETIC = 'arithmetic'
    C_PUSH = 'push'
    C_POP = 'pop'

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

_push_pop_dict = {'push': CommandType.C_PUSH,
                  'pop': CommandType.C_POP}

_arg0s = ChainMap(_arithmetics_dict, _push_pop_dict)


def _get_command_type(tokens):
    typearg, *rest = tokens
    return _arg0s.get(typearg, None)


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
        return self.tokens[0]

    @property
    def arg1(self):
        return self.tokens[1]

    @property
    def arg2(self):
        return self.tokens[2]
