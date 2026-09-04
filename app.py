from flask import Flask, request, render_template
from HousePrice import calculatePrice

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', result=None)


@app.route('/predecir', methods=['GET', 'POST'])
def predecir():
    result = None
    if request.method == 'POST':
        area = float(request.form['area'])
        result = calculatePrice(area)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)