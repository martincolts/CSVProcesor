import json
from Strategy.ProcesorFounder import ProcesorFounder
from Strategy.ProcesorContainer import  ProcesorContainer

class ProcesorCreator:

    def __init__(self):
        self.procesorFounder=ProcesorFounder()
        self.procesorList=[]

    def readJson(self):
        with open("./config.json") as file:
            config = json.load(file)
        values = config["config"]
        for value in values:
            self.createProcesorList(value)

    def createProcesorList(self, value):
        type=value["id"]
        procesor=self.procesorFounder.getProcesor(type)
        pc = ProcesorContainer(type,procesor)
        self.procesorList.append(pc)

    def getProcesorList(self):
        self.readJson()
        return self.procesorList



