from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
 
 
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:einstein@localhost/webmusic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#membuat model tabel untuk web music database
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    
 
 
    def __init__(self, name):
 
        self.name = name
        

 
 
 
 
 
#index route
#query on all genre data
@app.route('/')
def Index():
    all_data = Genre.query.all()
 
    return render_template("index.html", genre = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        
 
 
        my_data = Genre(name)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Genre Inserted Successfully")
 
        return redirect(url_for('Index'))
 
 
#update route untuk update genre
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Genre.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        
 
        db.session.commit()
        flash("Genre Updated Successfully")
 
        return redirect(url_for('Index'))
 
 
 
 
#route untuk menghapus genre
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Genre.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Genre Deleted Successfully")
 
    return redirect(url_for('Index'))
 
 
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)
 