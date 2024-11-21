import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from story_generator import StoryGenerator
from parse_grammar import parse_grammar

# Función para cargar la gramática y generar el cuento
def generate_story():
    try:
        global story_generator
        story = story_generator.generate_story()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, story)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema al generar el cuento:\n{e}")

# Función para guardar el cuento
def save_story():
    try:
        story = text_area.get(1.0, tk.END).strip()
        if not story:
            messagebox.showwarning("Advertencia", "No hay ningún cuento para guardar.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt")],
            title="Guardar cuento"
        )
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(story)
            messagebox.showinfo("Éxito", "Cuento guardado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problema al guardar el cuento:\n{e}")

# Configuración de la gramática y generador
try:
    grammar_file = "cuento.gr"
    grammar_rules = parse_grammar(grammar_file)
    story_generator = StoryGenerator(grammar_rules)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar la gramática:\n{e}")
    story_generator = None

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Cuentos")
root.geometry("800x600")
root.configure(bg="#f4f4f9")

# Título de la aplicación
title_label = tk.Label(
    root,
    text="Generador de Cuentos Mágicos",
    font=("Helvetica", 24, "bold"),
    bg="#f4f4f9",
    fg="#333"
)
title_label.pack(pady=20)

# Área de texto para mostrar el cuento generado
text_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 14),
    width=80,
    height=20,
    bg="#ffffff",
    fg="#333",
    relief=tk.FLAT,
    padx=10,
    pady=10
)
text_area.pack(pady=10)

# Botones para generar y guardar cuentos
button_frame = tk.Frame(root, bg="#f4f4f9")
button_frame.pack(pady=10)

generate_button = tk.Button(
    button_frame,
    text="Generar Cuento",
    font=("Helvetica", 14),
    bg="#007acc",
    fg="#ffffff",
    activebackground="#005b99",
    activeforeground="#ffffff",
    relief=tk.FLAT,
    command=generate_story
)
generate_button.grid(row=0, column=0, padx=10)

save_button = tk.Button(
    button_frame,
    text="Guardar Cuento",
    font=("Helvetica", 14),
    bg="#28a745",
    fg="#ffffff",
    activebackground="#1e7e34",
    activeforeground="#ffffff",
    relief=tk.FLAT,
    command=save_story
)
save_button.grid(row=0, column=1, padx=10)

# Iniciar la aplicación
root.mainloop()
