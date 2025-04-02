# Repositorio de Los Imparables 2

Dentro de este repositorio se encuentra la **Tarea Programada #1** del grupo **Los Imparables 2**.

## Integrantes

- **Mario Cordero** - C22306  
- **Christopher Zuñiga** - C28730  

## 📌 Estilo de Código

Para la implementación en **Python**, se seguirá la guía de estilo **PEP 8** para mantener el código legible y estructurado correctamente.  
🔗 [Referencia oficial de PEP 8](https://peps.python.org/pep-0008/)  

## 📜 Descripción

En esta tarea, se desarrolla una aplicación en **Python** que procesa un archivo .txt el cual contiene un log perteneciente a un sistema operativo. El fin de la aplicación es poder ofrecer un entorno amigable con el usuario y de fácil acceso a la información proporcionada en el log, logrando con esto el fácil entendimiento y permitiendo así un mejor análisis de la información contenida en el archivo.

## 📊 Presentaciones y recursos TP1

- 🔗 [Presentación Entregable #1](https://www.canva.com/design/DAGhpk5KZds/vbva_ABSX7URnhySVLA9lg/edit?utm_content=DAGhpk5KZds&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- 🔗 [DOC Entregable #1 (Requisitos de software)](https://docs.google.com/document/d/1-pL6v0Fi6CXQtW9VehQbuTX9JwXbPxlaxotsDXyK8_g/edit?usp=sharing)
- 🔗 [Presentación Entregable #2](https://www.canva.com/design/DAGi46PW5a8/Ww5yINbbRVSs8eE37Smu2w/edit?utm_content=DAGi46PW5a8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- 🔗 [DOC Entregable #3 (Gramática)](https://docs.google.com/document/d/18mt0UUAWnmb6NcEyALx32VE0ToXhcSUkzyq41YL3sys/edit?usp=sharing)

## 🔄 Esquema de Commits

Para mantener un historial de cambios claro y organizado, se utilizará la siguiente convención de commits:

| **Tipo**      | **Descripción**                                   | **Ejemplo**                                  |
|--------------|-------------------------------------------------|----------------------------------------------|
| **- FEAT:**     | Nueva funcionalidad o característica             | `FEAT: implementar autenticación con JWT`   |
| **- FIX:**      | Corrección de errores o bugs                    | `FIX: corregir cálculo de impuestos`        |
| **- REFACTOR:** | Mejora del código sin modificar funcionalidad   | `REFACTOR: simplificar lógica de paginación` |

---

## 🚀 Ejecución del Proyecto

### 🔹 Windows (Recomendado abrir una terminal en VS code)

1. Asegúrate de tener **Python 3** instalado. Puedes verificarlo con:
   ```sh
   python --version
   ```
2. Clona el repositorio:
   ```sh
   git clone https://github.com/UCR-ECCI-MM/tarea-programada-imparables-1.git
   ```
3. Accede a la carpeta del proyecto:
   ```sh
   cd tareas-programadas-imparables-2
   ```
4. Crea un entorno virtual para dentro del mismo instalar las dependencias y poder correr el proyecto
   ```sh
   python -m venv entornomostro
   ```
5. Activa el entorno virtual
   ```sh
   .\entornomostro\Scripts\activate
   ```
6. Instala las dependencias para que puedas correr cualquier entregable
   ```sh
   pip install matplotlib
   pip install PyQt5
   pip install ply
   ```
7. Cómo correr cada etapa, una vez instaladas dependencias y dentro del entorno virtual
   - ##### Entregable 1
   ```sh
   python Entregable1/main.py
   ```
   - ##### Entregable 2
   ```sh
   python Entregable2/lexer.py
   ```
   - ##### Entregable 3
   ```sh
   python Entregable3/parser.py
   ```

### 🔹 Mac / Ubuntu

1. Asegúrate de tener **Python 3** instalado. Puedes verificarlo con:
   ```sh
   python3 --version
   ```
2. Clona el repositorio:
   ```sh
   git clone https://github.com/usuario/repo-imparables2.git
   ```
3. Accede a la carpeta del proyecto:
   ```sh
   cd repo-imparables2
   ```
4. Crea un entorno para instalar las librerias necesarias:
   ```sh
   python3 -m venv entornomostro
   ```
5. Accede al entorno:
   ```sh
   source entornomostro/bin/activate
   ```
6. Instala las librerias necesarias:
   ```sh
   pip install matplotlib

   pip install PyQt5

   pip install ply
   ```
7. Ejecuta el programa:
   ```sh
   python -m Entregable*.ejecutable
   ```
      - ##### Entregable 1
   ```sh
   python -m Entregable1.main
   ```
   - ##### Entregable 2
   ```sh
   python -m Entregable2.lexer
   ```
   - ##### Entregable 3
   ```sh
   python -m Entregable2.parser
---

### ✅ Notas:
- Se seguirá la guía de estilo **PEP 8** en el código fuente.
- Los commits estarán estructurados bajo el esquema de la tabla anterior.
- En cada carpeta de entregable estará un `readme.md` con las indicaciones para poder ejecutar el proyecto.