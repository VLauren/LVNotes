import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
</head>

<body>
    <textarea></textarea>
</body>

"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
