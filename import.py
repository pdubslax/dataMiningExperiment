import csv
import ast
from urllib2 import Request, urlopen, URLError


def readInput():
	with open('spreadsheet.csv', 'r') as f:
		inputArray = [row for row in csv.reader(f.read().splitlines())]

	data = []
	for index in range(len(inputArray)-1):
		itemDic = {}
		for index2 in range(len(inputArray[0])-1):
			itemDic[inputArray[0][index2+1]]=inputArray[index+1][index2+1]
		data.append(itemDic)
	return data

def addAgeCalculation(data):
	ageTimeArray = []
	for index in range(len(data)):
		data[index]["age"]= int(data[index]["DYear"])-int(data[index]["BYear"])
		add = {'age':data[index]["age"],
			   'year':data[index]["BYear"]}
		ageTimeArray.append(add)
		# print str(int(data[index]["DYear"])-int(data[index]["BYear"])) + " " + str(int(data[index]["DYear"])) + " " + str(int(data[index]["BYear"]))
	return ageTimeArray

def writeCSV(array):
	with open('test.csv', 'wb') as csvfile:
		for index in range(len(array)):
			fieldnames = ['age', 'year of birth']
			spamwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
			spamwriter.writerow({'age':array[index]["age"] , 'year of birth':array[index]["year"]})
    
data = readInput()
ageTimeArray = addAgeCalculation(data)
writeCSV(ageTimeArray)





# country of origin -> extention language/culture/religion
# travel time over course of life / birth death points
# look at moving countries over course of life by profession
# what countires are famous for professions
# find a country match -> gdp -> 
# 
# 
# 
 





