inputs = input("Input integer numbers: ").split()

tuple_list = list()

for i in range (0, len(inputs), 2):
    tuple_list.append((int(inputs[i]), int(inputs[i+1])))

for i in range (len(tuple_list)):
    print(tuple_list[i], end=' + ')

