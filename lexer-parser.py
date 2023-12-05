
import lex
from yacc import yacc

reserved = {
   'int' : 'INT',
   'float' : 'FLOAT',
   'char' : 'CHAR',
   'boolean' : 'BOOLEAN',
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   
   'return' : 'RETURN',
   'for' : 'FOR',
   'switch' : 'SWITCH',
   'case' : 'CASE',
   'default' : 'DEFAULT',
   'break' : 'BREAK',
   'continue' : 'CONTINUE',
   'struct' : 'STRUCT'
}

tokens = [
    'ID',
    'NUM_INT',
    'TEXTO',
    'NUM_DEC',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ATRIB',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'PERCENT',
    'AND',
    'OR',
    'COLON',
    'NOT',
    'GREATER',
    'LESS',
    
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
t_PERCENT = r'\%'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_COLON = r'\:'
t_NOT = r'\!'
t_GREATER = r'\>'
t_LESS = r'\<'

t_TEXTO = r'".*"' 
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/(?!\/)'
t_ATRIB = r'\='
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_DOT = r'\.'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'






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
if (x > 10){ 
    int casa = 15;
} else{
    char y = a;
}
'''


lexer.input(code_snippet)

for token in lexer:
    print(token)

# Yacc example

import yacc




# 1. Programa
def p_programa(p):
    'programa : dec_star'
    p[0] = p[1]





# 2. Declaração
def p_dec_star(p):
    '''dec_star :
               | dec_star dec'''
    if len(p) == 1:
        pass
    else:
        p[0] = p[1]

def p_dec_var(p): #declaracao variavel
    'dec : dvar'
    p[0] = p[1]

def p_dec_func(p): #declaracao funcao
    'dec : dfunc'
    p[0] = p[1]

def p_dec_estr(p):
    'dec : destr'




# 3. Declaração de Variável

def p_declaracao_variavel(p):
    '''dvar : tipo ID SEMICOLON
            | tipo ID ATRIB expr SEMICOLON'''
    p[0] = p[0]

def p_tipo_int(p):
    'tipo : INT'
    p[0] = p[1]

def p_tipo_float(p):
    'tipo : FLOAT'
    p[0] = p[1]

def p_tipo_char(p):
    'tipo : CHAR'
    p[0] = p[1]

def p_tipo_boolean(p):
    'tipo : BOOLEAN'
    p[0] = p[1]






# 4. Declaração de Função

def p_declaracao_func(p):
    'dfunc : tipo ID LPAREN parametros RPAREN bloco'
    p[0] = p[1]






# 5. Parâmetros de Função

def p_parametros_singular(p):
    'parametros : param'
    p[0] = p[1]

def p_parametros_multiplos(p):
    'parametros : param COMMA parametros'
    p[0] = p[1]
def p_param_tipo(p):
    'param : tipo ID'
    p[0] = p[1]

def p_param_tipo_lista(p):
    'param : tipo array'
    p[0] = p[1]

def p_param_tipo_elipse(p):
    'param : tipo DOT DOT DOT ID'
    p[0] = p[1]





# 6. Bloco

def p_bloco(p):
    'bloco : LBRACE dec RBRACE'
    p[0] = p[1]





# 7. Expressões

def p_expression_atrib(p):
    'expr : atrib %prec atrib'
    p[0] = p[1]

def p_atrib_expr(p):
    'atrib : ID ATRIB expr %prec atrib'
    p[0] = p[1]

def p_atrib_plus_expr(p):
    'atrib : ID PLUS ATRIB expr %prec atrib'
    p[0] = p[1] + p[2]

def p_atrib_minus_expr(p):
    'atrib : ID MINUS ATRIB expr %prec atrib'
    p[0] = p[1] - p[3]

def p_atrib_times_expr(p):
    'atrib : ID TIMES ATRIB expr %prec atrib'
    p[0] = p[1] * p[3]

def p_atrib_slash_expr(p):
    'atrib : ID DIVIDE ATRIB expr %prec atrib'
    p[0] = p[1] / p[3]

def p_atrib_percent_expr(p):
    'atrib : ID PERCENT ATRIB expr %prec atrib'
    p[0] = p[1]
def p_atrib_and_expr(p):
    'atrib : ID AND ATRIB expr %prec atrib'
    p[0] = p[1]

def p_atrib_id(p):
    'atrib : ID ATRIB ID %prec atrib'
    p[0] = p[1]

def p_atrib_plus_id(p):
    'atrib : ID PLUS ATRIB ID %prec atrib'
    p[0] = p[1] + p[2]

def p_atrib_minus_id(p):
    'atrib : ID MINUS ATRIB ID %prec atrib'
    p[0] = p[1] - p[3]

def p_atrib_times_id(p):
    'atrib : ID TIMES ATRIB ID %prec atrib'
    p[0] = p[1] * p[3]

def p_atrib_slash_id(p):
    'atrib : ID DIVIDE ATRIB ID %prec atrib'
    p[0] = p[1] / p[3]

def p_atrib_percent_id(p):
    'atrib : ID PERCENT ATRIB ID %prec atrib'
    p[0] = p[1]

def p_atrib_and_id(p):
    'atrib : ID AND ATRIB ID %prec atrib'
    p[0] = p[1]

def p_atrib_or_id(p):
    'atrib : ID OR ATRIB ID %prec atrib'
    p[0] = p[1]






#9 Estruturas de Controle

def p_control_if(p):
    'control : IF LPAREN expr RPAREN bloco'
    p[0] = p[1]

def p_control_else(p):
    'control : IF LPAREN expr RPAREN bloco ELSE bloco'
    p[0] = p[1]

def p_control_while(p):
    'control : WHILE LPAREN expr RPAREN bloco'
    p[0] = p[1]

def p_control_for(p):
    'control : FOR LPAREN expr SEMICOLON expr SEMICOLON RPAREN bloco'
    p[0] = p[1]

def p_control_switch(p):
    'control : SWITCH LPAREN expr RPAREN caselista'
    p[0] = p[1]

def p_caselista(p):
    'caselista : casedec_star'
    p[0] = p[1]

def p_casedec_star(p):
    '''casedec_star :
               | casedec_star casedec'''
    if len(p) == 1:
        pass
    else:
        p[0] = p[1]

def p_casedec_expr(p):
    'casedec : CASE expr COLON bloco'
    p[0] = p[1]

def p_casedec_default(p):
    'casedec : DEFAULT COLON bloco'
    p[0] = p[1]

def p_control_break(p):
    'control : BREAK SEMICOLON'
    p[0] = p[1]

def p_control_continue(p):
    'control : CONTINUE SEMICOLON'
    p[0] = p[1]

def p_control_return(p):
    'control : RETURN expr SEMICOLON'
    p[0] = p[1]




# 10. Declaração de Estruturas

def p_destr(p):
    'destr : STRUCT ID LBRACE dvar_star RBRACE SEMICOLON '
    p[0] = p[1]

def p_destr_control(p):
    'destr : control'
    p[0] = p[1]

def p_dvar_star(p):
    '''dvar_star :
                 | dvar_star dvar'''
    if len(p) == 1:
        pass
    else:
        p[0] = p[1]

# 11. Arrays

def p_array(p):
    'array : ID LBRACKET expr RBRACKET'
    p[0] = p[1]

def p_array_empty(p):
    'array : ID LBRACKET RBRACKET'
    p[0] = p[1]

#def p_array_init(p):
#    'array_init : LBRACE expr RBRACE'
#    p[0] = p[1]

# 12. Expressoes (2)

def p_expr_log(p):
    'expr : expr_log'
    p[0] = p[1]

def p_expr_rel(p):
    'expr_log : expr_rel'
    p[0] = p[1]

def p_expr_log_and(p):
    'expr_log : expr_log AND expr_rel'
    p[0] = p[1]

def p_expr_log_or(p):
    'expr_log : expr_log OR expr_rel'
    p[0] = p[1]

def p_expr_log_not(p):
    'expr_log : NOT expr_rel'
    p[0] = p[1]

def p_expr_rel_arithmetic(p):
    'expr_rel : expr_ar'
    p[0] = p[1]

def p_expr_rel_greater(p):
    'expr_rel : expr_ar GREATER expr_ar'
    p[0] = p[1]

def p_expr_rel_greater_or_equal(p):
    'expr_rel : expr_ar GREATER ATRIB expr_ar'
    p[0] = p[1]

def p_expr_rel_less(p):
    'expr_rel : expr_ar LESS expr_ar'
    p[0] = p[1]

def p_expr_rel_less_or_equal(p):
    'expr_rel : expr_ar LESS ATRIB expr_ar'
    p[0] = p[1]

def p_expr_rel_diff(p):
    'expr_rel : expr_ar NOT ATRIB expr_ar'
    p[0] = p[1]

def p_expr_rel_equals(p):
    'expr_rel : expr_ar ATRIB ATRIB expr_ar'
    p[0] = p[1]

def p_expr_ar_expr_mul(p):
    'expr_ar : expr_mul'
    p[0] = p[1]

def p_expr_ar_plus_expr_mul(p):
    'expr_ar : expr_ar PLUS expr_mul'
    p[0] = p[1] + p[3]

def p_expr_ar_minus_expr_mul(p):
    'expr_ar : expr_ar MINUS expr_mul'
    p[0] = p[1] - p[3]

def p_expr_mul_unary(p):
    'expr_mul : expr_un'
    p[0] = p[1]

def p_expr_mul_times_unary(p):
    'expr_mul : expr_mul TIMES expr_un'
    p[0] = p[1] * p[3]

def p_expr_mul_divide_unary(p):
    'expr_mul : expr_mul DIVIDE expr_un'
    p[0] = p[1] / p[3]

def p_expr_mul_rest_unary(p):
    'expr_mul : expr_mul PERCENT expr_un'
    p[0] = p[1]

def p_expr_un_postfix(p):
    'expr_un : expr_postfix'
    p[0] = p[1]

def p_expr_un_minus(p):
    'expr_un : MINUS expr_un %prec uminus'
    p[0] = - p[2]

def p_expr_un_sub(p):
    'expr_un : PLUS PLUS expr_postfix'
    p[0] = + + p[3]

'''def p_expr_un_add(p):
    'expr_un : MINUS MINUS expr_postfix'
    p[0] = - - p[3]'''

def p_postfix_primary(p):
    'expr_postfix : primary'
    p[0] = p[1]

def p_postfix_primary_expr(p):
    'expr_postfix : primary LBRACKET expr RBRACKET'
    p[0] = p[1]

def p_postfix_primary_args(p):
    'expr_postfix : primary LPAREN args RPAREN'
    p[0] = p[1]

def p_postfix_dot_id(p):
    'expr_postfix : primary DOT ID'
    p[0] = p[1]

def p_postfix_arrow(p):
    'expr_postfix : primary MINUS GREATER ID'
    p[0] = p[1] - p[3]

def p_args(p):
    'args : expr'
    p[0] = p[1]

def p_args_empty(p):
    'args : '
    pass

def p_primary_id(p):
    'primary : ID %prec primary'
    p[0] = p[1]

def p_primary_integer(p):
    'primary : NUM_INT %prec primary'
    p[0] = p[1]

def p_primary_decimal(p):
    'primary : NUM_DEC %prec primary'
    p[0] = p[1]

def p_primary_text(p):
    'primary : TEXTO %prec primary'
    p[0] = p[1]

def p_primary_expr(p):
    'primary : LPAREN expr RPAREN %prec primary'
    p[0] = p[1]


precedence = (

    ('left', 'primary'),
    ('left', 'atrib'),
    ('right', 'uminus')
)

# Error rule for syntax errors
def p_error(p):
    if p:
         print("Syntax error at token", p.type)
         # Just discard the token and tell the parser it's okay.
         parser.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()


result = parser.parse(code_snippet)

yacc.yacc(debug=True)

print(result)
