from Strategy.ProcesorCreator import ProcesorCreator
import pandas as pd

import csv

#parameters
pace = 70
fileInput = "file5_25.csv"
fileToSave="f5_25.csv"


print ("Started executed with params:")
print("Pace: ", pace)
print("File in: ", fileInput)
print("File out: ", fileToSave)

pc = ProcesorCreator()

data = pd.read_csv(fileInput)
procesors = pc.getProcesorList()

with open(fileToSave, 'w', newline='') as outFile:
    writeFile = csv.writer(outFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for index, row in data.iterrows():
        for procesor in procesors:
            procesor.getProcesor().addValue(row[procesor.value])
        if (index+1) % pace == 0 and index != 0:
            row = []
            for procesor in procesors:
                row.append(procesor.getProcesor().process())
            writeFile.writerow(row)
            row = []
    row = []
    for procesor in procesors:
        row.append(procesor.getProcesor().process())
    writeFile.writerow(row)
    row = []