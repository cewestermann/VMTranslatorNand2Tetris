import sys
from pathlib import Path

from parser import Parser
from codewriter import new_codewriter

def translate(vmfile): 
  name = Path(vmfile).stem
  parser = Parser(vmfile)
  with new_codewriter(f'{name}.asm') as cw:
    while parser.has_more_commands():
      command = parser.advance()
      cw.write_command(command)
    
    






if __name__ == '__main__':
  translate(sys.argv[1])
