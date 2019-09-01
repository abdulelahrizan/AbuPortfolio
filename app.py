from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/application')
def application():
    return render_template('app.html')


if __name__ == '__main__':
    app.run(debug=True)