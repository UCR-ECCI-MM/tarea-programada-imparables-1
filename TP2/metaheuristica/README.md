# **Generador de Contraseñas Seguras con Simulated Annealing**

Este proyecto implementa un generador de contraseñas seguras basado en la metaheurística **Simulated Annealing (SA)**. El objetivo es crear contraseñas que cumplan con criterios específicos de seguridad, como longitud mínima, diversidad de caracteres y ausencia de repeticiones significativas.

---

## **Descripción del problema**

A medida que aumentan las necesidades de seguridad en el ámbito digital, se requieren contraseñas robustas que cumplan con reglas específicas, como incluir letras mayúsculas, minúsculas, dígitos y caracteres especiales. 

Este problema tiene un espacio de búsqueda exponencial, ya que cada carácter puede ser seleccionado de un conjunto extenso de símbolos, lo que lo clasifica como un problema NP-Duro. Este programa utiliza **Simulated Annealing** para abordar la complejidad y encontrar soluciones eficientes.

---

## **Estructura del código**

### **1. `evaluate_password(password, min_length=8, required_categories=3)`**
Evalúa la calidad de una contraseña basándose en:
- Inclusión de letras mayúsculas, minúsculas, dígitos y caracteres especiales.
- Longitud mínima.
- Reducción de puntos por caracteres repetidos.

La puntuación final está normalizada en un rango de **0 a 10**, donde 10 es una contraseña óptima.

---

### **2. `generate_initial_password(length=8)`**
Genera una contraseña inicial aleatoria de una longitud definida por el usuario. Utiliza un conjunto extendido de caracteres ASCII que incluye:
- Letras mayúsculas y minúsculas.
- Números.
- Símbolos especiales estándar y extendidos.

---

### **3. `get_neighbor(password)`**
Genera una contraseña vecina modificando un carácter aleatorio de la contraseña actual. Esto permite explorar el espacio de soluciones.

---

### **4. `simulated_annealing(init_password, max_iterations=1000, init_temp=100, cooling_rate=0.99)`**
La implementación principal de Simulated Annealing:
- Parte de una contraseña inicial generada aleatoriamente.
- Evalúa las contraseñas vecinas y decide si las acepta o no, basándose en un criterio probabilístico controlado por la temperatura.
- Ajusta la temperatura gradualmente con un factor de enfriamiento.

El proceso finaliza cuando se alcanza el máximo de iteraciones o la temperatura es demasiado baja.

---

## **Requisitos**

- Python 3.6 o superior.
- Biblioteca estándar de Python (`random`, `string`, `math`).

---

## **Ejecución del programa**

1. Abre una terminal y navega a la carpeta `TP2/metaheuristica`:

   ```sh
   cd TP2/metaheuristica
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
   python metaheuristica.py
   ```

---

## **Ejemplo de salida**

```txt
Contraseña inicial: J3$mX,~
Contraseña final: 4l¡MwZo
Puntuación final: 9.5 
```

---

## **Parametros Configurables**

- **length**: Define la longitud de la contraseña inicial. (Predeterminado: 8).
- **max_iterations**: Número máximo de iteraciones para el algoritmo. (Predeterminado: 1000).
- **init_temp**: Temperatura inicial del algoritmo. (Predeterminado: 100).
- **cooling_rate**: Tasa de enfriamiento para reducir gradualmente la temperatura. (Predeterminado: 0.99).
