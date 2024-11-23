from flask import Flask, request, jsonify, render_template
from story_generator import StoryGenerator
from parse_grammar import parse_grammar
import os

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Configuración de gramática
GRAMMAR_FILE = "cuento.gr"
grammar_rules = parse_grammar(GRAMMAR_FILE)
story_generator = StoryGenerator(grammar_rules)
current_story = None  # Variable global para almacenar el cuento actual


@app.route("/")
def home():
    """Renderiza la página principal."""
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_story():
    global current_story
    try:
        current_story = story_generator.generate_story()
        return jsonify({"success": True, "story": current_story.replace('"', '')})
    except Exception as e:
        return jsonify({"success": False, "error": f"Error generando cuento: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
