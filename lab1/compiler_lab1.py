import re

def generate_tokens(filename="file.txt"):
    token_specifications = [
        ('KEYWORD',    r'\b(int|if|return|float|else|while)\b'),
        ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
        ('INTEGER',    r'\b\d+\b'),
        ('OPERATOR',   r'==|=|\+|-|\*|/'),  
        ('DELIMITERS', r';'),
        ('SEPARATOR',  r'[\(\)\{\},]'),
    ]
    
    master_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specifications)
    
    try:
        with open(filename, 'r') as file:
            source_code = file.read()
            
        for match in re.finditer(master_regex, source_code):
            for token_type, _ in token_specifications:
                token_value = match.group(token_type)
                if token_value:
                    print(f"('{token_type}', '{token_value}')")
                    break
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    generate_tokens('file.txt')