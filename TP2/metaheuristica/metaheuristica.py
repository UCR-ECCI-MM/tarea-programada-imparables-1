import random
import string
import math
import os
import time

# Extended character set: ASCII + extra symbols
extended_symbols = (
    string.ascii_letters + 
    string.digits + 
    string.punctuation + 
    "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×÷"
)

COMMON_SEQUENCES = set([
    "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", 
    "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", 
    "uvw", "vwx", "wxy", "xyz", "123", "234", "345", "456", "567", "678", 
    "789", "890", "012", "qwe", "wer", "ert", "rty", "tyu", "yui", "uio", 
    "iop", "asd", "sdf", "dfg", "ghj", "hjk", "jkl", "zxc", "xcv", "cvb", 
    "vbn", "bnm", "password", "qwerty"
])

# Function to evaluate the password based on security criteria
def evaluate_password(password, min_length=8, required_categories=3):
  categories = {
    "lower": any(c.islower() for c in password),
    "upper": any(c.isupper() for c in password),
    "digit": any(c.isdigit() for c in password),
    "special": any(c in string.punctuation for c in password),
    "common_seq": not any(seq in password.lower() for seq in COMMON_SEQUENCES)
  }
  score = sum(categories.values())  # Maximum score is 5 if all categories are met

  # Penalty for missing required categories
  if len(password) < min_length:
    score -= (min_length - len(password)) * 0.5  # penalty for length

  # Penalty for repetitions
  repetitions = len(password) - len(set(password))
  score -= repetitions * 0.5

  # Normalize the score to a scale of 0 to 10
  max_score = 5  # Maximum score is 5 if all categories are met
  normalized_score = max(0, min(10, (score / max_score) * 10))
  return normalized_score


# Generate an initial password
def generate_initial_password(length=8):
  chars = extended_symbols
  return ''.join(random.choice(chars) for _ in range(length)) # Contraseña aleatoria

# Función de vecino para generar una nueva contraseña
def get_neighbor(password):
  chars = extended_symbols
  password = list(password) # Convert a string to a list for mutability
  
  # Select a random index to change
  index = random.randint(0, len(password) - 1)
  password[index] = random.choice(chars)
  
  return ''.join(password)

# Main function for Simulated Annealing
def simulated_annealing(init_password, max_iterations=1000, init_temp=100, cooling_rate=0.99):
  current_password = init_password
  current_score = evaluate_password(current_password)
  best_password = current_password
  best_score = current_score
  temperature = init_temp

  for iteration in range(max_iterations):
    new_password = get_neighbor(current_password)
    new_score = evaluate_password(new_password)

    # Calculate the change in score
    delta = new_score - current_score # Positive if new score is better, negative if worse

    # Accept or reject the new solution based on the Metropolis criterion
    # random.random() generate a random number between 0 and 1. If the number is less than the calculated value, the solution is accepted.
    # This allows the algorithm to escape local minima, especially at the beginning when the temperature is high.
    if delta > 0 or random.random() < math.exp(delta / temperature): 
      current_password = new_password
      current_score = new_score
      
      # Update the best solution found so far
      if new_score > best_score:
          best_password = new_password
          best_score = new_score
    
    # Reduce the temperature
    temperature *= cooling_rate

    # Break if the temperature is very low
    if temperature < 1e-3:
        break

  return best_password, best_score

# initial_password = generate_initial_password(length=8)
# result_password, result_score = simulated_annealing(initial_password)

# print("Contraseña inicial:", initial_password)
# print("Contraseña final:", result_password)
# print("Puntuación final:", result_score)

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    clear_console()
    print("=== Generador de Contraseñas Seguras (Metaheurística - Simulated Annealing) ===")
    initialSymbol = input("Ingrese el símbolo inicial de la contraseña: ")
    while len(initialSymbol) != 1:
        print("Por favor, ingrese solo un carácter.")
        initialSymbol = input("Ingrese el símbolo inicial de la contraseña: ")

    try:
        passLength = int(input("Ingrese la longitud deseada para la contraseña (sin contar el símbolo inicial, recomendado 8 o más): "))
        if passLength < 1:
            print("La longitud debe ser al menos 1.")
            return
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    start_time = time.time()
    solutions = []
    seen = set()
    while len(solutions) < 5:
        # Genera la contraseña inicial con el símbolo inicial fijo
        initial_password = initialSymbol + generate_initial_password(length=passLength)
        pwd, score = simulated_annealing(initial_password)
        # Asegura que la contraseña generada empiece con el símbolo inicial
        if pwd.startswith(initialSymbol) and pwd not in seen:
            solutions.append((pwd, score))
            seen.add(pwd)
    end_time = time.time()

    print("\nPropuestas de contraseñas seguras:")
    for idx, (pwd, score) in enumerate(solutions, 1):
        print(f"{idx}. {pwd}  |  Puntaje: {score}")

    print("\nTiempo de ejecución: %.4f segundos" % (end_time - start_time))

if __name__ == "__main__":
    main()