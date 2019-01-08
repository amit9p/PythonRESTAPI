from flask import Flask
import boto3, botocore

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/1")
def hello1():
    return "Hello World 1 !"


@app.route("/2")
def hello2():
    return "Hello World 2!"

@app.route('/msg/<msg>')
def display_msg(msg):
    msg = msg.replace(".","/")
    return msg



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
    
    
    


s3 = boto3.resource('s3')
s3obj = s3.Object( 'mybucket', 'myfile')

filedata= s3obj.get()["Body"].read()


print (filedata.decode('utf8').count('\n')-1)