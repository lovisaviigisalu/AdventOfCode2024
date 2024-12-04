# Define the file path
import math


path = "Day_2/input.txt"
def read_data_from_file(path):
    data = []
    with open(path, 'r') as file:
        for rida in file:
            rida=rida.split()
            list2=[]
            for el in rida:
                el=int(el)
                list2.append(el)
            if (len(list2) > 0):
                data.append(list2)

    return data

# Function to read the file and determine safe reports
def determine_safe_reports(matrix):
    notSafe=0
    for list in matrix:
        for i in range(len(list)-1):
            diff = abs(list[i]-list[i+1])
            if diff > 3 or diff < 1:
                notSafe+=1
                break
    return notSafe
    
    
data = read_data_from_file('Day_2/input.txt')
safe_reports = determine_safe_reports(data)
print(f"Number of safe reports: {safe_reports}")
