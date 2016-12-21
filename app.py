from flask import (
    Flask,
    jsonify,
    render_template,
    request)
from lp.solver import Solver as simplex
import pulp
from lp.NoSolutionException import NoSolutionException

app = Flask("Python Simplex")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=['POST'])
def process():
    # dirty code and magic happens here
    # what important for now the code works, so i got A grade 3:)
    variables = request.form['variables'].split(',')
    constraints = request.form['constraints'].split(',')
    objective = request.form['objective']
    title = request.form['title']
    z = int(request.form['z'])
    what_to_achieve = (pulp.LpMinimize, pulp.LpMaximize)[z]
    # apply input as lp variable
    for var in variables:
        exec ("{} = pulp.LpVariable('{}', lowBound=0, cat=pulp.LpInteger)".format(var, var))
    holy_problem = simplex(title, what_to_achieve)
    holy_problem.constraints(list=[eval(constraint) for constraint in constraints])
    holy_problem.objective(eval(objective))
    try:
        holy_problem.any_solution()
        response = {
            'varsAndSolution': [{'name': var.name, 'val': var.value()} for var in holy_problem.__prob__.variables()],
            'z': holy_problem.__prob__.objective.value(),
            'execTime': holy_problem.__prob__.solutionTime
        }
    except NoSolutionException:
        response = {
            'error': True,
            'message': NoSolutionException.message
        }
    return jsonify(response)


@app.route("/help")
def help():
    return render_template("help.html")
