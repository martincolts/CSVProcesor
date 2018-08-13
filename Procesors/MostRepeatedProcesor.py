from Procesors.ProcesorAbs import Procesor
import numpy as np

class MostRepeatedProcesor(Procesor):

    def __init__(self,type):
        Procesor.__init__(self,type)
        self.values=[]

    def process (self):
        counts = np.bincount(self.values)
        result = np.argmax(counts)
        self.values = []
        return result



