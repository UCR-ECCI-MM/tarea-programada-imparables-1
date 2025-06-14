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

def has_common_sequence(password):
    pw_lower = password.lower()
    for seq in COMMON_SEQUENCES:
        if seq in pw_lower:
            return True
    return False

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
    hasSymbol = any(c in string.punctuation for c in password)
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