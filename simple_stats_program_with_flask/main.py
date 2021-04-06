#flask program
#author: froginafog (Liang D.S.)

from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def index():
    sum_of_x = 0
    sum_of_y = 0
    mean_of_x = 0
    mean_of_y = 0
    variance_of_x = 0
    variance_of_y = 0
    standard_deviation_of_x = 0
    stardard_deviation_of_y = 0
    num_x_data = 0
    num_y_data = 0
    table_values = []
    if(request.method == 'POST'):
        x_received = request.form['x_input']
        y_received = request.form['y_input']
        if(x_received != None and y_received != None):
            if(x_received.isnumeric() and y_received.isnumeric()):
                x_received = float(x_received)
                y_received = float(y_received)
                x_data.append(x_received)
                y_data.append(y_received)
                num_x_data = len(x_data)
                num_y_data = len(y_data)
                if(num_x_data >= 2 and num_y_data >= 2):
                    sum_of_x = calculate_sum(x_data)
                    sum_of_y = calculate_sum(y_data)
                    mean_of_x = calculate_mean(x_data)
                    mean_of_y = calculate_mean(y_data)
                    variance_of_x = calculate_variance(x_data)
                    variance_of_y = calculate_variance(y_data)
                    standard_deviation_of_x = calculate_standard_deviation(x_data)
                    stardard_deviation_of_y = calculate_standard_deviation(y_data)
            else: #so that when no data is entered and we press submit, the data is cleared
                x_data.clear()
                y_data.clear()
    """
    #for formatting the output
    sum_of_x = "%.6f" % sum_of_x
    sum_of_y = "%.6f" % sum_of_y
    mean_of_x = "%.6f" % mean_of_x
    mean_of_y = "%.6f" % mean_of_y
    variance_of_x = "%.6f" % variance_of_x
    variance_of_y = "%.6f" % variance_of_y
    standard_deviation_of_x = "%.6f" % standard_deviation_of_x
    stardard_deviation_of_y = "%.6f" % stardard_deviation_of_y
    """
    if(num_x_data >= 2 and num_y_data >= 2):
        column_names = ["x", "y"]
        table = []
        table = matrix_push_front(table, y_data)
        table = matrix_push_front(table, x_data)
        table = matrix_transpose(table)
        table_num_rows = len(table)
        table_num_columns = len(table[0])
        table_string = table_to_string(column_names, table, 0, table_num_rows - 1, 0, table_num_columns - 1)
        print(table_string)
        calculation_table_column_names = [" ", "x", "y"]
        calculation_table = [
                                ["sum", sum_of_x, sum_of_y],
                                ["mean", mean_of_x, mean_of_y],
                                ["variance", variance_of_x, variance_of_y],
                                ["standard_deviation", standard_deviation_of_x, stardard_deviation_of_y]
                            ]
        table_num_rows = len(calculation_table)
        table_num_columns = len(calculation_table[0])
        table_string = table_to_string(calculation_table_column_names, calculation_table, 0, table_num_rows - 1, 0, table_num_columns - 1)
        print(table_string)
        print("-----------------------------------------------------------------------------------------")
    table_values = zip(x_data, y_data) # zip() returns an iterator of tuples
    return render_template("index.html",
                           table_values_output = table_values,
                           sum_of_x_output = sum_of_x,
                           sum_of_y_output = sum_of_y,
                           mean_of_x_output = mean_of_x,
                           mean_of_y_output = mean_of_y,
                           variance_of_x_output = variance_of_x,
                           variance_of_y_output = variance_of_y,
                           standard_deviation_of_x_output = standard_deviation_of_x,
                           stardard_deviation_of_y_output = stardard_deviation_of_y
                           )
    
if __name__ == '__main__':  
    app.run(debug = True)

def calculate_sum(a):
    result = 0
    for x in a:
        result = result + x
    return result
    
def calculate_mean(a):
    num_elements = len(a)
    if(num_elements > 0):
        return calculate_sum(a)/num_elements

def calculate_variance(a): #sample variance 
    mean = calculate_mean(a)
    num_elements = len(a)
    result = 0
    if(num_elements > 0):
        for i in range(0, num_elements):
            result = result + (a[i] - mean) * (a[i] - mean) 
        return result/(num_elements - 1) #sample variance
        #return result/num_elements for population variance

def calculate_standard_deviation(a):
    return sqrt(calculate_variance(a))

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

#push a row into the first row of the matrix
def matrix_push_front(A, a): #'A' is the matrix, 'a' is the list to be pushed in
    B = []
    B.append(a)
    num_rows = len(A)
    for i in range(0, num_rows):
        B.append(A[i])
    return B

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

x_data = []
y_data = []

