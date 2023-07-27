from flask import Flask, render_template, request, redirect
from entities.student import Student

app = Flask(__name__)

students = []


@app.route("/")
def index():
    return render_template('index.html', students_list=students)


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
        students.append(estudiante)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=8888)
