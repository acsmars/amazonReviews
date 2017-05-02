import json

def parseJson(fileName, fields = [], prune = []):
	"""
		Takes a filename and reads line deliniated json from the file
		If field keys are supplied, only those attributes will be loaded
		If prune keys are supplied, those attributes will not be loaded
	"""
	data = []
	with open(fileName, "r") as jsonFile:
		for i,line in enumerate(jsonFile):
			if not (i % 100000):
				print("Processing line {}".format(i))
			try:
				entry = json.loads(line)
				if fields:
					x = {}
					for key in fields:
						x[key] = entry.get(key)
					entry = x
				if prune:
					for key in prune:
						del entry[key]
				data.append(entry)
			except Exception as e:
				print("Error on line {} of data file: {}".format(i,e))
	return data

def groupByReviewer(data, removeID = True):
	"""
		Takes parsed data list and creates a table with keys by reviewerName 
	"""
	userTable = {}
	for review in data:
		reviewer = review.get("reviewerID")
		if not userTable.get(reviewer):
			userTable[reviewer] = []
		if removeID:
			del review["reviewerID"]
		userTable.get(reviewer).append(review)
	return userTable

def parseAndGroup(fileName, fields = [], prune = []):
	"""
		Wrapper for parseJson and groupByReviewer
	"""
	data = parseJson(fileName = fileName, fields = fields, prune = prune)
	userReviews = groupByReviewer(data)
	del data
	return userReviews

if __name__ == "__main__":
	fields = ["asin","reviewerName","overall"]
	userReviews = parseAndGroup("rawData/small5Set.json",prune = ["reviewText"])
	for key,user in userReviews.items():
		print(user)
