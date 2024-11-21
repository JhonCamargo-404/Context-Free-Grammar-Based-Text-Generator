import time

def timing_decorator(func):
    """
    Decorador para medir el tiempo de ejecución de una función.

    Uso:
    @timing_decorator
    def mi_funcion():
        # Implementación de la función

    El decorador imprime el tiempo transcurrido al ejecutar la función.

    Args:
    - func (callable): La función a decorar.

    Returns:
    - callable: La función decorada.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Función '{func.__name__}' tomó {elapsed_time:.4f} segundos.")
        return result
    return wrapper

def write_sentences_to_file(file_name: str, sentences: set):
    """
    Escribe cuentos generados en un archivo de texto.

    Args:
    - file_name (str): Nombre del archivo donde guardar los cuentos.
    - sentences (set): Conjunto de cuentos generados.

    Returns:
    - None
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for idx, sentence in enumerate(sentences, start=1):
            file.write(f"Cuento {idx}:\n")
            file.write(sentence + "\n\n")
    print(f"Se guardaron {len(sentences)} cuentos en el archivo '{file_name}'.")
