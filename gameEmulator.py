from multiprocessing import Process, Queue, Pipe
import time
from flask import Flask
from threading import Thread
import writeNewGameFiles
import thread
app = Flask(__name__)

q = Queue()

global ATL_parent_conn, ATL_child_conn
global DAL_parent_conn, DAL_child_conn
global atlStats


# ATL VS DAL 2-25-2015
def emulate(filePath):
    global atlStats
    data = []
 
    for line in open(filePath):
        data.append(line)
    
    for row in data:
        atlStats = row #data[len(data)-1]
        #conn.send(data[len(data)-1])
        print row
        time.sleep(.5) 
    

def f(conn):
    print "wut"
    conn.send("Sent from F")

@app.route("/")
def hello():
    return "Main Page"

@app.route("/todaysGames")
def todaysGames():    
    todaysGames = "AtlantaHawks 104;DallasMavericks 87;BostonCeltics 115;NewYorkKnicks 94;ChicagoBulls 86;CharlotteHornets 98;DenverNuggets 96;PhoenixSuns 110;HoustonRockets 110;LosAngelesClippers 105;MilwaukeeBucks 104;Philadelphia76ers 88;MinnesotaTimberwolves 97;WashingtonWizards 77;NewOrleansPelicans 102;BrooklynNets 96;OrlandoMagic 90;MiamiHeat 93;PortlandTrailblazers 111;SanAntonioSpurs 95;SacramentoKings 102;MemphisGrizzlies 90;UtahJazz 97;LosAngelesLakers 100"
    return todaysGames

@app.route("/AtlantaHawks")
def hawksGame():
    toReturn  = open("gameData/AtlantaHawks/2-25-2015-today.csv", 'r').read()
    return toReturn

@app.route("/DallasMavericks")
def mavericksGame():
    toReturn = open("gameData/DallasMavericks/2-25-2015-today.csv", 'r').read()     
    return toReturn
    
@app.route("/BostonCeltics")
def celticsGame():
    toReturn = open("gameData/BostonCeltics/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/NewYorkKnicks")
def knicksGame():
    toReturn = open("gameData/NewYorkKnicks/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/ChicagoBulls")
def bullsGame():
    toReturn = open("gameData/ChicagoBulls/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/CharlotteHornets")
def hornetsGame():
    toReturn = open("gameData/CharlotteHornets/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/DenverNuggets")
def nuggetsGame():
    toReturn = open("gameData/DenverNuggets/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/PhoenixSuns")
def sunsGame():
    toReturn = open("gameData/PhoenixSuns/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/HoustonRockets")
def rocketsGame():
    toReturn = open("gameData/HoustonRockets/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/LosAngelesClippers")
def clippersGame():
    toReturn = open("gameData/LosAngelesClippers/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/MilwaukeeBucks")
def bucksGame():
    toReturn = open("gameData/MilwaukeeBucks/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/Philadelphia76ers")
def seventySixersGame():
    toReturn = open("gameData/Philadelphia76ers/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/MinnesotaTimberwolves")
def timberwolvesGame():
    toReturn = open("gameData/MinnesotaTimberwolves/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/WashingtonWizards")
def wizardsGame():
    toReturn = open("gameData/WashingtonWizards/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/NewOrleansPelicans")
def pelicansGame():
    toReturn = open("gameData/NewOrleansPelicans/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/BrooklynNets")
def netsGame():
    toReturn = open("gameData/BrooklynNets/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/OrlandoMagic")
def magicGame():
    toReturn = open("gameData/OrlandoMagic/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/MiamiHeat")
def heatGame():
    toReturn = open("gameData/MiamiHeat/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/PortlandTrailblazers")
def blazersGame():
    toReturn = open("gameData/PortlandTrailblazers/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/SanAntonioSpurs")
def spursGame():
    toReturn = open("gameData/SanAntonioSpurs/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/SacramentoKings")
def kingsGame():
    toReturn = open("gameData/SacramentoKings/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/MemphisGrizzlies")
def grizzliesGame():
    toReturn = open("gameData/MemphisGrizzlies/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/UtahJazz")
def jazzGame():
    toReturn = open("gameData/UtahJazz/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/LosAngelesLakers")
def lakersGame():
    toReturn = open("gameData/LosAngelesLakers/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/ClevelandCavaliers")
def cavsGame():
    toReturn = open("gameData/ClevelandCavaliers/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/OklahomaCityThunder")
def thunderGame():
    toReturn = open("gameData/OklahomaCityThunder/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/GoldenStateWarriors")
def warriorsGame():
    toReturn = open("gameData/GoldenStateWarriors/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/IndianaPacers")
def pacersGame():
    toReturn = open("gameData/IndianaPacers/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/TorontoRaptors")
def raptorsGame():
    toReturn = open("gameData/TorontoRaptors/2-25-2015-today.csv", 'r').read()     
    return toReturn

@app.route("/DetroitPistons")
def pistonsGame():
    toReturn = open("gameData/DetroitPistons/2-25-2015-today.csv", 'r').read()     
    return toReturn

if __name__ == "__main__":
   
    #thread.start_new_thread(writeNewGameFiles.run())
    app.run(host='0.0.0.0', port=80, debug=True)
    
