# Count of same time projects
# sort by start date
# start a
# start b
# start c

# iterate over sorted by start array
if current_end_date >= start_date: project was running at the same time
This is a dream that might dies because we can't find an efficient algorithm

temp_df = pd.read_csv('KS_train_data.csv', delimiter=',')
temp_df[['created_at','deadline','launched_at']] = df[['created_at','deadline','launched_at']].apply(pd.to_datetime)


temp_df['overlapping_time_count'] = 0
for proj in range(len(temp_df)):
	for compProj in range(proj+1,len(temp_df)):
		if temp_df.at[proj,'deadline'] > temp_df.at[compProj, 'launched_at'] and temp_df.at[proj,'launched_at'] < temp_df.at[compProj,'deadline']:
			temp_df['overlapping_time_count'].iloc[proj] += 1
			temp_df['overlapping_time_count'].iloc[compProj] += 1


temp_df[['created_at','deadline','launched_at', 'overlapping_time_count']].head(10)
temp_df[['created_at', 'deadline']] = np.log10(temp_df[['created_at', 'deadline']])

temp_df.head(10000).plot.scatter(x='created_at', y='deadline')