def is_terminal(symbols):
    return not any(symbol[0].isupper() for symbol in symbols.split())

def parse_grammar(file_path: str) -> dict:
    grammar = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if "->" in line:
                key, values = line.strip().split("->")
                key = key.strip()
                values = [value.strip().split() for value in values.split("|")]
                grammar.setdefault(key, []).extend(values)
    return grammar
