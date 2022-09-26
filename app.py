from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/eda')
def eda():
    return render_template('eda.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
