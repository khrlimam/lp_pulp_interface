from flask import (
    Flask,
    jsonify,
    render_template,
    request)

app = Flask("Python Simplex")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=['POST'])
def process():
    data = {
        'title': request.form['title'],
        'constraints': request.form['constraints'],
        'objective': request.form['objective'],
        'variables': request.form['variables'],
        'z': request.form['z']
    };
    return jsonify(data)


@app.route("/help")
def help():
    return render_template("help.html")
