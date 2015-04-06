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
    
def experiment1(data):
	#test to see which countries have the highest common profession
	countries = {}
	for index in range(len(data)):
		birthCountry = data[index]["b.country"]
		if birthCountry in countries:
			countries[birthCountry][str(data[index]["prof"])]+=1
			countries[birthCountry]["total"]+=1

		else:
			countries[birthCountry]={"0":0,
									 "1":0,
									 "2":0,
									 "3":0,
									 "4":0,
									 "5":0,
									 "6":0,
									 "total":1}
			countries[birthCountry][str(data[index]["prof"])]+=1

	for key in countries:
		total = countries[key]["total"]
		curMax = 0
		mostcommonprof = 0
		# if float(countries[key]["0"])/total>curMax:
		# 	curMax = float(countries[key]["0"])/total
		# 	mostcommonprof = 0
		if float(countries[key]["1"])/total>curMax:
			curMax = float(countries[key]["0"])/total
			mostcommonprof = 1
		if float(countries[key]["2"])/total>curMax:
			curMax = float(countries[key]["0"])/total
			mostcommonprof = 2
		if float(countries[key]["3"])/total>curMax:
			curMax = float(countries[key]["0"])/total
			mostcommonprof = 3
		if float(countries[key]["4"])/total>curMax:
			curMax = float(countries[key]["0"])/total
			mostcommonprof = 4
		if float(countries[key]["5"])/total>curMax:
			curMax = float(countries[key]["0"])/total
			mostcommonprof = 5
		if float(countries[key]["6"])/total>curMax:
			curMax = float(countries[key]["0"])/total
			mostcommonprof = 6
		if (countries[key]["total"]>100):
			countries[key]["mostCommonProf"]=mostcommonprof
			countries[key]["ratio"]=curMax
			print key + " " + str(mostcommonprof) + ' ' + str(curMax)

	return countries


data = readInput()
ageTimeArray = addAgeCalculation(data)
writeCSV(ageTimeArray)
countries = experiment1(data)





# country of origin -> extention language/culture/religion
# travel time over course of life / birth death points
# look at moving countries over course of life by profession
# what countires are famous for professions
# find a country match -> gdp -> 
# 
# 
# 
 





