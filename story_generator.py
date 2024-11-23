import random
class StoryGenerator:
    def __init__(self, rules: dict) -> None:
        self.rules = rules
        self.unprocessed_queue = []  
        self.generated_stories = []  

    def reset_queue(self):
        self.unprocessed_queue = [['STORY']]

    def __expand_grammar(self, grammar: list) -> str:
        story = ""
        while grammar:
            first_symbol = grammar.pop(0)
            derived = self.rules.get(first_symbol, None)
            if derived:
                grammar = random.choice(derived) + grammar
            else:
                story += f" {first_symbol}"
        return story.strip().capitalize()

    def generate_story(self) -> str:
        self.reset_queue()  
        story = self.__expand_grammar(self.unprocessed_queue.pop(0))
        self.generated_stories.append(story)
        return story
