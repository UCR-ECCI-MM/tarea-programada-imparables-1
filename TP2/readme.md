# Generación de Contraseñas Óptimas Basada en un Grafo de Símbolos ASCII

   - La carpeta `TP2/` contiene tres implementaciones diferentes para abordar el problema de generación de contraseñas seguras a partir de un grafo de símbolos ASCII. Cada técnica explora una estrategia única para la creación de contraseñas seguras que cumplan con requisitos específicos de seguridad, a partir de un símbolo ASCII inicial.

## Estructura de Subcarpetas

   Cada subcarpeta en `TP2/` contiene la implementación y archivos relacionados con una de las técnicas de resolución:

   - ### **fuerzaBruta/**  
      - **Código fuente** de la técnica de Fuerza Bruta, que explora todas las combinaciones posibles para generar una contraseña segura.
      - **Documentación** sobre la complejidad y limitaciones de la técnica.
      - **Instrucciones de ejecución** específicas para probar esta técnica en particular.

   - ### **heuristica/**  
      - **Código fuente** de la Heurística de vecino más cercano con restricciones, diseñada para reducir el tiempo de generación de contraseñas cumpliendo con requisitos de seguridad.
      - **Documentación** sobre la metodología, ventajas y limitaciones de esta técnica.
      - **Instrucciones de ejecución** específicas para probar la técnica Heurística.

   - ### **metaheuristica/**
      - **Código fuente** de la técnica de Simulated Annealing (SA), una metaheurística que optimiza el proceso de generación de contraseñas explorando rutas de caracteres de manera controlada.
      - **Documentación** sobre cómo SA permite obtener combinaciones robustas en un tiempo razonable.
      - **Instrucciones de ejecución** para probar la técnica de Simulated Annealing.


## Ejecución y Uso

   - Cada subcarpeta incluye instrucciones detalladas para ejecutar las pruebas y ejemplos de salida para evaluar la eficacia y eficiencia de cada técnica de generación de contraseñas.