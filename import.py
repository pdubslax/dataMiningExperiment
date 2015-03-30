import csv

with open('spreadsheet.csv', 'r') as f:
	inputArray = [row for row in csv.reader(f.read().splitlines())]

data = []
for index in range(len(inputArray)-1):
	itemDic = {}
	for index2 in range(len(inputArray[0])-1):
		itemDic[inputArray[0][index2+1]]=inputArray[index][index2+1]
	data.append(itemDic)


