from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)

class Radiant(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    agent = db.Column(db.String(120), nullable=False)
    roles = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    radiants = Radiant.query.all()
    return render_template('index.html', radiants=radiants)

@app.route('/add_agent', methods=['GET'])
def add_agent():
    roles = ['Duelist', 'Controller', 'Initiator', 'Sentinel']
    return render_template('add_agent.html', roles=roles)

@app.route('/add', methods=['POST'])
def add():
    agent = request.form['agent']
    roles = request.form['roles']  
    new_radiant = Radiant(agent=agent, roles=roles)
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
    roles = ['Duelist', 'Controller', 'Initiator', 'Sentinel']
    return render_template('edit.html', radiant=edit_radiant, roles=roles)
 

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    update_radiant = Radiant.query.get(id)
    update_radiant.agent = request.form['agent']
    update_radiant.roles = request.form['roles']  
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)