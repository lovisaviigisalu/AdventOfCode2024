def read_data_from_file(file_name):
    list1, list2 = [], []

    with open(file_name, 'r') as file:
        for line in file:
            # Loeme iga rea ja eraldame arvud
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)

    return list1, list2



def calculate_total_distance(list1, list2):
    # Sorteeri mõlemad listid
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        dif=abs(list1[i] - list2[i])
        sum += dif

    # Arvuta kauguse summa
    return sum

def part2(a, b):
    a.sort()
    b.sort()
    bigSum = 0
    for i in range(len(a)):
        essa=a[i]
        howMany=0
        for j in range(0, len(b)):
            if b[j] == essa:
                howMany+=1
            if b[j] > essa:
                break
        bigSum += howMany * essa

    return bigSum


# Loeme andmed failist
list1, list2 = read_data_from_file('Day_1/input.txt')

print(part2(list1, list2))
''' 
total_distance = calculate_total_distance(list1, list2)
print(f"Kauguste summa: {total_distance}")
'''