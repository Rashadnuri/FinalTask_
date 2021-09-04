from flask import Flask,render_template,redirect,request,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os 
import random
import urllib.request
from datetime import datetime
import os.path

import pytz



UTC = pytz.utc

IST = pytz.timezone('Asia/Baku')
  
datetime_ist = datetime.now(IST)





app=Flask(__name__)
datafolder=datetime_ist.strftime('%Y-%m-%d')
randomName=random.randint(1,1000)
UPLOAD_FOLDER='static/uploads' +'/'+ datafolder
path= 'static/uploads' +'/'+ datafolder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdb.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "salam"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# os.mkdir(app.config['UPLOAD_FOLDER'])





ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'jfif'])
 
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

db=SQLAlchemy(app)

class File(db.Model):
    file_id=db.Column(db.Integer,primary_key=True)
    file_img=db.Column(db.String(100))

datafolder=datetime_ist.strftime('%Y-%m-%d')




@app.route('/' , methods=['GET', 'POST'])
def add():
    files=File.query.all()
    if request.method=='POST':
        files = request.files.getlist('files[]')
        randomName=random.randint(1,1000)
        path= UPLOAD_FOLDER
        # def isfile_casesensitive(path):
        #  if os.path.isfile(path): return False
        #  directory, filename = os.path.split(path)
        #  return filename in os.listdir(directory)
        path= UPLOAD_FOLDER
        if ():
           isfile=os.path.isdir(path)
           return True
        else :
            path= UPLOAD_FOLDER
            os.makedirs(path)
        for file in files:
         if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           UTC = pytz.utc
           IST = pytz.timezone('Asia/Baku')
           datetime_ist = datetime.now(IST)
           randomName=random.randint(1,1000)
           filename=datetime_ist.strftime('%Y-%m-%d')+'_'+str (randomName)+'.'+filename.split('.')[1]
           path= UPLOAD_FOLDER +'/'+ datafolder+'/'
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         
       
        img=filename
        files=File(
            file_img=filename

        )

        db.session.add(files)
        db.session.commit()
    #select * from news
    return render_template('add.html' , files=files)

# db.create_all()
if __name__=='__main__':
    app.run(debug=True)