#author: froginafog
from functions import *

#Load the json file as a dictionary.
filename = "NBA_Standings.json"
filepath = "./nba_data/" + filename
with open(filepath) as file: #open the file
    data_dict = json.load(file) #load the file into 'data_dict'
    #data_dict is of the type 'dict'

#Convert the dictionary into a pandas dataframe.
df = pandas.DataFrame.from_dict(data_dict)

#Sort the dataframe.
df_sorted = df.sort_values(by = ['W/L Ratio'], ascending = False)

#Plot the data of the pandas dataframe
plot_data_with_bar_chart(df_sorted, "Team Name", "W/L Ratio")

        
