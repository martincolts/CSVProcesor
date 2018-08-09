class ProcesorContainer:

    def __init__(self, value, procesor):
        self.value=value;
        self.procesor=procesor

    def getValue (self):
        return self.value

    def getProcesor(self):
        return self.procesor
