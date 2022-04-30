# make  quick start flask app
from turtle import title
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def principal():
    args={
        'titulo':'Home',
    }
    return render_template('indexblog.html',**args)
@app.route('/buscador')    
def buscador():
    args={
        'titulo':'Buscador',
        'buscador':'secciones'
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

