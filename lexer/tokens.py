import re

T_KEYWORD = 'KEYWORD'
T_IDENTIFIER = 'IDENTIFIER'
T_NUMBER = 'NUMBER'
T_OPERATOR = 'OPERATOR'
T_PUNCTUATION = 'PUNCTUATION'
T_PARANTHESES = 'PARANTHESES'
T_NEWLINE = 'NEWLINE'
T_EOF = 'EOF'

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__ (self):
        
        if self.type == T_NEWLINE:
            return f"Token({self.type}, '\\n')"

        return f"Token({self.type}, '{self.value}')"
