import random  # Importa el módulo random para realizar selecciones aleatorias

class StoryGenerator:
    # El constructor de la clase. Recibe un diccionario de reglas gramaticales.
    def __init__(self, rules: dict) -> None:
        self.rules = rules  # Guarda las reglas gramaticales pasadas al generador.
        self.unprocessed_queue = []  # Cola que contiene los símbolos no procesados.
        self.generated_stories = []  # Lista donde se almacenan los cuentos generados.

    # Reinicia la cola de procesamiento con el símbolo inicial 'STORY'
    def reset_queue(self):
        self.unprocessed_queue = [['STORY']]  # Comienza la cola con el símbolo inicial 'STORY'.

    # Expande recursivamente la gramática (símbolos no terminales) para generar un cuento
    def __expand_grammar(self, grammar: list) -> str:
        story = ""  # Inicia el cuento vacío
        while grammar:  # Mientras haya símbolos por procesar en la cola
            first_symbol = grammar.pop(0)  # Toma el primer símbolo de la cola

            # Busca las posibles expansiones del símbolo en las reglas gramaticales
            derived = self.rules.get(first_symbol, None)
            if derived:  # Si el símbolo es no terminal (tiene expansiones posibles)
                # Se elige una expansión aleatoria y se agrega al frente de la cola
                grammar = random.choice(derived) + grammar
            else:
                # Si el símbolo es terminal (una palabra real), se agrega al cuento
                story += f" {first_symbol}"

        # Devuelve el cuento generado, eliminando espacios extra y asegurándose de que empiece con mayúscula.
        return story.strip().capitalize()

    # Función principal para generar un cuento
    def generate_story(self) -> str:
        self.reset_queue()  # Reinicia la cola con el símbolo 'STORY' al inicio
        # Llama a la función privada que expande la gramática y genera el cuento
        story = self.__expand_grammar(self.unprocessed_queue.pop(0))
        self.generated_stories.append(story)  # Guarda el cuento generado en la lista
        return story  # Devuelve el cuento generado
