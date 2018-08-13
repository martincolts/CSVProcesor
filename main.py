from Strategy.ProcesorCreator import ProcesorCreator
import pandas as pd
import csv

#parameters
pace = 3
fileInput = "testFile.csv"
fileToSave="outFile.csv"

pc = ProcesorCreator()

data = pd.read_csv(fileInput)

procesors = pc.getProcesorList()
print (data.columns.values.tolist()[0])

for index, row in data.iterrows():
    print(row['column1'])

print(procesors[0].value)
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