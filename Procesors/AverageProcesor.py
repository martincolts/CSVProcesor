from ProcesorAbs import Procesor
import numpy as np

class AverageProcesor(Procesor):

    def __init__(self,type):
        Procesor.__init__(self,type)
        self.values=[]

    def process (self):
        return int(np.mean(self.values, axis=0))
