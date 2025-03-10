from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie/<filename>')
def movie(filename):
    return send_from_directory(directory='.', path=filename)

if __name__ == '__main__':
    app.run(debug=True)