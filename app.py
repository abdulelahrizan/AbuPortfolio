from portfoliodb import data, Design
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('base.html', data=data, Design=Design)


if __name__ == '__main__':
    app.run(debug=True)
