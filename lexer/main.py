import os
from lexer import Lexer

def run():

    file_path = "tests/test1.hl"

    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
        return

    with open(file_path, 'r') as file:
        source_code = file.read()

    print(f"--- Compiling {file_path} ---\n")

    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    print("--- Tokens Generated ---")
    for tok in tokens:
        print(tok)

if __name__ == "__main__":
    run()