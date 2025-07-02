import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV proporcionado
file_path = 'TP2/doc/resultados_comparacion.csv'
data = pd.read_csv(file_path)



# Mostrar las primeras filas del archivo para entender su estructura
data.head(), data.info()

# Configuración del estilo de los gráficos
sns.set(style="whitegrid")

# Crear un gráfico para visualizar la relación entre longitud y tiempo de ejecución
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x="Longitud", y="Tiempo", hue="Técnica", marker="o")

# Títulos y etiquetas
plt.title("Relación entre la longitud de la entrada y el tiempo de solución", fontsize=14)
plt.xlabel("Longitud de la contraseña", fontsize=12)
plt.ylabel("Tiempo de ejecución (segundos)", fontsize=12)
plt.legend(title="Técnica", fontsize=10, title_fontsize=12)
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Crear un gráfico de barras para comparar las notas promedio de los resultados por técnica
plt.figure(figsize=(10, 6))

# Calcular la media de las notas por técnica
mean_scores = data.groupby("Técnica")["Resultados"].mean().sort_values(ascending=False)

# Graficar las barras
mean_scores.plot(kind="bar", color=["#4caf50", "#2196f3", "#f44336"], alpha=0.8)

# Personalización del gráfico
plt.title("Comparación de Notas Promedio entre Técnicas")
plt.xlabel("Técnica")
plt.ylabel("Nota Promedio")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.show()
