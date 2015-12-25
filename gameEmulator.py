from multiprocessing import Process, Queue, Pipe
import time
import datetime
from flask import Flask, jsonify
from threading import Thread
import writeNewGameFiles
from recyclerViewGame import RecyclerViewGame
import json
import getTodaysGames
import os
app = Flask(__name__)

def getTodaysDate():
    year =  datetime.datetime.now().year
    month = datetime.datetime.now().month
    day =   datetime.datetime.now().day
    
    return str(month) + '-' + str(day) + '-' + str(year)

def getTodaysGames():
    gameJson = open("gameData/todaysGames.txt", "r+").read()
    return gameJson


@app.route("/")
def hello():
    return "NNBA Main Page"

@app.route("/todaysGames")
def todaysGames():    
    gameDict = getTodaysGames()
    return gameDict

@app.route("/AtlantaHawks")
def hawksGame():
    toReturn = "{}"
    if os.path.exists("gameData/AtlantaHawks/" + str(getTodaysDate()) + ".nnbadat"):    
        toReturn  = open("gameData/AtlantaHawks/" + str(getTodaysDate()) + ".nnbadat", 'r').read()
    return toReturn

@app.route("/DallasMavericks")
def mavericksGame():
    toReturn = open("gameData/DallasMavericks/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn
    
@app.route("/BostonCeltics")
def celticsGame():
    toReturn = open("gameData/BostonCeltics/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/NewYorkKnicks")
def knicksGame():
    toReturn = open("gameData/NewYorkKnicks/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/ChicagoBulls")
def bullsGame():
    toReturn = open("gameData/ChicagoBulls/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/CharlotteHornets")
def hornetsGame():
    toReturn = open("gameData/CharlotteHornets/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/DenverNuggets")
def nuggetsGame():
    toReturn = open("gameData/DenverNuggets/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/PhoenixSuns")
def sunsGame():
    toReturn = open("gameData/PhoenixSuns/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/HoustonRockets")
def rocketsGame():
    toReturn = open("gameData/HoustonRockets/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/LosAngelesClippers")
def clippersGame():
    toReturn = open("gameData/LosAngelesClippers/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MilwaukeeBucks")
def bucksGame():
    toReturn = open("gameData/MilwaukeeBucks/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/Philadelphia76ers")
def seventySixersGame():
    toReturn = open("gameData/Philadelphia76ers/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MinnesotaTimberwolves")
def timberwolvesGame():
    toReturn = open("gameData/MinnesotaTimberwolves/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/WashingtonWizards")
def wizardsGame():
    toReturn = open("gameData/WashingtonWizards/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/NewOrleansPelicans")
def pelicansGame():
    toReturn = open("gameData/NewOrleansPelicans/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/BrooklynNets")
def netsGame():
    toReturn = open("gameData/BrooklynNets/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/OrlandoMagic")
def magicGame():
    toReturn = open("gameData/OrlandoMagic/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MiamiHeat")
def heatGame():
    toReturn = open("gameData/MiamiHeat/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/PortlandTrailblazers")
def blazersGame():
    toReturn = open("gameData/PortlandTrailblazers/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/SanAntonioSpurs")
def spursGame():
    toReturn = open("gameData/SanAntonioSpurs/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/SacramentoKings")
def kingsGame():
    toReturn = open("gameData/SacramentoKings/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/MemphisGrizzlies")
def grizzliesGame():
    toReturn = open("gameData/MemphisGrizzlies/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/UtahJazz")
def jazzGame():
    toReturn = open("gameData/UtahJazz/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/LosAngelesLakers")
def lakersGame():
    toReturn = "{}"
    if os.path.exists("gameData/LosAngelesLakers/" + str(getTodaysDate()) + ".nnbadat"):
        toReturn = open("gameData/LosAngelesLakers/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/ClevelandCavaliers")
def cavsGame():
    toReturn = open("gameData/ClevelandCavaliers/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/OklahomaCityThunder")
def thunderGame():
    toReturn = "{}"
    if os.path.exists("gameData/OklahomaCityThunder/" + str(getTodaysDate()) + ".nnbadat"):
        toReturn = open("gameData/OklahomaCityThunder/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/GoldenStateWarriors")
def warriorsGame():
    toReturn = open("gameData/GoldenStateWarriors/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/IndianaPacers")
def pacersGame():
    toReturn = open("gameData/IndianaPacers/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/TorontoRaptors")
def raptorsGame():
    toReturn = open("gameData/TorontoRaptors/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

@app.route("/DetroitPistons")
def pistonsGame():
    toReturn = open("gameData/DetroitPistons/" + str(getTodaysDate()) + ".nnbadat", 'r').read()     
    return toReturn

if __name__ == "__main__":
   
    #thread.start_new_thread(writeNewGameFiles.run())
    app.run(host='0.0.0.0', port=80, debug=True)
    
