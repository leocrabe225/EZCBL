import re
import sys

def compile_ezcbl(source:str):
    output = ['Hello, COBOL!']

    pattern = r'(\w+)\(([^)]+)\)'
    match = re.search(pattern, source)

    if match:
        func_name = match.group(1)
        args = match.group(2)

        print(f"Function: {func_name}")
        print(f"Arguments: {args}")

    return '\n'.join(output)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        source = f.read()
    print(compile_ezcbl(source))