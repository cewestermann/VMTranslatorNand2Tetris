from .command import Command

class EOF: pass
end_of_file = EOF()


def _is_redundant(tokens):
    return not tokens or tokens[0].startswith('/')


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

    def close(self): self.file.close()


if __name__ == '__main__':
    parser = Parser('../StackArithmetic/SimpleAdd/SimpleAdd.vm')
    for _ in range(1000):
        print(parser.advance())
    
