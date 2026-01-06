import re
import sys

def compile_ezcbl(source):
    output = ['Hello, COBOL!']

    return '\n'.join(output)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        source = f.read()
    print(compile_ezcbl(source))