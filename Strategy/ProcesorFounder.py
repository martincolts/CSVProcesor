from Procesors.GetLastProcesor import GetLastProcesor
from Procesors.MostRepeatedProcesor import MostRepeatedProcesor
from Procesors.AverageProcesor import AverageProcesor


class ProcesorFounder:

    def __init__(self):
        pass

    def getProcesor(self, value):
        if  value == "AVERAGE":
            return AverageProcesor("AVERAGE")
        elif value == "REPEAT":
            return MostRepeatedProcesor("REPEAT")
        else:
            return GetLastProcesor("LAST")

