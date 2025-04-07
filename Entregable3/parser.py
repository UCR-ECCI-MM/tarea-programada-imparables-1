import ply.yacc as yacc
# It is assumed that your lexer (shown in your code) defines all these tokens.
# For example, tokens = ('COMMENT', 'LBRACKET', 'RBRACKET', 'TIMESTAMP', 'LOGLEVEL',
# 'ENTRY_NUMBER', 'MESSAGE', 'BEGIN_DIAGNOSTIC', 'END_DIAGNOSTIC', 'CHECK', 'ARROW',
# 'LBRACE', 'RBRACE', 'SEMICOLON', 'BEGIN_BOOT_SEQUENCE', 'END_BOOT_SEQUENCE', 'STEP',
# 'BEGIN_CRASH_REPORT', 'END_CRASH_REPORT', 'STACK_TRACE', 'FUNCTION', 'LIINE',
# 'BEGIN_BACKUP', 'END_BACKUP', 'SOURCE', 'DESTINATION', 'FILE_LIST', 'BEGIN_BACKUP_UPDATE',
# 'END_BACKUP_UPDATE', 'TIMESTAMP', 'PROGRESS', 'DETAILS', 'NUMBER', 'STRING', 'COMMA',
# 'COLON', 'IDENTIFIER', 'MINUS')
from lexer import tokens  # adjust this import to match your project structure

# ---------------------
# Grammar Rules
# ---------------------

def p_log(p):
    "log : entries"
    p[0] = p[1]

def p_entries_multiple(p):
    "entries : entries entry"
    p[0] = p[1] + [p[2]]

def p_entries_single(p):
    "entries : entry"
    p[0] = [p[1]]

# An entry consists of a header and an optional block section.
def p_entry(p):
    "entry : LBRACKET TIMESTAMP RBRACKET LOGLEVEL ENTRY_NUMBER MESSAGE entry_optional"
    p[0] = {
        "timestamp": p[2],
        "loglevel": p[4],
        "entry_number": p[5],
        "message": p[6],
        "blocks": p[7]
    }

def p_entry_optional(p):
    '''entry_optional : blocks
                      | empty'''
    p[0] = p[1] if p[1] is not None else []

# A list of blocks
def p_blocks_multiple(p):
    "blocks : blocks block"
    p[0] = p[1] + [p[2]]

def p_blocks_single(p):
    "blocks : block"
    p[0] = [p[1]]

# A block can be one of several types:
def p_block_diagnostic(p):
    "block : BEGIN_DIAGNOSTIC diagnostic_list END_DIAGNOSTIC"
    p[0] = ("diagnostic", p[2])

def p_block_boot(p):
    "block : BEGIN_BOOT_SEQUENCE boot_steps END_BOOT_SEQUENCE"
    p[0] = ("boot_sequence", p[2])

def p_block_crash(p):
    "block : BEGIN_CRASH_REPORT crash_contents END_CRASH_REPORT"
    p[0] = ("crash_report", p[2])

def p_block_backup(p):
    "block : BEGIN_BACKUP backup_contents END_BACKUP"
    p[0] = ("backup", p[2])

# Diagnostic block rules
def p_diagnostic_list_multiple(p):
    "diagnostic_list : diagnostic_list diagnostic_entry"
    p[0] = p[1] + [p[2]]

def p_diagnostic_list_single(p):
    "diagnostic_list : diagnostic_entry"
    p[0] = [p[1]]

def p_diagnostic_entry(p):
    "diagnostic_entry : CHECK STRING ARROW LBRACE diagnostic_fields RBRACE SEMICOLON"
    # p[2] is the quoted string indicating what is being checked (e.g. "video")
    p[0] = {"check": p[2], "fields": p[5]}

