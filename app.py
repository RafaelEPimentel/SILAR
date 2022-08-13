from flask import Flask, render_template, request, redirect, jsonify
from interface import go_to_point, getcurrentcycle, getX, getY, getZ

app = Flask(__name__)


@app.route('/')
def controller():
    return render_template('Controls.html')

@app.route("/experiment", methods= ['POST'])
def start_experiment():
    x = request.form.getlist('x[]')
    y = request.form.getlist('y[]')
    z = request.form.getlist('z[]')
    zspeed = request.form.getlist('zspeed[]')
    time = request.form.getlist('time[]')
    cycles = int(request.form['Cycles'])
    ceiling = int(request.form['Ceiling'])
    speed = int(request.form['Speed'])
    points = []

    for element in range(len(x)):
        if(float(z[element]) >= float(ceiling)):
            return('Error, point ' + str(element + 1) + ' is not lower than the set ceiling')
        point = [int(x[element]),int(y[element]),int(z[element]), int(time[element]), float(zspeed[element])]
        points.append(point)

    print(points)
    print(cycles)
    print(ceiling)
    go_to_point(points,cycles,ceiling, speed)

    return redirect('/')

@app.route("/getglobals", methods= ['GET'])
def get_globals():
    return jsonify({
        "currentcycle":  getcurrentcycle() + 1,
        "x": getX(),
        "y": getY(),
        "z": getZ(),
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0")
