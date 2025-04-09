
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW AUDIO BEGIN_BACKUP BEGIN_BACKUP_UPDATE BEGIN_BOOT_SEQUENCE BEGIN_CRASH_REPORT BEGIN_DIAGNOSTIC CHECK COLON COMMA DATE DESTINATION DETAILS END_BACKUP END_BACKUP_UPDATE END_BOOT_SEQUENCE END_CRASH_REPORT END_DIAGNOSTIC ENTRY_MESSAGE ENTRY_NUMBER ERROR_CODE FAIL FILE_LIST FUNCTION IDENTIFIER LATENCY LBRACE LBRACKET LINE LOGLEVEL MESSAGE MINUS NETWORK NUMBER PASS PROGRESS RBRACE RBRACKET RESULT SEMICOLON SOURCE STACK_TRACE STEP STORAGE STRING TIME TIMESTAMP VIDEOS : entriesentries : entry entriesentries : entryentry : log_line blocks_optlog_line : LBRACKET DATE TIME RBRACKET LOGLEVEL ENTRY_NUMBER ENTRY_MESSAGEblocks_opt : blocksblocks_opt : blocks : block blocksblocks : blockblock : diagnostic_block \n| boot_block \n| crash_block \n| backup_blockdiagnostic_block : BEGIN_DIAGNOSTIC check_list END_DIAGNOSTICcheck_list : check_line check_listcheck_list : check_linecheck_line : CHECK STRING ARROW LBRACE RESULT result_value COMMA LATENCY STRING RBRACE SEMICOLONCHECK_STRING : VIDEO \n| AUDIO\n| NETWORK\n| STORAGEresult_value : PASSresult_value : FAILresult_value : STRINGboot_block : BEGIN_BOOT_SEQUENCE step_list END_BOOT_SEQUENCEstep_list : step_line step_liststep_list : step_linestep_line : STEP STRING SEMICOLONcrash_block : BEGIN_CRASH_REPORT crash_content END_CRASH_REPORTcrash_content : error_code_line message_line stack_trace_lineerror_code_line : IDENTIFIER COLON NUMBER SEMICOLONmessage_line : IDENTIFIER COLON STRING SEMICOLONstack_trace_line : STACK_TRACE COLON LBRACKET stack_items RBRACKET SEMICOLONstack_items : stack_item COMMA stack_itemsstack_items : stack_itemstack_item : LBRACE function_line COMMA line_line RBRACEfunction_line : FUNCTION COLON STRINGline_line : LINE COLON NUMBERbackup_block : BEGIN_BACKUP backup_content END_BACKUPbackup_content : source_line destination_line file_list_line backup_update_list_optsource_line : SOURCE STRING SEMICOLONdestination_line : DESTINATION STRING SEMICOLONfile_list_line : FILE_LIST LBRACKET file_entries RBRACKET SEMICOLONfile_entries : STRING COMMA file_entriesfile_entries : STRING COMMAbackup_update_list_opt : backup_update_listbackup_update_list_opt : backup_update_list : backup_update_block backup_update_listbackup_update_list : backup_update_blockbackup_update_block : BEGIN_BACKUP_UPDATE backup_update_content END_BACKUP_UPDATEbackup_update_content : timestamp_line progress_line details_linetimestamp_line : TIMESTAMP STRING SEMICOLONprogress_line : PROGRESS NUMBER SEMICOLONdetails_line : DETAILS STRING SEMICOLON'
    
