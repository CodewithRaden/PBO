from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)

class Radiant(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    agent = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    radiants = Radiant.query.all()
    return render_template('index.html', radiants=radiants)  

@app.route('/add', methods=['POST'])
def add():
    agent = request.form['agent']
    new_radiant = Radiant(agent=agent)  
    db.session.add(new_radiant)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    delete_radiant = Radiant.query.get(id)
    db.session.delete(delete_radiant)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    edit_radiant = Radiant.query.get(id)
    return render_template('edit.html', radiant=edit_radiant)  

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    update_radiant = Radiant.query.get(id)
    update_radiant.agent = request.form['agent']  
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)