
import lex

reserved = {
   'int' : 'INT',
   'float' : 'FLOAT',
   'char' : 'CHAR',
   'boolean' : 'BOOLEAN',
   'void' : 'VOID',
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'scanf' : 'SCANF',
   'println' : 'PRINTLN',
   'main' : 'MAIN',
   'return' : 'RETURN'
}

tokens = [
    'ID',
    'NUM_INT',
    'OPERADOR',
    'TEXTO',
    'SPECIAL',
    'NUM_DEC'
 ] + list(reserved.values())

t_ignore  = ' \t'
t_ignore_COMMENT = '//.*'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Regular expressions for tokens
t_NUM_INT = r'\d+'
t_NUM_DEC = r'\d+\.\d+'
t_OPERADOR = r'\=|\+|\-|\*|\/(?!\/)|\%|\&\&|\=|\|\||\!|\>|\>\=|\<|\<\=|\!\=|\=\='
t_SPECIAL = r'\(|\)|\{|\}|\;|\,|\.|\[|\]'
t_TEXTO = r'".*"' 




# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Example usage
code_snippet = '''
int main() {
    int num1 = 123/2;
    float num2 = 45.67;
    char letra = 'A';
    if (num1 == 100) {
        println("Número maior que 100");
        //comentario de uma linha
    }
    return 0;
}
'''


lexer.input(code_snippet)

for token in lexer:
    print(token)