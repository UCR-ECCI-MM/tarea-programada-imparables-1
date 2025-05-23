import ply.lex as lex

tokens = (
    'COMMENT', 
    'LBRACKET', 
    'RBRACKET', 
    'COLON', 
    'MESSAGE', 
    'BEGIN_DIAGNOSTIC', 
    'END_DIAGNOSTIC', 
    'CHECK',
    'TIMESTAMP', 
    'LOGLEVEL', 
    'ENTRY',
    'ARROW', 
    'LBRACE', 
    'RBRACE', 
    'RESULT', 
    'LATENCY',
    'STRING',
    'SEMICOLON',
    'BEGIN_CRASH_REPORT', 
    'END_CRASH_REPORT', 
    'BEGIN_BOOT_SEQUENCE', 
    'END_BOOT_SEQUENCE',
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
    'PROGRESS',
    'DETAILS',
    'RESULT',
    'LATENCY',
    'VIDEO',
    'AUDIO',
    'STORAGE',
    'NETWORK',
    'PASS',
    'FAIL',
    'STEP',
    'STACK_TRACE',
    'FUNCTION',
    'LIINE',
)

# Regular expressions for tokens
def t_COMMENT(t):
    r'\#.*'
    return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

def t_TIMESTAMP(t):
    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    return t

def t_LOGLEVEL(t):
    r'(INFO|WARN|DEBUG|ERROR):'
    t.value = t.value[:-1]  # Remove the colon
    return t

def t_ENTRY(t):
    r'Entry \d{3}'
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

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

def t_INSIDEBRACE(t):
    r'\{[^}]*\}'
    return t

def t_RESULT(t):
    r'result:'
    return t

def t_LATENCY(t):
    r'latency:'
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_COLON(t):
    r':'
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_MESSAGE(t):
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

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_MINUS(t): 
    r'-' 
    return t

def t_BEGIN_BACKUP(t):
    r'BEGIN_BACKUP'
    return t

def t_END_BACKUP(t):
    r'END_BACKUP'
    return t

def t_BEGIN_BACKUP_UPDATE(t):
    r'BEGIN_BACKUP_UPDATE'
    return t

def t_END_BACKUP_UPDATE(t):
    r'END_BACKUP_UPDATE'
    return t

def t_SOURCE(t):
    r'SOURCE'
    return t

def t_DESTINATION(t):
    r'DESTINATION'
    return t

def t_FILE_LIST(t):
    r'FILE_LIST'
    return t

def t_PROGRESS(t):
    r'PROGRESS'
    return t

def t_DETAILS(t):
    r'DETAILS'
    return t

def t_VIDEO(t):
    r'VIDEO'
    return t

def t_AUDIO(t):
    r'AUDIO'
    return t

def t_STORAGE(t):
    r'STORAGE'
    return t

def t_NETWORK(t):
    r'NETWORK'
    return t

def t_PASS(t):
    r'PASS'
    return t

def t_FAIL(t):
    r'FAIL'
    return t

def t_STEP(t):
    r'STEP'
    return t

def t_STACK_TRACE(t):
    r'STACK_TRACE'
    return t

def t_FUNCTION(t):
    r'FUNCTION'
    return t

def t_LINE(t):
    r'LINE'
    return t


# Ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


try:
    with open('Docs/large_complex_log.txt', 'r') as file:
        data = file.read()
        lexer.input(data)
        for tok in lexer:
            print(tok.value)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
    