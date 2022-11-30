from collections import ChainMap
from enum import Enum

class CommandType(str, Enum):
    C_ARITHMETIC = 'arithmetic'
    C_PUSH = 'push'
    C_POP = 'pop'
    C_LABEL = 'label'
    C_GOTO = 'goto'
    C_IF = 'if-goto'
    C_FUNCTION = 'function'
    C_RETURN = 'return'
    C_CALL = 'call'


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

# TODO: This does not sit well with me, but it'll do for now
# since I don't have quick ways to test larger changers.
_push_pop_dict = {'push': CommandType.C_PUSH,
                  'pop': CommandType.C_POP,
                  'label': CommandType.C_LABEL,
                  'goto': CommandType.C_GOTO,
                  'if-goto': CommandType.C_IF,
                  'function': CommandType.C_FUNCTION,
                  'return': CommandType.C_RETURN,
                  'call': CommandType.C_CALL}

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
