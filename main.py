import os
from story_generator import StoryGenerator
from parse_grammar import parse_grammar
from helper import write_sentences_to_file

def main():
    """
    Genera un único cuento usando la gramática cargada.
    """
    try:
        # Cargar archivo de gramática
        grammar_file = 'cuento.gr'
        grammar_path = os.path.join(os.getcwd(), grammar_file)

        if not os.path.exists(grammar_path):
            raise FileNotFoundError(f"El archivo de gramática '{grammar_file}' no se encontró.")

        # Procesar la gramática
        print("Cargando la gramática...")
        rules = parse_grammar(grammar_path)

        # Crear instancia del generador
        story_generator = StoryGenerator(rules)

        # Generar un cuento
        print("Generando 1 cuento...")
        cuento = story_generator.generate_story()

        # Guardar el cuento en un archivo
        output_file = 'cuento_generado.txt'
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cuento)

        print(f"¡Cuento generado exitosamente y guardado en '{output_file}'!")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == '__main__':
    main()
