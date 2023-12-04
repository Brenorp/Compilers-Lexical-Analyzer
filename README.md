# Compilers-Lexical-Analyzer
A simple Lexical Analyzer for my Compilers course

It was built using PLY, a python implementation of the lex parsing tool.
lex.py is taken from https://github.com/dabeaz/ply repository, as it doesn't support pip package. It is untouched from the original and downloaded on October 2nd, 2023.

## First Assignment

In this assignment, we were tasked to build a lexical analyzer that reads the following tokens:

'NUM_INT' - A sequence of digits like "123".

'NUM_DEC' - A sequence of digits with a decimal part, like "123.456"

'ID' - Identifiers. Sequences that begin with a letter or underscore, followed by letters, digits or underscore. 

'TEXTO' - Sequences of characters between double quotation marks.

'OPERADOR' - Operator symbols, that represent operations, like "=", "+", "-", "*", "/", "%", "&&", "||", "!" as well as comparison operators like ">", ">=", "<", "<=", "!=", "==".

'SPECIAL' - Special symbols with special meanings, like "(", ")", "[", "]", "{", "}", ",", ";".

Reserved Words - words specific to the language, their token is their own wording. the following are this particular language reserverd words: "int", "float", "char", "boolean", "void", "if", "else", "for", "while", "scanf", "println", "main" and "return".

Commentary - Sequences that begin with "//" and contain all characters until the end of line. These are to be ignored by the lexer.

This assignment is in the file 'lexer.py' and uses 'lex.py'

## Second Assignment

In this assignment, we were tasked to build a parser that reads tokens from the lexer using the base grammar found in the assignment notes. We're expected to resolve conflicts and raise syntax errors that may appear in the input.
