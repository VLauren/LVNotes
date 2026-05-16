import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
#NOTE_PATH = os.path.join(os.path.dirname(__file__), "note.txt")
NOTE_PATH = os.path.join(os.path.dirname(__file__), "data/note.txt")

os.makedirs(os.path.dirname(NOTE_PATH), exist_ok=True)

def read_note():
    if not os.path.exists(NOTE_PATH):
        return ""
    with open(NOTE_PATH, "r", encoding="utf-8") as f:
        return f.read()

def write_note(text):
    with open(NOTE_PATH, "w", encoding="utf-8") as f:
        f.write(text)

@app.route("/")
def index():
    return render_template("index.html", content=read_note())

@app.route("/api/note", methods=["POST"])
def save_note():
    write_note(request.get_data(as_text=True))
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)
