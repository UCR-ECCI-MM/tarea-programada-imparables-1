import string
import time
import random
from hashlib import sha256

COMMON_SEQUENCES = [
    "abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz",
    "123", "234", "345", "456", "567", "678", "789", "890", "012",
    "qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop", "asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl", "zxc", "xcv", "cvb", "vbn", "bnm"
]

# Extended character set: ASCII + extra symbols
extended_symbols = (
    string.ascii_letters + 
    string.digits + 
    string.punctuation + 
    "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×÷"
)

def heuristicGeneratePassword(initialSymbol, passLength):
    """
    Generates a secure password using a heuristic approach.
    """
    password = initialSymbol

    while len(password) < passLength:
        # Get neighbors (arbitrary selection: ASCII range around current char)
        current_char = password[-1]
        neighbors = [
            chr((ord(current_char) + i) % 128) for i in range(1, 10)
        ] + [
            chr((ord(current_char) - i) % 128) for i in range(1, 10)
        ]
        
        # Filter neighbors that are in the extended symbol set
        valid_neighbors = [
            c for c in neighbors if c in extended_symbols and c not in password[-1:]
        ]

        # Add fallback to random choice from the extended set
        if valid_neighbors:
            next_char = random.choice(valid_neighbors)
        else:
            next_char = random.choice(extended_symbols)
        
        password += next_char
        score = evaluate_password(password)

    return password, score

# Function to evaluate the password based on security criteria
def evaluate_password(password, min_length=8, required_categories=3):
  categories = {
    "lower": any(c.islower() for c in password),
    "upper": any(c.isupper() for c in password),
    "digit": any(c.isdigit() for c in password),
    "special": any(c in string.punctuation for c in password),
    "common_seq": not any(seq in password.lower() for seq in COMMON_SEQUENCES),
  }
  score = sum(categories.values())  # Maximum score is 5 if all categories are met

  # Penalize if not enough categories are met
  if len(password) < min_length:
    score -= (min_length - len(password)) * 0.5  # Penalización más leve

  # Penalize for repeated characters
  repetitions = len(password) - len(set(password))
  score -= repetitions * 0.5

  # Normalize the score to a scale of 0 to 10
  max_score = 5  # Maximum score based on categories before penalizations
  normalized_score = max(0, min(10, (score / max_score) * 10))
  return normalized_score

def main():
    """
    Main function to initialize password generation, check requirements, and measure execution time.
    """
    initialSymbol = '!'  # Initial symbol of the password
    passLength = 12  # Desired length of the password

    # Start the timer
    start_time = time.time()

    # Generate a password using the heuristic method
    password, score = heuristicGeneratePassword(initialSymbol, passLength)

    # Check if the generated password meets the requirements
    if score >= 5:
        print("Contraseña generada que cumple los requisitos: ", password)
        print("Puntuación de seguridad: ", score)
    else:
        print("La contraseña generada no cumple con los requisitos: ", password)
        print("Puntuación de seguridad: ", score)

    # End the timer
    end_time = time.time()

    # Print the execution time
    print("Tiempo de ejecución: %s segundos" % (end_time - start_time))


if __name__ == "__main__":
    main()