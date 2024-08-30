marks = ['Chemistry', 56, 98, 34, 76, 88, 52, 20, 48, 63, 76]
name = ['Ashik', 'Kamal', 'Poly', 'jahan', 'Motin',
        'Mollika', 'Joni', 'Omar', 'Kader', 'Afroj']

# print(marks[0], marks[5], name[5])
# for a in range(1, 11):
#    print(marks[a], end= ", ")
# print(marks[1:11])
# print(name[3:7])

list1 = [56, 98, 34, 76, 88, 52, 20, 48, 63, 76]
list2 = [71, 43, 33, 12, 31, 43, 563, 523, 33]

# print("List-1 + List-2 Max Number =", len(list1+list2))

# Sample list containing multiple instances of x
data = [5, 1, 3, 2, 3, 4, 3, 6, 3, 7]
x = 3
# Removing all occurrences of x using a while loop
while x in data:
    data.remove(x)

print("Updated data structure:", data)