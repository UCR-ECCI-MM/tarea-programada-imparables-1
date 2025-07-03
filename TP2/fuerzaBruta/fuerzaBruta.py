import itertools
import string
import time
import os

# Secuencias comunes prohibidas
COMMON_SEQUENCES = [
    "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz",
    "123", "234", "345", "456", "567", "678", "789", "890", "012",
    "qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop", "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "zxc", "xcv", "cvb", "vbn", "bnm"
]

extended_symbols = (
    string.ascii_letters + 
    string.digits + 
    string.punctuation + 
    "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×÷"
)

def has_common_sequence(password):
    pw_lower = password.lower()
    for seq in COMMON_SEQUENCES:
        if seq in pw_lower:
            return True
    return False

def evaluate_password(password, min_length=8, required_categories=3):
  categories = {
    "lower": any(c.islower() for c in password),
    "upper": any(c.isupper() for c in password),
    "digit": any(c.isdigit() for c in password),
    "special": any(c in string.punctuation for c in password),
    "noCommonSeq": not has_common_sequence(password)
  }
  score = sum(categories.values())  # Máximo: 4 si todas las categorías están presentes

  # Penalización por longitud insuficiente
  if len(password) < min_length:
    score -= (min_length - len(password)) * 0.5  # Penalización más leve

  # Penalización por repetición de caracteres
  repetitions = len(password) - len(set(password))
  score -= repetitions * 0.5

  # Normalización para un rango entre 0 y 10
  max_score = 4  # Máximo posible antes de penalizaciones
  normalized_score = max(0, min(10, (score / max_score) * 10))
  return normalized_score

def checkRequirements(password):
    """
    Verifies if a password meets the following requirements:
    - Includes at least 1 uppercase character.
    - Includes at least 1 lowercase character.
    - Includes at least 1 digit.
    - Includes at least 1 special character.
    - Does not repeat characters consecutively.
    - Does not contain common sequences (abc, 123, qwerty, etc).
    """
    hasLower = any(c.islower() for c in password)
    hasUpper = any(c.isupper() for c in password)
    hasDigit = any(c.isdigit() for c in password)
    hasSymbol = any(c in extended_symbols for c in password)
    noRepeat = all(password[i] != password[i+1] for i in range(len(password) - 1))
    noCommonSeq = not has_common_sequence(password)

    return (hasLower and hasUpper and hasDigit and hasSymbol and noRepeat and noCommonSeq)

def generatePasswords(initialSymbol, passLength, max_results=5):
    """
    Generates up to max_results valid passwords of a specific length,
    starting from an initial symbol, and verifies if they meet the security requirements.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    solutions = []
    
    for combination in itertools.product(chars, repeat=passLength):
        password = initialSymbol + ''.join(combination)
        if checkRequirements(password):
            solutions.append(password)
            if len(solutions) >= max_results:
                break

    return solutions

def generatePasswordsWithLimit(initialSymbol, passLength, max_attempts=10000):
    """
    Genera contraseñas usando fuerza bruta con un límite de intentos.
    
    Parámetros:
    initialSymbol (str): Símbolo inicial fijo para cada contraseña.
    passLength (int): Longitud de las contraseñas excluyendo el símbolo inicial.
    max_attempts (int): Máximo número de intentos antes de detener la generación.
    
    Retorna:
    list: Lista de contraseñas válidas que cumplen los requisitos.
    """
    solutions = []
    attempts = 0
    score = 0

    for combination in itertools.product(extended_symbols, repeat=passLength):
        # Verificar si se alcanzó el límite de intentos
        if attempts >= max_attempts:
            print(f"Alcanzado el límite de intentos ({max_attempts}). Deteniendo.")
            break

        # Crear la contraseña
        password = initialSymbol + ''.join(combination)

        # Verificar si la contraseña cumple con los requisitos
        if evaluate_password(password) >= 0:
            solutions.append(password)
            score = evaluate_password(password)

        attempts += 1

    print(f"Intentos realizados: {attempts}")
    return solutions, score

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    clear_console()
    print("=== Generador de Contraseñas Seguras (Fuerza Bruta) ===")
    initialSymbol = input("Ingrese el símbolo inicial de la contraseña: ")
    while len(initialSymbol) != 1:
        print("Por favor, ingrese solo un carácter.")
        initialSymbol = input("Ingrese el símbolo inicial de la contraseña: ")

    try:
        passLength = int(input("Ingrese la longitud deseada para la contraseña (sin contar el símbolo inicial, recomendado 2 o 3): "))
        if passLength < 1:
            print("La longitud debe ser al menos 1.")
            return
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    start_time = time.time()
    solutions = generatePasswords(initialSymbol, passLength)
    end_time = time.time()

    if solutions:
        print("\nPropuestas de contraseñas seguras:")
        for idx, pwd in enumerate(solutions, 1):
            print(f"{idx}. {pwd}")
    else:
        print("No se encontraron contraseñas válidas con los parámetros dados.")

    print("\nTiempo de ejecución: %.4f segundos" % (end_time - start_time))


if __name__ == "__main__":
    main()