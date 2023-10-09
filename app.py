from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resultado', methods= ['POST', 'GET'])
def submission():
     if request.method == 'POST':
        
        # Obtenemos el valor del input
        entrada = request.form.get("fibo")
        
        # Validamos si el input está vacío
        if entrada == '':
            return render_template('resultado.html', resultado = str(entrada))

        n = int(entrada)
        # Validamos el valor de n


        if n == 0:
            return render_template('resultado.html', resultado = str(n))
        

        # Manejo de los casos base, dos primeros terminos de la serie
        if n in {0, 1}:
            return render_template('resultado.html', resultado = str(n))

        # Calculo de los siguientes casos, con modelo iterativo
        anterior, num_fib = 0, 1
        for _ in range(2, n + 1):
            # Computar el siguiente numero fibonacci, recordando el anterior
            anterior, num_fib = num_fib, anterior + num_fib

        
        return render_template('resultado.html', resultado = str(num_fib))
     
if __name__ == "__main__":
    app.run(debug=True)