_lr_action_items = {'LBRACKET':([0,3,4,7,8,9,10,11,12,13,19,33,36,39,43,55,60,79,],[5,5,-7,-4,-6,-9,-10,-11,-12,-13,-8,-14,-25,-29,-39,67,71,-5,]),'$end':([1,2,3,4,6,7,8,9,10,11,12,13,19,33,36,39,43,79,],[0,-1,-3,-7,-2,-4,-6,-9,-10,-11,-12,-13,-8,-14,-25,-29,-39,-5,]),'BEGIN_DIAGNOSTIC':([4,9,10,11,12,13,33,36,39,43,79,],[14,14,-10,-11,-12,-13,-14,-25,-29,-39,-5,]),'BEGIN_BOOT_SEQUENCE':([4,9,10,11,12,13,33,36,39,43,79,],[15,15,-10,-11,-12,-13,-14,-25,-29,-39,-5,]),'BEGIN_CRASH_REPORT':([4,9,10,11,12,13,33,36,39,43,79,],[16,16,-10,-11,-12,-13,-14,-25,-29,-39,-5,]),'BEGIN_BACKUP':([4,9,10,11,12,13,33,36,39,43,79,],[17,17,-10,-11,-12,-13,-14,-25,-29,-39,-5,]),'DATE':([5,],[18,]),'CHECK':([14,21,119,],[22,22,-17,]),'STEP':([15,24,49,],[25,25,-28,]),'IDENTIFIER':([16,27,62,],[28,41,-31,]),'SOURCE':([17,],[31,]),'TIME':([18,],[32,]),'END_DIAGNOSTIC':([20,21,34,119,],[33,-16,-15,-17,]),'STRING':([22,25,31,45,52,67,70,76,92,99,104,108,],[35,38,46,56,61,78,80,90,78,109,111,114,]),'END_BOOT_SEQUENCE':([23,24,37,49,],[36,-27,-26,-28,]),'END_CRASH_REPORT':([26,50,105,],[39,-30,-33,]),'COLON':([28,41,51,97,113,],[42,52,60,108,118,]),'END_BACKUP':([29,54,63,64,65,73,87,102,],[43,-47,-40,-46,-49,-48,-50,-43,]),'DESTINATION':([30,57,],[45,-41,]),'RBRACKET':([32,77,84,85,92,103,106,117,],[47,91,94,-35,-45,-44,-34,-36,]),'ARROW':([35,],[48,]),'SEMICOLON':([38,46,53,56,61,90,91,94,100,109,116,],[49,57,62,68,72,101,102,105,110,115,119,]),'STACK_TRACE':([40,72,],[51,-32,]),'NUMBER':([42,89,118,],[53,100,120,]),'FILE_LIST':([44,68,],[55,-42,]),'LOGLEVEL':([47,],[58,]),'LBRACE':([48,71,95,],[59,86,86,]),'BEGIN_BACKUP_UPDATE':([54,65,87,102,],[66,66,-50,-43,]),'ENTRY_NUMBER':([58,],[69,]),'RESULT':([59,],[70,]),'TIMESTAMP':([66,],[76,]),'ENTRY_MESSAGE':([69,],[79,]),'PASS':([70,],[82,]),'FAIL':([70,],[83,]),'END_BACKUP_UPDATE':([74,98,115,],[87,-51,-54,]),'PROGRESS':([75,101,],[89,-52,]),'COMMA':([78,80,81,82,83,85,96,114,117,],[92,-24,93,-22,-23,95,107,-37,-36,]),'FUNCTION':([86,],[97,]),'DETAILS':([88,110,],[99,-53,]),'LATENCY':([93,],[104,]),'LINE':([107,],[113,]),'RBRACE':([111,112,120,],[116,117,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'entries':([0,3,],[2,6,]),'entry':([0,3,],[3,3,]),'log_line':([0,3,],[4,4,]),'blocks_opt':([4,],[7,]),'blocks':([4,9,],[8,19,]),'block':([4,9,],[9,9,]),'diagnostic_block':([4,9,],[10,10,]),'boot_block':([4,9,],[11,11,]),'crash_block':([4,9,],[12,12,]),'backup_block':([4,9,],[13,13,]),'check_list':([14,21,],[20,34,]),'check_line':([14,21,],[21,21,]),'step_list':([15,24,],[23,37,]),'step_line':([15,24,],[24,24,]),'crash_content':([16,],[26,]),'error_code_line':([16,],[27,]),'backup_content':([17,],[29,]),'source_line':([17,],[30,]),'message_line':([27,],[40,]),'destination_line':([30,],[44,]),'stack_trace_line':([40,],[50,]),'file_list_line':([44,],[54,]),'backup_update_list_opt':([54,],[63,]),'backup_update_list':([54,65,],[64,73,]),'backup_update_block':([54,65,],[65,65,]),'backup_update_content':([66,],[74,]),'timestamp_line':([66,],[75,]),'file_entries':([67,92,],[77,103,]),'result_value':([70,],[81,]),'stack_items':([71,95,],[84,106,]),'stack_item':([71,95,],[85,85,]),'progress_line':([75,],[88,]),'function_line':([86,],[96,]),'details_line':([88,],[98,]),'line_line':([107,],[112,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> entries','S',1,'p_S','parser.py',17),
  ('entries -> entry entries','entries',2,'p_entries_multiple','parser.py',21),
  ('entries -> entry','entries',1,'p_entries_single','parser.py',25),
  ('entry -> log_line blocks_opt','entry',2,'p_entry_log','parser.py',35),
  ('log_line -> LBRACKET DATE TIME RBRACKET LOGLEVEL ENTRY_NUMBER ENTRY_MESSAGE','log_line',7,'p_log_line','parser.py',39),
  ('blocks_opt -> blocks','blocks_opt',1,'p_blocks_opt','parser.py',43),
  ('blocks_opt -> <empty>','blocks_opt',0,'p_blocks_opt_empty','parser.py',47),
  ('blocks -> block blocks','blocks',2,'p_blocks_multiple','parser.py',51),
  ('blocks -> block','blocks',1,'p_blocks_single','parser.py',55),
  ('block -> diagnostic_block','block',1,'p_block','parser.py',59),
  ('block -> boot_block','block',1,'p_block','parser.py',60),
  ('block -> crash_block','block',1,'p_block','parser.py',61),
  ('block -> backup_block','block',1,'p_block','parser.py',62),
  ('diagnostic_block -> BEGIN_DIAGNOSTIC check_list END_DIAGNOSTIC','diagnostic_block',3,'p_diagnostic_block','parser.py',66),
  ('check_list -> check_line check_list','check_list',2,'p_check_list_multiple','parser.py',70),
  ('check_list -> check_line','check_list',1,'p_check_list_single','parser.py',74),
  ('check_line -> CHECK STRING ARROW LBRACE RESULT result_value COMMA LATENCY STRING RBRACE SEMICOLON','check_line',11,'p_check_line','parser.py',78),
  ('CHECK_STRING -> VIDEO','CHECK_STRING',1,'p_check_string','parser.py',81),
  ('CHECK_STRING -> AUDIO','CHECK_STRING',1,'p_check_string','parser.py',82),
  ('CHECK_STRING -> NETWORK','CHECK_STRING',1,'p_check_string','parser.py',83),
  ('CHECK_STRING -> STORAGE','CHECK_STRING',1,'p_check_string','parser.py',84),
  ('result_value -> PASS','result_value',1,'p_result_value_pass','parser.py',87),
  ('result_value -> FAIL','result_value',1,'p_result_value_fail','parser.py',91),
  ('result_value -> STRING','result_value',1,'p_result_value_string','parser.py',95),
  ('boot_block -> BEGIN_BOOT_SEQUENCE step_list END_BOOT_SEQUENCE','boot_block',3,'p_boot_block','parser.py',99),
  ('step_list -> step_line step_list','step_list',2,'p_step_list_multiple','parser.py',103),
  ('step_list -> step_line','step_list',1,'p_step_list_single','parser.py',107),
  ('step_line -> STEP STRING SEMICOLON','step_line',3,'p_step_line','parser.py',111),
  ('crash_block -> BEGIN_CRASH_REPORT crash_content END_CRASH_REPORT','crash_block',3,'p_crash_block','parser.py',115),
  ('crash_content -> error_code_line message_line stack_trace_line','crash_content',3,'p_crash_content','parser.py',119),
  ('error_code_line -> IDENTIFIER COLON NUMBER SEMICOLON','error_code_line',4,'p_error_code_line','parser.py',123),
  ('message_line -> IDENTIFIER COLON STRING SEMICOLON','message_line',4,'p_message_line','parser.py',127),
  ('stack_trace_line -> STACK_TRACE COLON LBRACKET stack_items RBRACKET SEMICOLON','stack_trace_line',6,'p_stack_trace_line','parser.py',131),
  ('stack_items -> stack_item COMMA stack_items','stack_items',3,'p_stack_items_multiple','parser.py',135),
  ('stack_items -> stack_item','stack_items',1,'p_stack_items_single','parser.py',139),
  ('stack_item -> LBRACE function_line COMMA line_line RBRACE','stack_item',5,'p_stack_item','parser.py',143),
  ('function_line -> FUNCTION COLON STRING','function_line',3,'p_function_line','parser.py',147),
  ('line_line -> LINE COLON NUMBER','line_line',3,'p_line_line','parser.py',151),
  ('backup_block -> BEGIN_BACKUP backup_content END_BACKUP','backup_block',3,'p_backup_block','parser.py',155),
  ('backup_content -> source_line destination_line file_list_line backup_update_list_opt','backup_content',4,'p_backup_content','parser.py',159),
  ('source_line -> SOURCE STRING SEMICOLON','source_line',3,'p_source_line','parser.py',163),
  ('destination_line -> DESTINATION STRING SEMICOLON','destination_line',3,'p_destination_line','parser.py',167),
  ('file_list_line -> FILE_LIST LBRACKET file_entries RBRACKET SEMICOLON','file_list_line',5,'p_file_list_line','parser.py',171),
  ('file_entries -> STRING COMMA file_entries','file_entries',3,'p_file_entries_multiple','parser.py',175),
  ('file_entries -> STRING COMMA','file_entries',2,'p_file_entries_single','parser.py',179),
  ('backup_update_list_opt -> backup_update_list','backup_update_list_opt',1,'p_backup_update_list_opt','parser.py',183),
  ('backup_update_list_opt -> <empty>','backup_update_list_opt',0,'p_backup_update_list_opt_empty','parser.py',187),
  ('backup_update_list -> backup_update_block backup_update_list','backup_update_list',2,'p_backup_update_list_multiple','parser.py',191),
  ('backup_update_list -> backup_update_block','backup_update_list',1,'p_backup_update_list_single','parser.py',195),
  ('backup_update_block -> BEGIN_BACKUP_UPDATE backup_update_content END_BACKUP_UPDATE','backup_update_block',3,'p_backup_update_block','parser.py',199),
  ('backup_update_content -> timestamp_line progress_line details_line','backup_update_content',3,'p_backup_update_content','parser.py',203),
  ('timestamp_line -> TIMESTAMP STRING SEMICOLON','timestamp_line',3,'p_timestamp_line','parser.py',207),
  ('progress_line -> PROGRESS NUMBER SEMICOLON','progress_line',3,'p_progress_line','parser.py',211),
  ('details_line -> DETAILS STRING SEMICOLON','details_line',3,'p_details_line','parser.py',215),
]
