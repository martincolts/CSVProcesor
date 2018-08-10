from Procesors.AverageProcesor import  AverageProcesor
from Procesors.MostRepeatedProcesor import MostRepeatedProcesor
from Procesors.GetLastProcesor import GetLastProcesor
from Strategy.ProcesorCreator import ProcesorCreator
import pandas as pd

pc = ProcesorCreator()

procesors = pc.getProcesorList()

print(procesors)


