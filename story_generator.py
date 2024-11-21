import random
from helper import timing_decorator

class StoryGenerator:
    """
    StoryGenerator: Genera cuentos únicos basados en una gramática libre de contexto.
    """

    def __init__(self, rule: dict) -> None:
        """
        Inicializa el StoryGenerator.

        Atributos:
        - rule (dict): Reglas de la gramática que definen la estructura del cuento.
        - unprocessed_queue (list): Cola para rastrear las secuencias no procesadas.
        - generated_stories (list): Lista para almacenar los cuentos generados.
        """
        self.rule = rule
        self.unprocessed_queue = [['STORY']]
        self.generated_stories = []

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

    @timing_decorator
    def generate_story(self) -> str:
        """
        Genera un único cuento.

        Returns:
        - str: Cuento generado.
        """
        story = self.__get_story(self.unprocessed_queue.pop(0))
        self.generated_stories.append(story)
        return story
