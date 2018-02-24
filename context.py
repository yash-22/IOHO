class Context:
	crimes = {
		'Battery' : ['Baseball bat', 'Hockey stick', 'Beer bottle', 'Broken glass', 'Man', 'Woman'],
		'Knife Violence': ['Knife', 'Dagger', 'Matchete', 'Man', 'Woman'],
		'Gun Violence': ['Assault rifle', 'Handgun', 'Man', 'Woman']
	}

	# finds crime occuring based on objects given
	def find_crime(self, objects):
		# set of objects given
		object_set = set(objects)

		# most likely crime that is occuring
		likely_crime = ""
		# probability that this crime is occuring
		likely_prob = 0.0

		# find overlap of two lists and probablity of crime occuring
		for key, value in self.crimes.items():
			value_set = set(value)
			overlap = object_set & value_set

			crime_prob = float(len(overlap)) / len(object_set) * 100
			if (crime_prob > 0.5 and crime_prob > likely_prob):
				likely_crime = key
				likely_prob = crime_prob

		if (likely_crime == ""):
			return None
		return likely_crime