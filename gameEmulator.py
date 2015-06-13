from multiprocessing import Process, Queue, Pipe
import time
import csv
from flask import Flask
app = Flask(__name__)

theTimeDoe = 0
q = Queue()

global parent_conn, child_conn

# ATL VS DAL 2-25-2015
def emulate():
    atlFile = open("gameData/AtlantaHawks/2-25-2015.csv", "r")
    atlData = atlFile.read()
    
    with open('gameData/AltantaHawks/2-25-2015.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for line in atlData:
        print line + "\n" 


def f(conn):
    print "wut"
    conn.send("Sent from F")

@app.route("/")
def hello():
    print "hello"
    temp = child_conn.recv()
    return temp

@app.route("/todaysGames")
def todaysGames():    
    return str(q.get())




if __name__ == "__main__":
    
    ##parent_conn, child_conn = Pipe()
    ##p = Process(target=f, args=(parent_conn,))
    ##p.start()

    ##app.run(host='0.0.0.0', port=80, debug=True)

    emulate()
