def is_terminal(symbols):
    """
    Verifica si un conjunto de símbolos es terminal.

    Args:
    - symbols (str): Cadena que representa los símbolos de una regla.

    Returns:
    - bool: True si los símbolos son terminales, False si contienen no terminales.
    """
    return not any(symbol[0].isupper() for symbol in symbols.split())

def parse_grammar(file_path):
    """
    Procesa un archivo de gramática y lo convierte en un diccionario de reglas.

    Args:
    - file_path (str): Ruta del archivo de gramática.

    Returns:
    - dict: Diccionario que contiene las reglas de la gramática.
    """
    grammar = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Divide cada línea en partes (símbolo izquierda y derecha)
            line_segments = line.strip().split("->")
            if len(line_segments) == 2:
                key_data, value_data = line_segments
                key_data = key_data.strip()
                value_data = [alt.strip().split() for alt in value_data.split("|")]

                if key_data in grammar:
                    grammar[key_data].extend(value_data)
                else:
                    grammar[key_data] = value_data
    return grammar
