#author: froginafog
import pandas
from datetime import datetime
import csv
import json
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------------

def table_to_string(column_names, table, starting_row, ending_row, starting_column, ending_column):
    max_column_lengths = [0] * len(column_names)
    for j in range(starting_column, ending_column + 1):
        max_column_lengths[j] = len(column_names[j])
    for i in range(starting_row, ending_row + 1):
        for j in range(starting_column, ending_column + 1):
            table[i][j] = str(table[i][j])
            if(len(table[i][j]) > max_column_lengths[j]):
                max_column_lengths[j] = len(table[i][j])
    num_dashes = 0
    for n in range(starting_column, ending_column + 1):
        num_dashes = num_dashes + max_column_lengths[n] + 3
    num_dashes = num_dashes + 1
    dashes = ""
    for n in range(0, num_dashes):
        dashes = dashes + '-'
    output = dashes + "\n|" 
    for j in range(starting_column, ending_column + 1):
        s = " %" + str(max_column_lengths[j]) + "s "
        s = s % column_names[j]
        output = output + s + "|"
    output = output + "\n" + dashes + "\n"
    for i in range(starting_row, ending_row + 1):
        output = output + dashes + "\n|"
        for j in range(starting_column, ending_column + 1):
            s = " %" + str(max_column_lengths[j]) + "s "
            s = s % table[i][j]
            output = output + s + "|"
        output = output + "\n"
    output = output + dashes + "\n"
    return output      

#--------------------------------------------------------------------------------------

def convert_table_to_pandas(table, column_names):
    df = pandas.DataFrame(table, columns = column_names)
    pandas.set_option('display.max_rows', df.shape[0] + 1)
    pandas.set_option('display.max_columns', df.shape[1] + 1)
    pandas.set_option('display.width', 1000)
    return df

#--------------------------------------------------------------------------------------

def convert_table_to_dictionary(column_names, table):
    num_rows = table
    dictionary = {column_names[i]: table[i] for i in range(0, len(num_rows))}
    return dictionary

#--------------------------------------------------------------------------------------

def append_win_lose_ratios_to_table(table):
    num_rows = len(table)
    num_columns = len(table[0])
    for i in range(0, num_rows):
        ratio = float(table[i][1])/float(table[i][2])
        ratio = "%.3f" % ratio
        table[i].append(ratio)

#--------------------------------------------------------------------------------------

def append_num_games_to_table(table):
    num_rows = len(table)
    num_columns = len(table[0])
    for i in range(0, num_rows):
        num_matches = int(table[i][1]) + int(table[i][2])
        num_matches = "%d" % num_matches
        table[i].append(num_matches)

#----------------------------------------------------------------------------
#push a row into the first row of the matrix
def matrix_push_front(A, a): #'A' is the matrix, 'a' is the list to be pushed in
    B = []
    B.append(a)
    num_rows = len(A)
    for i in range(0, num_rows):
        B.append(A[i])
    return B

#--------------------------------------------------------------------------------------

def save_table_as_csv(column_names, table, filepath):
    table = matrix_push_front(table, column_names)
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)      

#--------------------------------------------------------------------------------------

def save_table_as_json(column_names, table, filepath):
    dictionary = convert_table_to_dictionary(column_names, table)
    with open(filepath, 'w') as file:
        json.dump(dictionary, file)

#--------------------------------------------------------------------------------------

def read_csv_file(filepath):
    df = pandas.read_csv(filepath) 
    return df

#--------------------------------------------------------------------------------------

def print_csv_file(filepath): 
    df = pandas.read_csv(filepath)
    table_string = table_to_string(df.columns, df.values, 0, df.shape[0] - 1, 0, df.shape[1] - 1)
    print(table_string)

#--------------------------------------------------------------------------------------

def read_json_file(filepath):
    with open(filepath) as file:
        data = json.load(file) #'data' is of the type 'dict'
    return data

#--------------------------------------------------------------------------------------

def convert_dictionary_of_dictionaries_to_table(dictionary):
    column_names = []
    for key in dictionary.keys(): #The keys become the column names.
        column_names.append(key)
    table = []
    for value_dict in dictionary.values(): #Here, value_dict is still a dictionary 
        row = []
        for value in value_dict.values():
            row.append(value)
        table.append(row)
    table = matrix_transpose(table)
    return column_names, table

#--------------------------------------------------------------------------------------

def matrix_transpose(A):
    num_rows = len(A)
    num_columns = len(A[0])
    a = [] 
    for j in range(0, num_columns):
        for i in range(0, num_rows):
            a.append(A[i][j])
    temp = num_rows
    num_rows = num_columns
    num_columns = temp
    AT = [] #transpose of A
    k = 0
    for i in range(0, num_rows):
        row = []
        for j in range(0, num_columns):
            row.append(a[k])
            k = k + 1
        AT.append(row)
    return AT

#--------------------------------------------------------------------------------------

def plot_data_with_bar_chart(df, x_axis_column_name, y_axis_column_name):
    #Everything in df is in the form of string.
    #Before we plot, we must convert the strings to numbers.
    w_l_ratio = list(df[y_axis_column_name])
    num_strings = len(w_l_ratio)
    for i in range(0, num_strings):
        w_l_ratio[i] = list(w_l_ratio[i])
        num_chars = len(w_l_ratio[i])
        for j in range(0, num_chars):
            if(w_l_ratio[i][j] == ','):
                w_l_ratio[i][j] = ''
        w_l_ratio[i] = ''.join(w_l_ratio[i])
        w_l_ratio[i] = float(w_l_ratio[i])
    plt.bar(df[x_axis_column_name], w_l_ratio, width = 0.7)
    plt.xticks(rotation = 90) #angle of rotation of the x-labels
    plt.grid(color = 'silver', axis = 'y', alpha = 0.5)
    #plt.barh(df[x_axis_column_name], df['W/L Ratio'], height = 0.1)
    #plt.xticks(rotation = 45) #angle of rotation of the x-labels
    #plt.grid(color = 'silver', axis = 'x', alpha = 0.5)
    plt.xlabel(x_axis_column_name)
    plt.ylabel(y_axis_column_name)
    plt.title(y_axis_column_name + " versus " + x_axis_column_name)
    for x, y in zip(df[x_axis_column_name], w_l_ratio):
        label = "{:.3f}".format(y)
        plt.annotate(label, #the text we want to put on each bar
                     xy = (x,y), #position of each text that we want to put
                     textcoords = "offset points", #how to position the text
                     xytext = (0,12), #distance from the text to each point
                     horizontalalignment = 'center',
                     verticalalignment = 'center',
                     rotation = 45 #degreen of rotation of the text
                     )
    plt.show()
