# make  quick start flask app
from turtle import title
from flask import Flask,render_template,request,json
import requests
app = Flask(__name__)
#URL_FINAL = 'http://127.0.0.1:4000'
URL_FINAL = 'https://apidscpruebassegundo.herokuapp.com'

@app.route('/')
def principal():
    args={
        'titulo':'Home',
    }
    return render_template('indexblog.html',**args)
@app.route('/buscador')    
def buscador():
    #Opciones para sectores
    try:
        r = requests.get(URL_FINAL+'/sector')
        sectores = r.json()
        opt = [valor['NomSec']  for valor in sectores]
        opcionessectoreshtml =" ".join([ "<option value='" + x + "'>Label " + x + "</option>"  for x in opt])
    except:
        opcionessectoreshtml =""
    #Opciones para subsectores
    args={
        'titulo':'Buscador',
        'buscador':'secciones',
        "opcionessectoreshtml":opcionessectoreshtml
    }
    return render_template('buscador.html',**args)
@app.route('/dashboard')    
def dashboard():
    args={
        'titulo':'Dashboard',
        'dashboard':'secciones'
    }
    return render_template('dashboard.html',**args)        
@app.route('/proveedores')    
def proveedores():
    args={
        'titulo':'Proveedores',
        'proveedores':'secciones'
    }
    return render_template('proveedores.html',**args)      
@app.route('/nosotros')    
def nosotros():
    args={
        'titulo':'Nosotros', 
    }
    return render_template('nosotros.html',**args)   
@app.route('/contacto')    
def contacto():
    args={
        'titulo':'Contacto',
    }
    return render_template('contacto.html',**args)  
            
if __name__ == '__main__':
    app.run(debug=True) 

