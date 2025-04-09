
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW AUDIO BEGIN_BACKUP BEGIN_BACKUP_UPDATE BEGIN_BOOT_SEQUENCE BEGIN_CRASH_REPORT BEGIN_DIAGNOSTIC CHECK COLON COMMA DATE DESTINATION DETAILS END_BACKUP END_BACKUP_UPDATE END_BOOT_SEQUENCE END_CRASH_REPORT END_DIAGNOSTIC ENTRY_MESSAGE ENTRY_NUMBER ERROR_CODE FAIL FILE_LIST FUNCTION IDENTIFIER LATENCY LBRACE LBRACKET LINE LOGLEVEL MESSAGE MINUS NETWORK NUMBER PASS PROGRESS RBRACE RBRACKET RESULT SEMICOLON SOURCE STACK_TRACE STEP STORAGE STRING TIME TIMESTAMP VIDEOS : entriesentries : entry entriesentries : entryentry : log_line blocks_optlog_line : LBRACKET DATE TIME RBRACKET LOGLEVEL ENTRY_NUMBER ENTRY_MESSAGEblocks_opt : blocksblocks_opt : blocks : block blocksblocks : blockblock : diagnostic_block \n| boot_block \n| crash_block \n| backup_blockdiagnostic_block : BEGIN_DIAGNOSTIC check_list END_DIAGNOSTICcheck_list : check_line check_listcheck_list : check_linecheck_line : CHECK COLON STRING ARROW LBRACE RESULT COLON result_value COMMA LATENCY COLON STRING RBRACE SEMICOLONresult_value : PASSresult_value : FAILresult_value : STRINGboot_block : BEGIN_BOOT_SEQUENCE step_list END_BOOT_SEQUENCEstep_list : step_line step_liststep_list : step_linestep_line : STEP COLON STRING SEMICOLONcrash_block : BEGIN_CRASH_REPORT crash_content END_CRASH_REPORTcrash_content : error_code_line message_line stack_trace_lineerror_code_line : IDENTIFIER COLON NUMBER SEMICOLONmessage_line : IDENTIFIER COLON STRING SEMICOLONstack_trace_line : STACK_TRACE COLON LBRACKET stack_items RBRACKET SEMICOLONstack_items : stack_item COMMA stack_itemsstack_items : stack_itemstack_item : LBRACE function_line COMMA line_line RBRACEfunction_line : FUNCTION COLON STRINGline_line : LINE COLON NUMBERbackup_block : BEGIN_BACKUP backup_content END_BACKUPbackup_content : source_line destination_line file_list_line backup_update_list_optsource_line : SOURCE COLON STRING SEMICOLONdestination_line : DESTINATION COLON STRING SEMICOLONfile_list_line : FILE_LIST COLON LBRACKET file_entries RBRACKET SEMICOLONfile_entries : STRING COMMA file_entriesfile_entries : STRINGbackup_update_list_opt : backup_update_listbackup_update_list_opt : backup_update_list : backup_update_block backup_update_listbackup_update_list : backup_update_blockbackup_update_block : BEGIN_BACKUP_UPDATE backup_update_content END_BACKUP_UPDATEbackup_update_content : timestamp_line progress_line details_linetimestamp_line : TIMESTAMP COLON STRING SEMICOLONprogress_line : PROGRESS COLON NUMBER SEMICOLONdetails_line : DETAILS COLON STRING SEMICOLON'
    
