from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['files']
        f.save('newTest.txt')
        return '200'
    else:
        return 'Upload Page'

#f = 'original_msg.txt'
#fl = {'files': open(f, 'rb')}
#r = requests.post('http://127.0.0.1:5000/upload', files=fl)
