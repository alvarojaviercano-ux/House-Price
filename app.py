from flask import Flask, request, render_template
from HousePrice import calculatePrice

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', result=None)


@app.route('/predecir', methods=['GET', 'POST'])
def predecir():
    result = None
    error = None

    if request.method == 'POST':
        try:
            area = float(request.form['area'])

            if area <= 0:
                error = "El área debe ser mayor que 0."

            elif area > 1000:
                error = "El área ingresada es demasiado grande."

            else:
                result = calculatePrice(area)

        except ValueError:
            error = "Ingrese un numero válido."

    return render_template(
        'index.html',
        result=result,
        error=error
    )