def p_diagnostic_fields(p):
    '''diagnostic_fields : diagnostic_fields COMMA diagnostic_field
                         | diagnostic_field'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_diagnostic_field(p):
    '''diagnostic_field : RESULT STRING
                        | LATENCY STRING'''
    # Here we remove the colon from RESULT and LATENCY tokens if needed.
    field = "result" if p[1].startswith("result") else "latency"
    p[0] = (field, p[2])

# Boot sequence block rules
def p_boot_steps_multiple(p):
    "boot_steps : boot_steps boot_step"
    p[0] = p[1] + [p[2]]

def p_boot_steps_single(p):
    "boot_steps : boot_step"
    p[0] = [p[1]]

def p_boot_step(p):
    "boot_step : STEP STRING SEMICOLON"
    p[0] = p[2]

# Crash report block rules
def p_crash_contents(p):
    "crash_contents : crash_field_list"
    p[0] = p[1]

def p_crash_field_list_multiple(p):
    "crash_field_list : crash_field_list crash_field"
    p[0] = p[1] + [p[2]]

def p_crash_field_list_single(p):
    "crash_field_list : crash_field"
    p[0] = [p[1]]

def p_crash_field_error_code(p):
    "crash_field : IDENTIFIER COLON NUMBER SEMICOLON"
    # Assumes IDENTIFIER is 'ERROR_CODE'
    p[0] = ("error_code", p[3])

def p_crash_field_message(p):
    "crash_field : IDENTIFIER COLON STRING SEMICOLON"
    # Assumes IDENTIFIER is 'MESSAGE'
    p[0] = ("message", p[3])

def p_crash_field_stack_trace(p):
    "crash_field : STACK_TRACE COLON LBRACKET stack_trace_entries RBRACKET SEMICOLON"
    p[0] = ("stack_trace", p[4])

def p_stack_trace_entries_multiple(p):
    "stack_trace_entries : stack_trace_entries COMMA stack_trace_entry"
    p[0] = p[1] + [p[3]]

def p_stack_trace_entries_single(p):
    "stack_trace_entries : stack_trace_entry"
    p[0] = [p[1]]

def p_stack_trace_entry(p):
    "stack_trace_entry : LBRACE function_field COMMA line_field RBRACE"
    p[0] = {"function": p[2], "line": p[4]}

def p_function_field(p):
    "function_field : FUNCTION COLON STRING"
    p[0] = p[3]

def p_line_field(p):
    "line_field : LIINE COLON NUMBER"
    p[0] = p[3]

# Backup block rules
def p_backup_contents(p):
    "backup_contents : backup_field_list"
    # backup_field_list is a list of different backup-related fields.
    p[0] = dict(p[1])

def p_backup_field_list_multiple(p):
    "backup_field_list : backup_field_list backup_field"
    p[0] = p[1] + [p[2]]

def p_backup_field_list_single(p):
    "backup_field_list : backup_field"
    p[0] = [p[1]]

def p_backup_field_source(p):
    "backup_field : SOURCE STRING SEMICOLON"
    p[0] = ("source", p[2])

def p_backup_field_destination(p):
    "backup_field : DESTINATION COLON STRING SEMICOLON"
    p[0] = ("destination", p[3])

def p_backup_field_file_list(p):
    "backup_field : FILE_LIST COLON LBRACKET file_list_entries RBRACKET SEMICOLON"
    p[0] = ("file_list", p[4])

def p_file_list_entries_multiple(p):
    "file_list_entries : file_list_entries COMMA STRING"
    p[0] = p[1] + [p[3]]

def p_file_list_entries_single(p):
    "file_list_entries : STRING"
    p[0] = [p[1]]

def p_backup_field_backup_update(p):
    "backup_field : BEGIN_BACKUP_UPDATE backup_update_contents END_BACKUP_UPDATE"
    p[0] = ("backup_update", p[2])

def p_backup_update_contents(p):
    "backup_update_contents : backup_update_field_list"
    p[0] = dict(p[1])

def p_backup_update_field_list_multiple(p):
    "backup_update_field_list : backup_update_field_list backup_update_field"
    p[0] = p[1] + [p[2]]

def p_backup_update_field_list_single(p):
    "backup_update_field_list : backup_update_field"
    p[0] = [p[1]]

def p_backup_update_field_timestamp(p):
    "backup_update_field : TIMESTAMP COLON STRING SEMICOLON"
    p[0] = ("timestamp", p[3])

def p_backup_update_field_progress(p):
    "backup_update_field : PROGRESS COLON NUMBER SEMICOLON"
    p[0] = ("progress", p[3])

def p_backup_update_field_details(p):
    "backup_update_field : DETAILS COLON STRING SEMICOLON"
    p[0] = ("details", p[3])

# Empty rule for optional parts
def p_empty(p):
    "empty :"
    p[0] = None

def p_error(p):
    if p:
        print("Syntax error at token", p.type, "value", p.value)
    else:
        print("Syntax error at EOF")

# ---------------------
# Build the parser
# ---------------------
parser = yacc.yacc()

# ---------------------
# Example usage:
# ---------------------
if __name__ == '__main__':
    # Read log file data (adjust the path if necessary)
    try:
        with open('Docs/large_complex_log.txt', 'r') as file:
            data = file.read()
            result = parser.parse(data)
        # For demonstration, simply print the parse tree (or parts of it)
        from pprint import pprint
        pprint(result)
    except FileNotFoundError:
        print("Log file not found")
