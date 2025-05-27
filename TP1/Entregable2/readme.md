# 🔍 Entregable 2 - Analizador Léxico

Implementación de lexer para procesamiento de logs del sistema.

## 🚀 Ejecución

### Requisitos previos
- Python 3.8+

- Estar en el entorno virtual y tenerlo activo.

- Tener estas dependencias instaladas:
   ```sh
   pip install matplotlib

   pip install PyQt5

   pip install ply
   ```

### Instrucciones
1. Asegúrate de estar en el entorno virtual y tenerlo activo

2. Ejecutar:
   ```sh
   python lexer.py
   ```
   o
   ```sh
   python -m Entregable2.lexer
   ```

## 📋 Funcionalidades
- Tokenización de líneas de log
- Identificación de:
  - Fechas y horas
  - Niveles de severidad (INFO, WARNING, ERROR)
  - IDs de proceso
  - Mensajes de sistema
- Validación de estructura básica

## 🧠 Estructura del Lexer
```python
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
```

## 📂 Archivos
```
Entregable2/
├── lexer.py
└── readme.md
```