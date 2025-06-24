### **Generación de Contraseña - Heurística**

Este proyecto implementa un generador de contraseñas seguras utilizando un enfoque **heurístico**. El algoritmo construye progresivamente la contraseña, eligiendo los caracteres más adecuados a partir de un conjunto de opciones vecinas, hasta cumplir con todos los requisitos de seguridad.

---

### **Requisitos**

- Python 3.x instalado en tu sistema.

---

### **Ejecución**

Para ejecutar este generador de contraseñas heurístico, sigue estos pasos:

1. Abre una terminal y navega a la carpeta `TP2/heuristica`:

   ```sh
   cd TP2/heuristica
   ```

2. Crea un entorno virtual:

   ```sh
   python3 -m venv venv
   ```

3. Activa el entorno virtual:
   - En Linux/Mac:

     ```sh
     source venv/bin/activate
     ```

   - En Windows:

     ```sh
     venv\Scripts\activate
     ```

4. Ejecuta el programa de fuerza bruta:

   ```sh
   python heuristica.py
   ```

---

### **Funcionamiento del Algoritmo**

El algoritmo genera contraseñas mediante los siguientes pasos:

1. Comienza con un símbolo inicial dado por el usuario.
2. Selecciona caracteres vecinos basados en valores ASCII cercanos al último carácter de la contraseña.  
3. Filtra las opciones vecinas según su validez, asegurándose de cumplir con:  
   - No repetir caracteres consecutivos.  
   - Incluir al menos una mayúscula, una minúscula, un dígito y un símbolo especial.
   - No contener alguna secuencia establecida en la lista de secuencias comunes.

4. Añade al resultado el carácter más adecuado hasta completar la longitud deseada.  

---

### **Notas**

- Este enfoque es eficiente porque evita explorar exhaustivamente todas las combinaciones posibles.  
- La técnica utilizada balancea la búsqueda local y el cumplimiento de las restricciones de seguridad, priorizando soluciones factibles en menos tiempo.
