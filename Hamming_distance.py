x = 1
y = 4

list1 = bin(x).replace("0b","")
list2 = bin(y).replace("0b","")


if len(list1) > len(list2):
	list2 = ('0' * (len(list1) - len(list2))) + list2
else:
	list1 = ('0' * (len(list2) - len(list1))) + list1

solution = 0

for i in range(len(list1)):
	if list1[i] != list2[i]:
		solution += 1

print(solution)