
from flask import Flask, render_template, request

app = Flask(__name__)


# Página principal
@app.route('/')
def index():
    return render_template('index.html')


# Ejercicio 1: Promedio de notas y asistencia
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        if not (10 <= nota1 <= 70 and
                10 <= nota2 <= 70 and
                10 <= nota3 <= 70 and
                0 <= asistencia <= 100):
            return "Los valores ingresados están fuera de rango.", 400

        promedio = round((nota1 + nota2 + nota3) / 3, 2)

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template(
            'ejercicio1.html',
            promedio=promedio,
            estado=estado
        )

    return render_template('ejercicio1.html')


# Ejercicio 2: Nombre con más caracteres
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        nombres = [nombre1, nombre2, nombre3]

        if (not all(nombres) or
                len({nombre.lower() for nombre in nombres}) != 3):
            return "Debes ingresar tres nombres diferentes.", 400

        nombre_mayor = max(nombres, key=len)
        cantidad = len(nombre_mayor)

        return render_template(
            'ejercicio2.html',
            nombre_mayor=nombre_mayor,
            cantidad=cantidad
        )

    return render_template('ejercicio2.html')


# Ejecutar aplicación
if __name__ == '__main__':
    app.run(debug=True)
