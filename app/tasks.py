import time

def example(seconds):
    myCmd = os.popen('FFREPORT=file=./static/out.log:level=32 ffmpeg/ffmpeg -progress static/progress.txt -y -i ./in.mp4 ./static/out.mp4').read()
    os.system (myCmd)