import ply.lex as lex
# Illegal character
tokens = (
    #'COMMENT',
    'LBRACKET', 
    'RBRACKET', 
    'DATE',
    'TIME',
    'LOGLEVEL',
    'ENTRY_NUMBER',
    'STRING',
    'BEGIN_DIAGNOSTIC', 
    'END_DIAGNOSTIC', 
    'VIDEO',
    'STORAGE',
    'NETWORK',
    'AUDIO',
    'RESULT',
    'PASS',
    'FAIL',
    'LATENCY',
    'SEMICOLON',
    'CHECK',
    'BEGIN_BOOT_SEQUENCE', 
    'END_BOOT_SEQUENCE',
    'STEP',
    'COLON', 
    'ENTRY_MESSAGE',
    'MESSAGE',
    'TIMESTAMP', 
    'ARROW', 
    'LBRACE', 
    'RBRACE', 
    'BEGIN_CRASH_REPORT', 
    'END_CRASH_REPORT', 
    'COMMA', 
    'NUMBER', 
    'IDENTIFIER',
    'MINUS',
    'BEGIN_BACKUP',
    'END_BACKUP',
    'SOURCE',
    'DESTINATION',
    'FILE_LIST',
    'BEGIN_BACKUP_UPDATE',
    'END_BACKUP_UPDATE',
    'ERROR_CODE',
    'PROGRESS',
    'DETAILS',
    'STACK_TRACE',
    'FUNCTION',
    'LINE',
)

t_ignore_COMMENT = r'\#.*'

#Regular expressions for tokens
# def t_COMMENT(t):
#     r'\#.*'
#     return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t


def t_DATE(t): 
    r'\d{4}-\d{2}-\d{2}'
    return t

def t_TIME(t): 
    r'\d{2}:\d{2}:\d{2}'
    return t

def t_LOGLEVEL(t):
    r'(INFO|WARN|DEBUG|ERROR):'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_ENTRY_NUMBER(t):
    r'\s*Entry\s*\d+:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_BEGIN_DIAGNOSTIC(t):
    r'BEGIN_DIAGNOSTIC'
    return t

def t_END_DIAGNOSTIC(t):
    r'END_DIAGNOSTIC'
    return t

def t_CHECK(t):
    r'CHECK:'
    return t

def t_ARROW(t):
    r'->'
    return t

def t_RESULT(t):
    r'result:'
    return t

def t_LATENCY(t):
    r'latency:'
    return t

def t_VIDEO(t):
    r'video'
    return t

def t_AUDIO(t):
    r'audio'
    return t

def t_STORAGE(t):
    r'storage'
    return t

def t_NETWORK(t):
    r'newwork'
    return t

def t_PASS(t):
    r'PASS'
    return t

def t_FAIL(t):
    r'FAIL'
    return t

def t_TIMESTAMP(t):
    r'TIMESTAMP:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_STEP(t):
    r'STEP:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_SOURCE(t):
    r'SOURCE:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    # t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_DESTINATION(t):
    r'DESTINATION:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_FUNCTION(t):
    r'FUNCTION:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_LINE(t):
    r'LINE:\s*\d+'
    return t

def t_ERROR_CODE(t):
    r'ERROR_CODE:\s*\d+'
    return t

def t_PROGRESS(t):
    r'PROGRESS:'
    return t

def t_DETAILS(t):
    r'DETAILS:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_STACK_TRACE(t):
    r'STACK_TRACE:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_MESSAGE(t):
    r'MESSAGE:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_FILE_LIST(t):
    r'FILE_LIST:'
    t.value = t.value[:-1]  # Remove the colon (OJO)
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_INSIDEBRACE(t):
    r'\{[^}]*\}'
    return t

def t_ENTRY_MESSAGE(t):
    r'[a-zA-Z][a-zA-Z0-9\s]*\.'
    return t

def t_BEGIN_CRASH_REPORT(t):
    r'BEGIN_CRASH_REPORT'
    return t

def t_END_CRASH_REPORT(t):
    r'END_CRASH_REPORT'
    return t

def t_BEGIN_BOOT_SEQUENCE(t):
    r'BEGIN_BOOT_SEQUENCE'
    return t

def t_END_BOOT_SEQUENCE(t):
    r'END_BOOT_SEQUENCE'
    return t

def t_COMMA(t):
    r','
    return t

def t_BEGIN_BACKUP_UPDATE(t):
    r'BEGIN_BACKUP_UPDATE'
    return t

def t_END_BACKUP_UPDATE(t):
    r'END_BACKUP_UPDATE'
    return t

def t_BEGIN_BACKUP(t):
    r'BEGIN_BACKUP'
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_MINUS(t): 
    r'-' 
    return t

def t_END_BACKUP(t):
    r'END_BACKUP'
    return t

def t_COLON(t):
    r':'
    return t


# Ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_SEMICOLON(t):
    r';'
    return t

# def t_COLON(t):
#     r':'
#     return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Build the lexer
lexer = lex.lex()


try:
    # Clear the output file before starting
    # with open('lexer_output.txt', 'w') as f:
    #     f.write("ANÁLISIS LÉXICO\n")
    #     f.write("=" * 50 + "\n\n")
    
    with open('Docs/large_complex_log.txt', 'r') as file:
        data = file.read()
        lexer.input(data)
        # for tok in lexer:
        #     with open('lexer_output.txt', 'a') as f:
        #         f.write(f"Token: {tok.type:<20} | Valor: {tok.value}\n")
        print("Análisis léxico completado. Resultados guardados en 'lexer_output.txt'")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)