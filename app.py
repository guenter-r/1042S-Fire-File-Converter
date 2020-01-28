from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from qi1042 import *
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
   return render_template('home.html')


## Upload through webpage
@app.route('/fire', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return('<body style="background:#343a40"><img src="./static/404.png" style="border-radius:30px; margin: 40px 50px;"></body>')
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return('<body style="background:#343a40"><img src="./static/404.png" style="border-radius:30px; margin: 40px 50px;"></body>')
            
        file.save(secure_filename(file.filename))
        file_name = secure_filename(file.filename)
        
      # Bug handling the "file" which is an object :
      # create dict, array for rendering
        q_records,keys = import_split_1042(file_name)
        return render_template('q_records.html', q_records = q_records, keys = keys)

## CURL request: Post a txt file
@app.route('/get_html', methods = ['GET', 'POST'])
def return_html():
    if request.method == 'POST':
       file = request.get_data()
       # file (byte) must be converted in order to allow process through function below!
       file = file.decode()
       # create physical file for split
       with open('data.txt','w+') as d:
           d.write(str(file))
       # create dict, array for rendering
       q_records,keys = import_split_1042('data.txt')
       html = render_template('q_records.html', q_records = q_records, keys = keys)
       with open('q_records.html','w+') as h:
           h.write(str(html))
       os.remove('data.txt')
       return html
    if request.method == 'GET':
        return('<body style="background:#343a40"><img src="./static/404.png" style="border-radius:30px; margin: 40px 50px;"></body>')


if __name__ == '__main__':
   app.run(debug = False, host='0.0.0.0',port="1042")
