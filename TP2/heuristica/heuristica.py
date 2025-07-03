import string
import time
import random
import os

COMMON_SEQUENCES = set([
    "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", 
    "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", 
    "uvw", "vwx", "wxy", "xyz", "123", "234", "345", "456", "567", "678", 
    "789", "890", "012", "qwe", "wer", "ert", "rty", "tyu", "yui", "uio", 
    "iop", "asd", "sdf", "dfg", "ghj", "hjk", "jkl", "zxc", "xcv", "cvb", 
    "vbn", "bnm", "password", "qwerty"
])

extended_symbols = (
    string.ascii_letters + 
    string.digits + 
    string.punctuation + 
    "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×÷"
)

def heuristicGeneratePassword(initialSymbol, passLength):
    password = initialSymbol
    while len(password) < passLength:
        current_char = password[-1]
        neighbors = [
            chr((ord(current_char) + i) % 128) for i in range(1, 10)
        ] + [
            chr((ord(current_char) - i) % 128) for i in range(1, 10)
        ]
        valid_neighbors = [
            c for c in neighbors if c in extended_symbols and c not in password[-1:]
        ]
        if valid_neighbors:
            next_char = random.choice(valid_neighbors)
        else:
            next_char = random.choice(extended_symbols)
        password += next_char
    score = evaluate_password(password)
    return password, score

def evaluate_password(password, min_length=8, required_categories=3):
    categories = {
        "lower": any(c.islower() for c in password),
        "upper": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special": any(c in string.punctuation for c in password),
        "common_seq": not any(seq in password.lower() for seq in COMMON_SEQUENCES)
    }
    score = sum(categories.values())
    if len(password) < min_length:
        score -= (min_length - len(password)) * 0.5
    repetitions = len(password) - len(set(password))
    score -= repetitions * 0.5
    max_score = 5
    normalized_score = max(0, min(10, (score / max_score) * 10))
    return normalized_score

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    clear_console()
    print("=== Generador de Contraseñas Seguras (Heurística) ===")
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
        pwd, score = heuristicGeneratePassword(initialSymbol, passLength)
        if pwd not in seen:
            solutions.append((pwd, score))
            seen.add(pwd)
    end_time = time.time()

    print("\nPropuestas de contraseñas seguras:")
    for idx, (pwd, score) in enumerate(solutions, 1):
        print(f"{idx}. {pwd}  |  Puntaje: {score}")

    print("\nTiempo de ejecución: %.4f segundos" % (end_time - start_time))

if __name__ == "__main__":
    main()