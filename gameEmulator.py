from multiprocessing import Process, Queue, Pipe
import time
#import multiprocessing_import_worker

from flask import Flask
app = Flask(__name__)

theTimeDoe = 0
q = Queue()

global parent_conn, child_conn


def emulate(q):
    print "emulate"
    global theTimeDoe
    for x in range(0,60):
        theTimeDoe = x
        q = Queue()
        q.put(theTimeDoe)
        time.sleep(5)

def f():
    print "wut"
    child_conn.send("dindu nuffin")

@app.route("/")
def hello():
    print "hello"
    temp = child_conn.recv()
    print temp
    return temp

@app.route("/todaysGames")
def todaysGames():    
    return str(q.get())




if __name__ == "__main__":
    
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=())
    p.start()
    #print parent_conn.recv()   # prints "[42, None, 'hello']"
    p.join()

    app.run(host='0.0.0.0', port=80, debug=True)

