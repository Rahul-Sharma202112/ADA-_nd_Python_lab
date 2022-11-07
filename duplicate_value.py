# Program to find the duplicate values in a list
def duplicate_value(values): #function to find duplicate integer values in a list
    x=set()                 #creating two set in which first set store the unique value and second set store the duplicate values
    y=set()
    for value in values:
        if value not in x:
            x.add(value)
        else:
            y.add(value)
    return list(y)


num=(input("Enter random number :")).split()
n=[int(x) for x in num]
duplicate_values=duplicate_value(n)
print(duplicate_values)