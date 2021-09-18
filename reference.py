
#import both csv files and cast them to lists
af = pd.read_excel('applications-form.xlsx', sheet_name='Sheet1', usecols=['Primary Type of Research'])
af = af.values.tolist()

rf = pd.read_excel('reviewers-form.xlsx', sheet_name='LOI Reviewers', usecols=['Type of Research Expertise'])
rf = rf.values.tolist()

reviewerNames = pd.read_excel('reviewers-form.xlsx', sheet_name='LOI Reviewers', usecols=['Reviewer'])
reviewerNames = reviewerNames.values.tolist()

mergedRf = list(zip(reviewerNames, rf))

#compare the Type of Research Expertise & Types of Research Columns

# Create a DataFrame object from the recruiter list
details = pd.DataFrame(mergedRf, columns =['Reviewers', 'Type of Research Expertise'])

#calculating a similarity score and adding it to a list
similarityScore = []
x = 0
app = int(input("What applicant would you like to look at: "))
while x < len(rf):
  #cast them to string
  string1 = str(af[app])
  string2 = str(rf[x])
  similarityScore.append(lev.distance(string1, string2)) 
  x = x + 1


#appending the similarity-score list to the dataframe
details['Similarity Score'] = similarityScore
details = details.sort_values(by = ['Similarity Score'])


#appending top 3 similar reviewers to a list
appreviewers = []
appreviewers.append(details[0:1].Reviewers.tolist())
appreviewers.append(details[1:2].Reviewers.tolist())
appreviewers.append(details[2:3].Reviewers.tolist())
#printing the top 3 reviewers
print("The 3 most similar reviewers to Applicant " + str(app) +  " are: ")
print(*appreviewers, sep='\n')