from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', title="EK Machine Error System", year="2025")

if __name__ == '__main__':
    app.run(debug=True)