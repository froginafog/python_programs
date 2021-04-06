#author: froginafog
from functions import *

filepath = './nba_data/NBA_Standings.json'
data = read_json_file(filepath) #'data' is of the type 'dict'
print(data)
column_names, table = convert_dictionary_of_dictionaries_to_table(data)
table_string = table_to_string(column_names, table, 0, len(table) - 1, 0, len(column_names) - 1)

#Save "table_string" to a .txt file.
#filepath = "./nba_data/" + "NBA_Standings " + str(datetime.now()) + ".txt"
filepath = "NBA_Standings.txt"
file = open(filepath, "w")
file.write(table_string)
file.close()
