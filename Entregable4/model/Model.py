import json
try: # Intento directo de importación
    from lexer import lexer  # Import the lexer instance
except ImportError:
    from Entregable4.lexer import lexer  # Import the lexer instance

try: # Intento directo de importación
    from parser import parser  # Import the lexer instance
except ImportError:
    from Entregable4.parser import parser  # Import the lexer instance

class Model:
    def __init__(self):
        """
        Initialize the model
        """
        self.data = []

    def lexerAnalyzeData(self, file_path):
        """
        Perform lexical analysis on the input data using the lexer, and returning all the tokens
        """
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                lexer.input(data)

                # Process tokens and store them
                self.lexical_data = [
                    {
                        'type': tok.type,
                        'value': tok.value,
                        'line': tok.lineno,
                        'position': tok.lexpos
                    }
                    for tok in lexer
                ]
                print("Análisis léxico completado y almacenado en el modelo.")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error during lexical analysis: {e}")

    def getLexicalData(self):
        """
        Retrieve the stored lexical analysis data, all the tokens info.
        """
        return self.lexical_data

    def lexerAnalyze(self, file_path):
        """
        Perform lexical analysis on the input data using the lexer, just the errors
        """
        self.lexical_errors = []  # Store lexical errors
        try:
            with open(file_path, 'r') as file:
                data = file.read()
                lexer.input(data)

                # Process tokens and check for errors
                for tok in lexer:
                    pass  # Process tokens normally (no need to store them here)

        except FileNotFoundError:
            error_message = f"File not found: {file_path}"
            self.lexical_errors.append(error_message)
        except Exception as e:
            error_message = f"Error during lexical analysis: {e}"
            self.lexical_errors.append(error_message)

        # Check for errors in the lexer
        if hasattr(lexer, 'errors') and lexer.errors:
            self.lexical_errors.extend(lexer.errors)

        # Return True if errors were found, False otherwise
        return len(self.lexical_errors) > 0

    def getLexicalErrors(self):
        """
        Retrieve the stored lexical errors, just errors.
        """
        return self.lexical_errors

    def parserAnalyzeData(self, file_path):
        """
        Parse the log file and store the data in the model
        """
        try:
            with open(file_path, 'r') as file:
                # Simulate parsing logic (replace with actual parser logic)
                data = file.read()
                # Example: Load parsed data into the model
                result = parser.parse(data)
                self.data = result
                print("Análisis sintáctico completado y almacenado en el modelo.")
                # For demonstration, simply print the parse tree (or parts of it)
                # from pprint import pprint
                # pprint(result)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {file_path}")

    def getParserData(self):
        """
        Return the parsed data
        """
        return self.data