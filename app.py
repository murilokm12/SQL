from flask import Flask, redirect, render_template, request, url_for
import sqlite3


app = Flask(__name__)

def init():
   conn = sqlite3.connect('alunix')
   cursor = conn.cursor()

   cursor.execute('CREATE TABLE if not exists alunoos(nome text, email text, idade integer)')   



   conn.commit()  
   conn.close()

init()





@app.route('/cadastro')
def index():
    return render_template('index.html',)



@app.route('/adicionar',methods= ['POST'])

def adicionar():
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']

    conn = sqlite3.connect('alunix')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO alunoos( nome, email, idade)values(?,?,?)',(nome, idade, email))   

    conn.commit()  
    conn.close()

    return redirect(url_for('index'))




app.run(debug=True)