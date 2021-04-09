from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SECRET_KEY'] = "jfdshfsfgdufvhjhvbfdvhvjv"

db = SQLAlchemy(app)
class users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(10))

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password



@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    # users = users.query.all()
    if request.method == 'POST':
        datas = users.query.all()
        data = request.form.get('firstname') 
        for data in datas:
        # if request.form.get('firstname') == data:
            print("successful")
            return redirect(url_for('homepage'))
                
        else:
            print("Not successful")
            flash("not successful")

    return render_template('login.html')
    

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user = users(request.form.get('firstname'), request.form.get('lastname'), request.form.get('password'))

        db.session.add(user)
        db.session.commit()
        flash('record successfully added.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)