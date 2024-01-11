from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sorteo', methods=['POST'])
def sorteo():

    result = subprocess.run(['python', 'Sorteo.py'], capture_output=True, text=True)


    output = result.stdout

    return render_template('sorteo_resultado.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)




