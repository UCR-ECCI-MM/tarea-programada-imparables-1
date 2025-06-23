### **Generación de Contraseña - Heurística**

Este proyecto implementa un generador de contraseñas seguras utilizando un enfoque **heurístico**. El algoritmo construye progresivamente la contraseña, eligiendo los caracteres más adecuados a partir de un conjunto de opciones vecinas, hasta cumplir con todos los requisitos de seguridad.

---

### **Requisitos**

- Python 3.x instalado en tu sistema.

---

### **Ejecución**

Para ejecutar este generador de contraseñas heurístico, sigue estos pasos:

1. Asegúrate de estar en el directorio que contiene el archivo `heuristica.py`.  
2. Ejecuta el siguiente comando en tu terminal:  

   ```bash
   python3 heuristica.py
   ```

---

### **Funcionamiento del Algoritmo**

El algoritmo genera contraseñas mediante los siguientes pasos:  
1. Comienza con un símbolo inicial dado por el usuario.  
2. Selecciona caracteres vecinos basados en valores ASCII cercanos al último carácter de la contraseña.  
3. Filtra las opciones vecinas según su validez, asegurándose de cumplir con:  
   - No repetir caracteres consecutivos.  
   - Incluir al menos una mayúscula, una minúscula, un dígito y un símbolo especial.  
4. Añade al resultado el carácter más adecuado hasta completar la longitud deseada.  

---

### **Notas**

- Este enfoque es eficiente porque evita explorar exhaustivamente todas las combinaciones posibles.  
- La técnica utilizada balancea la búsqueda local y el cumplimiento de las restricciones de seguridad, priorizando soluciones factibles en menos tiempo.