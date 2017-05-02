import statistics
import copy

import parseData


def pruneSmallSets(ratings, minLength = 5):
	"""
		Removes reviewers with less than n reviews from the set
		Modifies the set
	"""
	deletionList = []
	for key,rating in ratings.items():
		if len(rating) < minLength:
			deletionList.append(key)
	for key in deletionList:
		del ratings[key]
	return ratings

def genAverageRatings(ratings):
	"""
		Returns a new table with an average review by each key
		Does not modify the set
	"""
	averageRatings = {}
	for key,rating in ratings.items():
		overallRatings = [x.get("overall") for x in rating]
		avg = sum(overallRatings)/len(rating)
		sd = statistics.stdev(overallRatings)
		averageRatings[key] = {
			"average":avg,
			"sd":sd
		}
		
	return averageRatings

def genPrunedAverages(fileName, groups = ["reviewerID","asin"], pruneMin = 5):
	"""
		Returns list of dictionaries
		One dictionary for each grouping requested
	"""
	fields = copy.copy(groups)
	fields.append("overall")
	groupedPruned = [pruneSmallSets(x,pruneMin) for x in parseData.parseAndGroup(fileName,fields = fields, groupAttributes = groups)]
	averagedGroups = [genAverageRatings(x) for x in groupedPruned]

	return averagedGroups

if __name__ == "__main__":
	genPrunedAverages("rawData/small5Set.json", groups = ["reviewerID"])

