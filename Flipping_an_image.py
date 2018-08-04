input_list = [[1,1,0],[1,0,1],[0,0,0]]
print("Original list:\t", input_list)
i = 0
for ls in input_list:
    i = 0
    temp = len(ls)-1
    while temp >= (len(ls)/2) and i <= (len(ls)/2):
        a = ls[i]
        ls[i] = ls[temp]
        ls[temp] = a
        temp -= 1
        i+=1

print("Horizontal list:\t" ,input_list)
for ls in input_list:
	i = 0
	while i <= (len(ls)-1):
		if ls[i] == 0:
			ls[i] = 1
		else:
			ls[i] = 0
		i += 1

print("Flipped list:\t", input_list)
