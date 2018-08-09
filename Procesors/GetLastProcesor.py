from ProcesorAbs import Procesor
import numpy as np

class GetLastProcesor(Procesor):

    def __init__(self,type):
        Procesor.__init__(self,type)
        self.values=[]

    def process (self):
        return self.values[-1]

