from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def controller():
    return render_template('Controls.html')


if __name__ == '__main__':
    app.run()
