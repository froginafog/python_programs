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

#Convert the strings into numerics.
df['W/L Ratio'] = df['W/L Ratio'].astype(float)
df['Games'] = df['Games'].astype(int)

#Plot the data of the pandas dataframe
fig = plt.figure()
ax = plt.axes(projection='3d')
x_data = []
for i in range(0, df.shape[0]):
    x_data.append(i)
y_data = df['Games']
z_data = df['W/L Ratio']
#ax.scatter3D(x_data, y_data, z_data, c = z_data, cmap = 'Greens')
ax.scatter3D(x_data, y_data, z_data)
ax.set_xlabel('Team Index')
ax.set_ylabel('Games Played')
ax.set_zlabel('Win/Loss Ratio')
ax.set_title('NBA Standings')
team_names = df['Team Name']
for x, y, z in zip(x_data, y_data, z_data):
    label = '%s' % df['Team Name'][x]
    ax.text(x, y, z, label)
plt.show()
