from flask import jsonify
import os
from datetime import datetime 
from flask import Flask, json
from flask import render_template, request, redirect, url_for

#from config import Config 
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///posts.db'     #database_file

db = SQLAlchemy(app)

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    #label= db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return "<Title: {}>".format(self.title)


class Person(db.Model):
    id= db.Column(db.String(80),default='1', nullable=False, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    #label= db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return "<Title: {}>".format(self.title)        

# ###   adding api from here now

buses=[
    {"userid": "deepak@gmail.com",
      "Task & status": "hackathon ,COMPLETED"
    }
]

@app.route('/api')
def hello():
    return {'hello': 'Universe'}

'''@app.route('/buses')
def getbuses():
    return jsonify(buses)
    #return render_template("home.html")
'''

'''@app.route('/buses/<int:index>')
def getbus(index):
    bus=buses[index]
    return jsonify(bus)
'''
@app.route('/buses', methods=['POST'])
def addbus():
    bus0= request.form['id']
    bus1= request.form['userid']
    bus2= request.form['carno.']
    #buses.append(bus1)
    #buses.append(bus2)
    new_post = Person(id=bus0,title=bus1,author=bus2)
    db.session.add(new_post)
    db.session.commit()
    #return redirect('/buses')
    books = Person.query.all()
    
    return render_template("completed.html", books=books)


@app.route('/ALLUSERSTASKSTATUS', methods=['GET'])
def adbus():
    books = Person.query.all()
    return render_template("completed.html", books=books)
    
     


'''@app.route('/buses/<int:index>',methods=['DELETE'])
def deletebus(index):
    deleted= buses.pop(index)
    return jsonify(deleted), 200
'''

# ## API added task completed

# ##
try:
    @app.route("/", methods=["GET", "POST"])

    def home():
        if request.method=='POST':
            post_title = request.form['title']
            post_author = request.form['author']
            #post_label = request.form['label']
            new_post = Book(title=post_title, author=post_author)
            db.session.add(new_post)
            db.session.commit()
            return redirect('/')
        else:
            books = Book.query.all()    
            
        return render_template("home.html", books=books)

except my.IntegrityError as e:
    print("invalid or already used data")
    print(e) 

@app.route("/delete", methods=['POST'])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


#new route for to do list is addeded

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/new')
def index1():
    incomplete =Todo.query.filter_by(complete=False).all() 
    complete =Todo.query.filter_by(complete=True).all()
    books = Book.query.all()
    return render_template('index1.html', incomplete=incomplete, complete=complete, books=books )

@app.route('/add', methods=['POST'])
def add():
    todo= Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index1'))

@app.route('/complete/<id>')
def complete(id):
    todo= Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()  

    return redirect(url_for('index1'))


#to do list addded
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'User({self.username}, {self.email})'


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method=='POST':
        
        try:
            post_username = request.form['username']
            post_email = request.form['email']
            post_password = request.form['password']
            new_post = User(username=post_username, email=post_email, password=post_password)
            db.session.add(new_post)
            db.session.commit()
           
        #return redirect('/form')
            booksnew = User.query.all()       
            return render_template("home.html", booksnew=booksnew)
        except Exception as e:
            print('this username or email already exits!!!')
            print(e) 
    else:
        booksnew = User.query.all()    
        
    return render_template("home.html", booksnew=booksnew)


if __name__ == "__main__":
    #app.run(debug=True, port=50001)
    app.run(debug=True)








##3##3#3#33333#3333#333#3##3#33#####3#3#33#3#3#
















'''this is for api and jason'''

