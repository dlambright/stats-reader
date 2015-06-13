from multiprocessing import Process, Queue, Pipe
import time
from flask import Flask
app = Flask(__name__)

q = Queue()

global ATL_parent_conn, ATL_child_conn
global DAL_parent_conn, DAL_child_conn
# ATL VS DAL 2-25-2015
def emulate(conn, filePath):
    data = []
 
    for line in open(filePath):
        data.append(line)
    
    for row in data:
        conn.send(row)
        time.sleep(5) 


    

def f(conn):
    print "wut"
    conn.send("Sent from F")

@app.route("/")
def hello():
    return "Main Page"

@app.route("/todaysGames")
def todaysGames():    
    return str(q.get())

@app.route("/ATL")
def hawksGame():
    atlStatsLine = ATL_child_conn.recv()
    return atlStatsLine

@app.route("/DAL")
def mavericksGame():
    dalStatsLine = DAL_child_conn.recv()
    return  dalStatsLine



if __name__ == "__main__":
    
    ATL_parent_conn, ATL_child_conn = Pipe()
    DAL_parent_conn, DAL_child_conn = Pipe()
    
    atl = Process(target=emulate, args=(ATL_parent_conn, "gameData/Atlantahawks/2-25-2015.csv"))
    atl.start()
    
    dal = Process(target=emulate, args=(DAL_parent_conn, "gameData/DallasMavericks/2-25-2015.csv"))
    dal.start()
    

    app.run(host='0.0.0.0', port=80, debug=True)

    emulate()
