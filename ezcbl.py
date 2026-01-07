import re
import sys

def compile_ezcbl(source:str):
    output:list[str] = []

    pattern = r'(\w+)\(([^)]+)\)'

    for match in re.finditer(pattern, source):
        func_name = match.group(1)
        args_str = match.group(2)
        args = [arg.strip() for arg in args_str.split(',')]

        #print(f"Function: {func_name}")
        #print(f"Arguments: {args_str}")
        #print(f"Arguments: {args}")

        output.append(f"    PERFORM CALL-{func_name}")
        output.append(f"")
        output.append(f"CALL-{func_name}.")

        for arg in args:
            output.append(f"    MOVE {arg}")
            output.append(f"      TO {arg} OF WS-PARAMS")
            output.append(f"")

        output.append(f"    CALL {func_name} USING WS-PARAMS")
        output.append(f"    .")
        output.append(f"")

    return '\n'.join(output)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        source = f.read()
    print(compile_ezcbl(source))