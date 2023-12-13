# lexer.py
import ply.lex as lex

tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Token tidak valid: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# parser.py
# parser.py
import ply.yacc as yacc

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term(p):
    'term : NUMBER'
    p[0] = int(p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# main.py
with open(input("Masukkan nama file: "), 'r') as file:
    input_text = file.read()

lexer.input(input_text)
while True:
    token = lexer.token()
    if not token:
        break
    print(token)

result = parser.parse(input_text)
print("Hasil kompilasi:", result)
