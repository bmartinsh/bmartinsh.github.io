from flask import Flask, render_template
from flask_socketio import SocketIO

app  = Flask(__name__)
app.config['SECRET_KEY']='bruh'
socket=SocketIO(app)
somelist = ['A','B','C']
i=0

@app.route('/')
def main():
    return render_template('index.html')

@socket.on('message')
def handlemsg(msg):
    global i
    if i<len(somelist):
        socket.send(somelist[i])
        i+=1

if __name__ == '__main__':
    #app.run(app)
    app.run(debug=True)