_lr_action_items = {'LBRACKET':([0,3,4,7,8,9,10,11,12,13,19,33,36,39,43,61,68,81,],[5,5,-7,-4,-6,-9,-10,-11,-12,-13,-8,-14,-21,-25,-35,73,79,-5,]),'$end':([1,2,3,4,6,7,8,9,10,11,12,13,19,33,36,39,43,81,],[0,-1,-3,-7,-2,-4,-6,-9,-10,-11,-12,-13,-8,-14,-21,-25,-35,-5,]),'BEGIN_DIAGNOSTIC':([4,9,10,11,12,13,33,36,39,43,81,],[14,14,-10,-11,-12,-13,-14,-21,-25,-35,-5,]),'BEGIN_BOOT_SEQUENCE':([4,9,10,11,12,13,33,36,39,43,81,],[15,15,-10,-11,-12,-13,-14,-21,-25,-35,-5,]),'BEGIN_CRASH_REPORT':([4,9,10,11,12,13,33,36,39,43,81,],[16,16,-10,-11,-12,-13,-14,-21,-25,-35,-5,]),'BEGIN_BACKUP':([4,9,10,11,12,13,33,36,39,43,81,],[17,17,-10,-11,-12,-13,-14,-21,-25,-35,-5,]),'DATE':([5,],[18,]),'CHECK':([14,21,130,],[22,22,-17,]),'STEP':([15,24,60,],[25,25,-24,]),'IDENTIFIER':([16,27,63,],[28,41,-27,]),'SOURCE':([17,],[31,]),'TIME':([18,],[32,]),'END_DIAGNOSTIC':([20,21,34,130,],[33,-16,-15,-17,]),'COLON':([22,25,28,31,41,45,51,55,78,82,88,96,98,118,122,],[35,38,42,46,52,56,61,68,89,92,99,110,111,124,126,]),'END_BOOT_SEQUENCE':([23,24,37,60,],[36,-23,-22,-24,]),'END_CRASH_REPORT':([26,50,107,],[39,-26,-29,]),'END_BACKUP':([29,54,64,65,66,75,86,114,],[43,-43,-36,-42,-45,-44,-46,-39,]),'DESTINATION':([30,70,],[45,-37,]),'RBRACKET':([32,83,84,90,91,108,115,123,],[47,93,-31,101,-41,-30,-40,-32,]),'STRING':([35,38,46,52,56,79,89,92,102,110,111,126,],[48,49,57,62,69,91,100,103,91,119,120,128,]),'STACK_TRACE':([40,74,],[51,-28,]),'NUMBER':([42,99,124,],[53,112,127,]),'FILE_LIST':([44,80,],[55,-38,]),'LOGLEVEL':([47,],[58,]),'ARROW':([48,],[59,]),'SEMICOLON':([49,53,57,62,69,93,100,101,112,120,129,],[60,63,70,74,80,107,113,114,121,125,130,]),'BEGIN_BACKUP_UPDATE':([54,66,86,114,],[67,67,-46,-39,]),'ENTRY_NUMBER':([58,],[71,]),'LBRACE':([59,73,94,],[72,85,85,]),'TIMESTAMP':([67,],[78,]),'ENTRY_MESSAGE':([71,],[81,]),'RESULT':([72,],[82,]),'END_BACKUP_UPDATE':([76,97,125,],[86,-47,-50,]),'PROGRESS':([77,113,],[88,-48,]),'COMMA':([84,91,95,103,104,105,106,119,123,],[94,102,109,-20,116,-18,-19,-33,-32,]),'FUNCTION':([85,],[96,]),'DETAILS':([87,121,],[98,-49,]),'PASS':([92,],[105,]),'FAIL':([92,],[106,]),'LINE':([109,],[118,]),'LATENCY':([116,],[122,]),'RBRACE':([117,127,128,],[123,-34,129,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'entries':([0,3,],[2,6,]),'entry':([0,3,],[3,3,]),'log_line':([0,3,],[4,4,]),'blocks_opt':([4,],[7,]),'blocks':([4,9,],[8,19,]),'block':([4,9,],[9,9,]),'diagnostic_block':([4,9,],[10,10,]),'boot_block':([4,9,],[11,11,]),'crash_block':([4,9,],[12,12,]),'backup_block':([4,9,],[13,13,]),'check_list':([14,21,],[20,34,]),'check_line':([14,21,],[21,21,]),'step_list':([15,24,],[23,37,]),'step_line':([15,24,],[24,24,]),'crash_content':([16,],[26,]),'error_code_line':([16,],[27,]),'backup_content':([17,],[29,]),'source_line':([17,],[30,]),'message_line':([27,],[40,]),'destination_line':([30,],[44,]),'stack_trace_line':([40,],[50,]),'file_list_line':([44,],[54,]),'backup_update_list_opt':([54,],[64,]),'backup_update_list':([54,66,],[65,75,]),'backup_update_block':([54,66,],[66,66,]),'backup_update_content':([67,],[76,]),'timestamp_line':([67,],[77,]),'stack_items':([73,94,],[83,108,]),'stack_item':([73,94,],[84,84,]),'progress_line':([77,],[87,]),'file_entries':([79,102,],[90,115,]),'function_line':([85,],[95,]),'details_line':([87,],[97,]),'result_value':([92,],[104,]),'line_line':([109,],[117,]),}

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
  ('check_line -> CHECK COLON STRING ARROW LBRACE RESULT COLON result_value COMMA LATENCY COLON STRING RBRACE SEMICOLON','check_line',14,'p_check_line','parser.py',78),
  ('result_value -> PASS','result_value',1,'p_result_value_pass','parser.py',81),
  ('result_value -> FAIL','result_value',1,'p_result_value_fail','parser.py',85),
  ('result_value -> STRING','result_value',1,'p_result_value_string','parser.py',89),
  ('boot_block -> BEGIN_BOOT_SEQUENCE step_list END_BOOT_SEQUENCE','boot_block',3,'p_boot_block','parser.py',93),
  ('step_list -> step_line step_list','step_list',2,'p_step_list_multiple','parser.py',97),
  ('step_list -> step_line','step_list',1,'p_step_list_single','parser.py',101),
  ('step_line -> STEP COLON STRING SEMICOLON','step_line',4,'p_step_line','parser.py',105),
  ('crash_block -> BEGIN_CRASH_REPORT crash_content END_CRASH_REPORT','crash_block',3,'p_crash_block','parser.py',109),
  ('crash_content -> error_code_line message_line stack_trace_line','crash_content',3,'p_crash_content','parser.py',113),
  ('error_code_line -> IDENTIFIER COLON NUMBER SEMICOLON','error_code_line',4,'p_error_code_line','parser.py',117),
  ('message_line -> IDENTIFIER COLON STRING SEMICOLON','message_line',4,'p_message_line','parser.py',121),
  ('stack_trace_line -> STACK_TRACE COLON LBRACKET stack_items RBRACKET SEMICOLON','stack_trace_line',6,'p_stack_trace_line','parser.py',125),
  ('stack_items -> stack_item COMMA stack_items','stack_items',3,'p_stack_items_multiple','parser.py',129),
  ('stack_items -> stack_item','stack_items',1,'p_stack_items_single','parser.py',133),
  ('stack_item -> LBRACE function_line COMMA line_line RBRACE','stack_item',5,'p_stack_item','parser.py',137),
  ('function_line -> FUNCTION COLON STRING','function_line',3,'p_function_line','parser.py',141),
  ('line_line -> LINE COLON NUMBER','line_line',3,'p_line_line','parser.py',145),
  ('backup_block -> BEGIN_BACKUP backup_content END_BACKUP','backup_block',3,'p_backup_block','parser.py',149),
  ('backup_content -> source_line destination_line file_list_line backup_update_list_opt','backup_content',4,'p_backup_content','parser.py',153),
  ('source_line -> SOURCE COLON STRING SEMICOLON','source_line',4,'p_source_line','parser.py',157),
  ('destination_line -> DESTINATION COLON STRING SEMICOLON','destination_line',4,'p_destination_line','parser.py',161),
  ('file_list_line -> FILE_LIST COLON LBRACKET file_entries RBRACKET SEMICOLON','file_list_line',6,'p_file_list_line','parser.py',165),
  ('file_entries -> STRING COMMA file_entries','file_entries',3,'p_file_entries_multiple','parser.py',169),
  ('file_entries -> STRING','file_entries',1,'p_file_entries_single','parser.py',173),
  ('backup_update_list_opt -> backup_update_list','backup_update_list_opt',1,'p_backup_update_list_opt','parser.py',177),
  ('backup_update_list_opt -> <empty>','backup_update_list_opt',0,'p_backup_update_list_opt_empty','parser.py',181),
  ('backup_update_list -> backup_update_block backup_update_list','backup_update_list',2,'p_backup_update_list_multiple','parser.py',185),
  ('backup_update_list -> backup_update_block','backup_update_list',1,'p_backup_update_list_single','parser.py',189),
  ('backup_update_block -> BEGIN_BACKUP_UPDATE backup_update_content END_BACKUP_UPDATE','backup_update_block',3,'p_backup_update_block','parser.py',193),
  ('backup_update_content -> timestamp_line progress_line details_line','backup_update_content',3,'p_backup_update_content','parser.py',197),
  ('timestamp_line -> TIMESTAMP COLON STRING SEMICOLON','timestamp_line',4,'p_timestamp_line','parser.py',201),
  ('progress_line -> PROGRESS COLON NUMBER SEMICOLON','progress_line',4,'p_progress_line','parser.py',205),
  ('details_line -> DETAILS COLON STRING SEMICOLON','details_line',4,'p_details_line','parser.py',209),
]
