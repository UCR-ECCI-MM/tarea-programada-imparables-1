import itertools
import string
import time

def checkRequirements(password):
  """
  Verifies if a password meets the following requirements:
  - Includes at least 1 uppercase character.
  - Includes at least 1 lowercase character.
  - Includes at least 1 digit.
  - Includes at least 1 special character.
  - Does not repeat characters.
  """
  hasLower = any(c.islower() for c in password)
  hasUpper = any(c.isupper() for c in password)
  hasDigit = any(c.isdigit() for c in password)
  hasSymbol = any(c in string.punctuation for c in password)
  noRepeat = all(password[i] != password[i+1] for i in range(len(password) - 1))

  return (hasLower and hasUpper and hasDigit and hasSymbol and noRepeat)

def generatePasswords(initialSymbol, passLength):
  """
  Generates all possible combinations of passwords of a specific length,
  starting from an initial symbol, and verifies if they meet the security requirements.
  """
  # Define the set of characters to be used in the passwords (ASCII letters, digits, and punctuation)
  chars = string.ascii_letters + string.digits + string.punctuation
  solutions = []
    
  # Generate all possible combinations of passwords of the specified length
  for combination in itertools.product(chars, repeat=passLength):
      # turn the combination into a string
      password = initialSymbol + ''.join(combination)
      
      # verify if the password meets the security requirements
      if checkRequirements(password): solutions.append(password)

  return solutions

def main():
  initialSymbol = 'A'  # Initial symbol of the password
  passLength = 3  # Length of the password

  start_time = time.time()
  solutions = generatePasswords(initialSymbol, passLength)
  end_time = time.time()

  print("Numero de contraseñas que cumplen con los requisitos de seguridad: ", len(solutions))
  print("Tiempo de ejecución: %s segundos" % (end_time - start_time))


if __name__ == "__main__":
  main()