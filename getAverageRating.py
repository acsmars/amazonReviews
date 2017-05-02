import parseData

def pruneSmallSets(ratings, minReviews = 5):
	"""
		Removes reviewers with less than n reviews from the set
		Modifies the set
	"""
	deletionList = []
	for key,rating in ratings.items():
		if len(rating) < minReviews:
			deletionList.append(key)
	for key in deletionList:
		del ratings[key]

def genAverageRatings(ratings):
	"""
		Returns a new table with an average review by each user
		Does not modify the set
	"""
	averageRatings = {}
	for key,rating in userRatings.items():
		averageRatings[key] = sum([x.get("overall") for x in rating])/len(rating)
	return averageRatings

if __name__ == "__main__":
	userRatings = parseData.parseAndGroup("rawData/small5Set.json",fields = ["overall","reviewerID"])

	pruneSmallSets(userRatings)
	averageRatings = genAverageRatings(userRatings)

	print(averageRatings)