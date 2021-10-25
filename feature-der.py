def deriveFeatures(dataframe): # Call this to derive features :)
	#convert dates to datetime format
	dataframe[['created_at', 'deadline', 'launched_at']] = dataframe[['created_at', 'deadline', 'launched_at']].apply(pd.to_datetime,unit='s')

	#derive duration
	dataframe['duration'] = (dataframe['deadline'] - dataframe['launched_at'])

	#derive word count for name & blurb
	dataframe['word_count'] = get_word_count(dataframe['blurb'])
	dataframe['name_count'] = get_word_count(dataframe['name'])	

	#calculate same day launches
	get_same_day_launced(dataframe)

	#get readablity of name and blurb
	# get_readablity(dataframe)



def get_word_count(blurb_list):
    word_list =[]
    for blurb_index in blurb_list:
        word_list.append(len(str(blurb_index).split()))
    return word_list


def get_same_day_launced(dataframe): #calculate how many prjects were launched on the same day
	for key in ['launched_at', 'created_at', 'deadline']: 
		dataframe[key] = dataframe[key].dt.date
	
	possibleDates = dataframe['launched_at'].unique()
	dataframe['same_day_projects'] = 0
	for date in possibleDates:
		sameDayProj = dataframe.loc[dataframe['launched_at']==date]
		dataframe['same_day_projects'].loc[dataframe['launched_at']==date] = len(sameDayProj)	


def get_readablity(dataframe): #TODO something doesn't work, it gives the same redablity to everything
	import textstat
	from textstat import flesch_reading_ease

	# for index, row in dataframe.iterrows():
	# 	t=row['blurb'];
	# 	text=str(t)

	for copy in ['blurb', 'name']:
		read = []
		for i in dataframe[copy].head(10):
			print(i)
			# read.append(textstat.flesch_reading_ease(str(i)))
			dataframe[copy+'_readability'] = textstat.flesch_reading_ease(str(i))