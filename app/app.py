from flask import Flask
#import redis
import os
#import rq
#from redis import Redis
app = Flask(__name__)

@app.route('/')
def hello_world():
    #r = Redis.from_url('redis://127.0.0.1:6379')
    #queue = rq.Queue( connection=Redis.from_url('redis://127.0.0.1:6379'))
    #job = queue.enqueue(example, 23)
    #job.get_id()
    #r.set('status',0)
    #myCmd = os.popen('FFREPORT=file=./static/out.log:level=32 ffmpeg/ffmpeg -progress url.txt -y -i ./in.mp4  ./static/out.mp4').read()
    #os.system (myCmd)
    #f = open('static/out.log')
    #result = "Result: "
    #for line in f:
    #    result=result+"<br>"+line
    return "<a href='/status'>Status</a>"
@app.route('/status')
def status():
    #r = Redis.from_url('redis://127.0.0.1:6379')
    #status = r.get('status')
    return "<a href='/static/out.mp4'>Result</a>"
if __name__ == '__main__':
    app.run()
#myCmd = os.popen('FFREPORT=file=./static/out.log:level=32 ffmpeg/ffmpeg -y -i ./in.mp4 ./static/out.mp4').read()
#FFREPORT=file=./out.log:level=32 ffmpeg/ffmpeg -y -i ./in.mp4 ./out.mp4