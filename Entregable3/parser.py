import ply.yacc as yacc
from Entregable2.lexer import tokens

# Regla inicial: el documento se compone de una lista de entradas
def p_S(p):
    "S : entries"
    p[0] = p[1]

def p_entries_multiple(p):
    "entries : entry entries"
    p[0] = [p[1]] + p[2]

def p_entries_single(p):
    "entries : entry"
    p[0] = [p[1]]

# Una entrada puede ser una línea de comentario o una línea de log (con o sin bloques)
def p_entry_comment(p):
    "entry : COMMENT"
    p[0] = ('comment', p[1])

def p_entry_log(p):
    "entry : log_line blocks_opt"
    p[0] = ('log', p[1], p[2])

# Regla para la línea de log:
def p_log_line(p):
    "log_line : LBRACKET TIMESTAMP RBRACKET LOGLEVEL COLON ENTRY NUMBER COLON MESSAGE"
    p[0] = {
        'timestamp': p[2],
        'loglevel': p[4],
        'entry': p[6],
        'number': p[7],
        'message': p[9]
    }

# Bloques opcionales que pueden acompañar la línea de log
def p_blocks_opt(p):
    "blocks_opt : blocks"
    p[0] = p[1]

def p_blocks_opt_empty(p):
    "blocks_opt : "
    p[0] = []

def p_blocks(p):
    "blocks : block blocks"
    p[0] = [p[1]] + p[2]

def p_blocks_single(p):
    "blocks : block"
    p[0] = [p[1]]

# Un bloque puede ser de diagnóstico, boot, crash o backup
def p_block(p):
    """block : diagnostic_block
             | boot_block
             | crash_block
             | backup_block"""
    p[0] = p[1]

# Bloque de diagnóstico
def p_diagnostic_block(p):
    "diagnostic_block : BEGIN_DIAGNOSTIC check_list END_DIAGNOSTIC"
    p[0] = ('diagnostic', p[2])

def p_check_list_multiple(p):
    "check_list : check_line check_list"
    p[0] = [p[1]] + p[2]

def p_check_list_single(p):
    "check_list : check_line"
    p[0] = [p[1]]

def p_check_line(p):
    "check_line : CHECK COLON STRING ARROW LBRACE RESULT COLON result_value COMMA LATENCY COLON STRING RBRACE SEMICOLON"
    p[0] = {
        'check': p[3],
        'result': p[8],
        'latency': p[12]
    }

def p_result_value_pass(p):
    "result_value : PASS"
    p[0] = 'PASS'

def p_result_value_fail(p):
    "result_value : FAIL"
    p[0] = 'FAIL'

def p_result_value_string(p):
    "result_value : STRING"
    p[0] = p[1]

# Bloque de secuencia de arranque (boot)
def p_boot_block(p):
    "boot_block : BEGIN_BOOT_SEQUENCE step_list END_BOOT_SEQUENCE"
    p[0] = ('boot', p[2])

def p_step_list_multiple(p):
    "step_list : step_line step_list"
    p[0] = [p[1]] + p[2]

def p_step_list_single(p):
    "step_list : step_line"
    p[0] = [p[1]]

def p_step_line(p):
    "step_line : STEP COLON STRING SEMICOLON"
    p[0] = p[3]

# Bloque de reporte de crash
def p_crash_block(p):
    "crash_block : BEGIN_CRASH_REPORT crash_content END_CRASH_REPORT"
    p[0] = ('crash', p[2])

def p_crash_content(p):
    "crash_content : error_code_line message_line stack_trace_line"
    p[0] = {
        'error_code': p[1],
        'message': p[2],
        'stack_trace': p[3]
    }

def p_error_code_line(p):
    "error_code_line : IDENTIFIER COLON NUMBER SEMICOLON"
    p[0] = p[3]

def p_message_line(p):
    "message_line : IDENTIFIER COLON STRING SEMICOLON"
    p[0] = p[3]

def p_stack_trace_line(p):
    "stack_trace_line : STACK_TRACE COLON LBRACKET stack_items RBRACKET SEMICOLON"
    p[0] = p[4]

def p_stack_items_multiple(p):
    "stack_items : stack_item COMMA stack_items"
    p[0] = [p[1]] + p[3]

def p_stack_items_single(p):
    "stack_items : stack_item"
    p[0] = [p[1]]

def p_stack_item(p):
    "stack_item : LBRACE function_line COMMA line_line RBRACE"
    p[0] = {
        'function': p[2],
        'line': p[4]
    }

def p_function_line(p):
    "function_line : FUNCTION COLON STRING"
    p[0] = p[3]

def p_line_line(p):
    "line_line : LINE COLON NUMBER"
    p[0] = p[3]

# Bloque de backup
def p_backup_block(p):
    "backup_block : BEGIN_BACKUP backup_content END_BACKUP"
    p[0] = ('backup', p[2])

def p_backup_content(p):
    "backup_content : source_line destination_line file_list_line backup_update_list_opt"
    p[0] = {
        'source': p[1],
        'destination': p[2],
        'file_list': p[3],
        'updates': p[4]
    }

def p_source_line(p):
    "source_line : SOURCE COLON STRING SEMICOLON"
    p[0] = p[3]

def p_destination_line(p):
    "destination_line : DESTINATION COLON STRING SEMICOLON"
    p[0] = p[3]

def p_file_list_line(p):
    "file_list_line : FILE_LIST COLON LBRACKET file_entries RBRACKET SEMICOLON"
    p[0] = p[4]

def p_file_entries_multiple(p):
    "file_entries : STRING COMMA file_entries"
    p[0] = [p[1]] + p[3]

def p_file_entries_single(p):
    "file_entries : STRING"
    p[0] = [p[1]]

def p_backup_update_list_opt(p):
    "backup_update_list_opt : backup_update_list"
    p[0] = p[1]

def p_backup_update_list_opt_empty(p):
    "backup_update_list_opt : "
    p[0] = []

def p_backup_update_list_multiple(p):
    "backup_update_list : backup_update_block backup_update_list"
    p[0] = [p[1]] + p[2]

def p_backup_update_list_single(p):
    "backup_update_list : backup_update_block"
    p[0] = [p[1]]

def p_backup_update_block(p):
    "backup_update_block : BEGIN_BACKUP_UPDATE backup_update_content END_BACKUP_UPDATE"
    p[0] = p[2]

def p_backup_update_content(p):
    "backup_update_content : timestamp_line progress_line details_line"
    p[0] = {
        'timestamp': p[1],
        'progress': p[2],
        'details': p[3]
    }

def p_timestamp_line(p):
    "timestamp_line : TIMESTAMP COLON STRING SEMICOLON"
    p[0] = p[3]

def p_progress_line(p):
    "progress_line : PROGRESS COLON NUMBER SEMICOLON"
    p[0] = p[3]

def p_details_line(p):
    "details_line : DETAILS COLON STRING SEMICOLON"
    p[0] = p[3]

# Manejo de errores de sintaxis
def p_error(p):
    if p:
        print("Syntax error at token", p.type, "value", p.value)
    else:
        print("Syntax error at EOF")

# Construye el parser
parser = yacc.yacc()

if __name__ == '__main__':
    try:
        with open('Docs/large_complex_log.txt', 'r') as file:
            data = file.read()
            result = parser.parse(data)
            print(result)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(e)
