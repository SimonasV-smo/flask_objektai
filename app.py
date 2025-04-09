from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('stats.html')

@app.route('/add')
def add():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)