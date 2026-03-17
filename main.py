from flask import Flask, render_template, request
from generate.generate import generates

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    lessons = []
    if request.method == "POST":
        for _ in range(3):
            lessons.append(generates(request.form))
    return render_template("index.html", lessons=lessons)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)