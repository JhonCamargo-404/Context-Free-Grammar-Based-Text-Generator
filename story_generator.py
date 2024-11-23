import random
from helper import timing_decorator

class StoryGenerator:
    def __init__(self, rule: dict) -> None:
        """
        Inicializa el StoryGenerator.

        Atributos:
        - rule (dict): Reglas de la gramática que definen la estructura del cuento.
        """
        self.rule = rule
        self.reset_queue()  # Inicializa la cola de procesamiento
        self.generated_stories = []

    def reset_queue(self):
        """
        Reinicia la cola de procesamiento para generar un nuevo cuento.
        """
        self.unprocessed_queue = [['STORY']]

    def __get_story(self, grammar: list) -> str:
        """
        Genera un cuento único basado en la gramática proporcionada.

        Args:
        - grammar (list): Lista con la secuencia de símbolos a procesar.

        Returns:
        - str: El cuento generado como texto.
        """
        story = ''
        while grammar:
            first_symbol = grammar.pop(0)
            derived = self.rule.get(first_symbol, None)
            if derived:
                # Selección aleatoria de la expansión
                expansion = random.choice(derived)
                grammar = expansion + grammar
            else:
                story += ' ' + first_symbol
        return story.strip().capitalize()

    def generate_story(self) -> str:
        """
        Genera un único cuento. Reinicia la cola antes de procesar.

        Returns:
        - str: Cuento generado.
        """
        self.reset_queue()  # Reinicia la cola antes de generar
        story = self.__get_story(self.unprocessed_queue.pop(0))
        self.generated_stories.append(story)
        return story

