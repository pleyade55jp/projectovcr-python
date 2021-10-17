from flask import Flask
from flask import Flask, render_template, request
from os import abort

app = Flask(__name__)



 
@app.route('/')
def principal():
    return render_template('principal.html')

@app.route('/Inicio')
def Inicio():
    return render_template('principal.html')


@app.route('/Pagina principal')
def Pagina_principal():
    return render_template('principal.html')

@app.route('/Calculadora')
def Calculadora():
    return render_template('calculadora.html')



@app.route('/Historia')
def Historia():
    return render_template('Historia.html')
   


@app.route('/numero' , methods = ['POST'] )
def calcular_numeros():
        n1 = float(request.form.get("N1"))
        n2 = float(request.form.get("N2"))
        n3 = n1+ n2   
        nombre = n3
        
        return render_template('calculadora.html' , nombre = nombre)
        

 

app.run(debug=True)