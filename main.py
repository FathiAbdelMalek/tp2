import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


print('========= TP 02 : Abdelmalek Fathi =========')
print('First you should create the RdP')
places_num = int(input('Enter the number of places : '))
places = []
print('Enter the Initial Marking :')
for place in range(1, places_num+1):
    places.append(int(input('for P{} : '.format(place))))
initial_places = []
for place in places:
    initial_places.append(place)
transitions_num = int(input('Enter the number of transitions : '))
transitions = []
pre = []
post = []
for place in range(places_num):
    pre.append([])
    post.append([])
i = 1
j = 0
print('Enter the Pre Matrix')
for row in pre:
    print('for P{} :'.format(i))
    for val in range(1, transitions_num+1):
        row.append(int(input('T{} : '.format(val))))
    i += 1
i = 1
print('Enter the Post Matrix')
for row in post:
    print('for P{} :'.format(i))
    for val in range(1, transitions_num+1):
        row.append(int(input('T{} : '.format(val))))
    i += 1
print('Initial Marking {}'.format(places))
print('Pre Matrix = [')
for row in pre:
    print(row)
print(']')
print('Post Matrix = [')
for row in post:
    print(row)
print(']')
print('Now you can simulate the crossing')
choice = 1
while choice != 0:
    print("1 - simulate a crossing.")
    print("2 - show initial marking.")
    print("3 - show pre matrix.")
    print("4 - show post matrix.")
    print("5 - clear the terminal.")
    print("0 - quit.")
    choice = int(input('Enter your choice : '))
    if choice == 1:
        order = input('Enter the order of the crossing like that T1 T2... (eg: 1 2 3) : ')
        co = order.split(' ')
        flag = 0
        for c in co:
            t1 = []
            t2 = []
            for row in pre:
                t1.append(row[int(c)-1])
            for row in post:
                t2.append(row[int(c)-1])
            i = 0
            for val in t1:
                places[i] -= val
                i += 1
            i = 0
            for val in t2:
                places[i] += val
                if places[i] < 0:
                    flag = 1
                    break
                i += 1
        if flag > 0:
            print(print("Can't simulate this crossing"))
        else:
            print('New Marking {}'.format(places))
        for i in range(places_num):
            places[i] = initial_places[i]
    elif choice == 2:
        print('Initial Marking {}'.format(places))
    elif choice == 3:
        print('Pre Matrix = [')
        for row in pre:
            print(row)
        print(']')
    elif choice == 4:
        print('Post Matrix = [')
        for row in post:
            print(row)
        print(']')
    elif choice == 5:
        clearConsole()
    elif choice == 0:
        print('Thanks for utilizing this program')
    else:
        print('Enter valid choice !')
print("=============== End of TP 02 ===============")
input("Press Enter to exit")
