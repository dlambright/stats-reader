from multiprocessing import Process, Queue, Pipe
import time
import datetime
from flask import Flask, jsonify
from threading import Thread
import writeNewGameFiles
from recyclerViewGame import RecyclerViewGame
import json
import getTodaysGames
app = Flask(__name__)


year =  datetime.datetime.now().year
month = datetime.datetime.now().month
day =   datetime.datetime.now().day
    
todaysDate = str(month) + '-' + str(day) + '-' + str(year)

def getTodaysGames():
    gameJson = open("gameData/todaysGames.txt", "r+").read()
    return gameJson


@app.route("/")
def hello():
    return "NNBA Main Page"

@app.route("/todaysGames")
def todaysGames():    
    #todaysGames = "AtlantaHawks 104 DallasMavericks 87;BostonCeltics 115 NewYorkKnicks 94;ChicagoBulls 86 CharlotteHornets 98;DenverNuggets 96 PhoenixSuns 110;HoustonRockets 110 LosAngelesClippers 105;MilwaukeeBucks 104 Philadelphia76ers 88;MinnesotaTimberwolves 97 WashingtonWizards 77;NewOrleansPelicans 102 BrooklynNets 96;OrlandoMagic 90 MiamiHeat 93;PortlandTrailblazers 111 SanAntonioSpurs 95;SacramentoKings 102 MemphisGrizzlies 90;UtahJazz 97 LosAngelesLakers 100"
    
    gameDict = getTodaysGames()

    return gameDict

@app.route("/AtlantaHawks")
def hawksGame():
    toReturn  = open("gameData/AtlantaHawks/" + todaysDate + ".nnbadat", 'r').read()
    return toReturn

@app.route("/DallasMavericks")
def mavericksGame():
    toReturn = open("gameData/DallasMavericks/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn
    
@app.route("/BostonCeltics")
def celticsGame():
    toReturn = open("gameData/BostonCeltics/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/NewYorkKnicks")
def knicksGame():
    toReturn = open("gameData/NewYorkKnicks/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/ChicagoBulls")
def bullsGame():
    toReturn = open("gameData/ChicagoBulls/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/CharlotteHornets")
def hornetsGame():
    toReturn = open("gameData/CharlotteHornets/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/DenverNuggets")
def nuggetsGame():
    toReturn = open("gameData/DenverNuggets/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/PhoenixSuns")
def sunsGame():
    toReturn = open("gameData/PhoenixSuns/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/HoustonRockets")
def rocketsGame():
    toReturn = open("gameData/HoustonRockets/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/LosAngelesClippers")
def clippersGame():
    toReturn = open("gameData/LosAngelesClippers/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MilwaukeeBucks")
def bucksGame():
    toReturn = open("gameData/MilwaukeeBucks/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/Philadelphia76ers")
def seventySixersGame():
    toReturn = open("gameData/Philadelphia76ers/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MinnesotaTimberwolves")
def timberwolvesGame():
    toReturn = open("gameData/MinnesotaTimberwolves/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/WashingtonWizards")
def wizardsGame():
    toReturn = open("gameData/WashingtonWizards/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/NewOrleansPelicans")
def pelicansGame():
    toReturn = open("gameData/NewOrleansPelicans/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/BrooklynNets")
def netsGame():
    toReturn = open("gameData/BrooklynNets/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/OrlandoMagic")
def magicGame():
    toReturn = open("gameData/OrlandoMagic/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MiamiHeat")
def heatGame():
    toReturn = open("gameData/MiamiHeat/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/PortlandTrailblazers")
def blazersGame():
    toReturn = open("gameData/PortlandTrailblazers/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/SanAntonioSpurs")
def spursGame():
    toReturn = open("gameData/SanAntonioSpurs/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/SacramentoKings")
def kingsGame():
    toReturn = open("gameData/SacramentoKings/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MemphisGrizzlies")
def grizzliesGame():
    toReturn = open("gameData/MemphisGrizzlies/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/UtahJazz")
def jazzGame():
    toReturn = open("gameData/UtahJazz/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/LosAngelesLakers")
def lakersGame():
    toReturn = open("gameData/LosAngelesLakers/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/ClevelandCavaliers")
def cavsGame():
    toReturn = open("gameData/ClevelandCavaliers/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/OklahomaCityThunder")
def thunderGame():
    toReturn = open("gameData/OklahomaCityThunder/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/GoldenStateWarriors")
def warriorsGame():
    toReturn = open("gameData/GoldenStateWarriors/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/IndianaPacers")
def pacersGame():
    toReturn = open("gameData/IndianaPacers/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/TorontoRaptors")
def raptorsGame():
    toReturn = open("gameData/TorontoRaptors/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/DetroitPistons")
def pistonsGame():
    toReturn = open("gameData/DetroitPistons/" + todaysDate + ".nnbadat", 'r').read()     
    return toReturn

if __name__ == "__main__":
   
    #thread.start_new_thread(writeNewGameFiles.run())
    app.run(host='0.0.0.0', port=80, debug=True)
    
