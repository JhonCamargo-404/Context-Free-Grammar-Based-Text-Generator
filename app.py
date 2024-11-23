from flask import Flask, request, jsonify, render_template, send_file
from story_generator import StoryGenerator
from parse_grammar import parse_grammar
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

app = Flask(__name__)

# Configuración de gramática
grammar_file = "cuento.gr"
grammar_rules = parse_grammar(grammar_file)
story_generator = StoryGenerator(grammar_rules)

current_story = None

pdfmetrics.registerFont(TTFont('Bokor', 'static/fonts/Bokor/Bokor-Regular.ttf'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_story():
    global current_story
    try:
        current_story = story_generator.generate_story()
        return jsonify({"success": True, "story": current_story.replace('"', '')})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
