from flask import Flask, render_template, request, redirect
from entities.student import Student
from entities.professor import Professor

app = Flask(__name__)

students_list = []
professors_list = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/students")
def students():
    return render_template('students.html', students_list=students_list)


@app.route("/professors")
def professors():
    return render_template('professors.html', professors_list=professors_list)


@app.route("/new_student", methods=['GET', 'POST'])
def new_student():
    if request.method == "GET":
        print("Método GET")
        return render_template('new_student.html')
    elif request.method == "POST":
        estudiante = Student(
            request.form["nombre"],
            request.form["apellido_paterno"],
            request.form["apellido_materno"],
            request.form["fecha_nacimiento"],
            request.form["matricula"]
        )
        students_list.append(estudiante)
        return redirect('/students')


if __name__ == '__main__':
    app.run(debug=True, port=8888)
