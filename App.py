from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        grade = request.form["grade"]

        students[name] = grade

    return render_template("index56.html", students=students)

@app.route("/delete/<name>")
def delete(name):
    if name in students:
        del students[name]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
