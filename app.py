from flask import Flask
import boto3, botocore

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ping")
def pinging():
    return "Pinged Successfully !"


@app.route('/msg/<msg>')
def display_msg(msg):
    msg = msg.replace(".","/")
    return msg


@app.route('/avro/<s3bucket>/<s3Key>')            
def avroCount(s3bucket,s3Key):                    
    s3Key = s3Key.replace(".","/")                
    s3 = boto3.resource('s3')                     
    s3obj = s3.Object( s3bucket, s3Key)           
    filedata= s3obj.get()["Body"].read()          
    count = filedata.decode('utf8').count('\n')-1 
    return count                                  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
