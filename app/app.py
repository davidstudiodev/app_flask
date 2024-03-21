from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return '<h1> ¡Hola Mundo desde Flask! ¿Qué tal? </h1>'
    
    cursos = ['PHP', 'Python', 'JavaScript', 'C++']
    
    data = {
        'Titulo': 'Index',
        'Bienvenida': '¡Saludo!',
        'Cursos': cursos,
        'Numero_cursos': len(cursos)
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=65342)