from flask import Flask, render_template, request, redirect
from interface import go_to_point

app = Flask(__name__)


@app.route('/')
def controller():
    return render_template('Controls.html')

@app.route("/experiment", methods= ['POST'])
def start_experiment():
    x = request.form.getlist('x[]')
    y = request.form.getlist('y[]')
    z = request.form.getlist('z[]')
    cycles = int(request.form['Cycles'])
    points = []

    for element in range(len(x)):
        point = [int(x[element]),int(y[element]),int(z[element])]
        points.append(point)

    print(points)
    print(cycles)
    go_to_point(points,cycles)


    return redirect('/')

if __name__ == '__main__':
    app.run()
