import time
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Importa tus funciones de generación de contraseña desde los tres métodos.
from fuerzaBruta.fuerzaBruta import generatePasswordsWithLimit, extended_symbols as fb_symbols
from heuristica.heuristica import heuristicGeneratePassword, evaluate_password as heur_check
from metaheuristica.metaheuristica import generate_initial_password, simulated_annealing

# Configuración de las pruebas
initial_symbol = '!'
password_lengths = [6, 8, 10, 12]
num_trials = 5  # Número de repeticiones por longitud

# Archivo CSV para guardar los resultados
output_file = "resultados_comparacion.csv"

# Función para medir tiempos y guardar resultados
def run_experiments():
    results = []

    # Fuerza Bruta
    for length in password_lengths:
        for trial in range(num_trials):
            start_time = time.time()
            solutions, score = generatePasswordsWithLimit(initial_symbol, length, num_trials)
            end_time = time.time()
            results.append(["Fuerza Bruta", length, score, end_time - start_time])

    # Heurística
    for length in password_lengths:
        for trial in range(num_trials):
            start_time = time.time()
            password, score = heuristicGeneratePassword(initial_symbol, length)
            end_time = time.time()
            results.append(["Heurística", length, score, end_time - start_time])

    # Metaheurística
    for length in password_lengths:
        for trial in range(num_trials):
            start_time = time.time()
            init_password = generate_initial_password(length)
            final_password, final_score = simulated_annealing(init_password)
            end_time = time.time()
            results.append(["Metaheurística", length, final_score, end_time - start_time])

    # Guardar resultados en CSV
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Técnica", "Longitud", "Resultados", "Tiempo"])
        writer.writerows(results)

    print(f"Resultados guardados en {output_file}")


if __name__ == "__main__":
    run_experiments()
