import os

morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

my_dict = {}
temp = 0
output_list = []
ls = ''


for i in range(65,91):
	my_dict[chr(i)] =  morse_code[temp]
	temp += 1

# input_str = 'gin zen gig msg'.split()
for i in words:
	for ch in i:
		if ch.upper() in my_dict.keys():
			ls += my_dict[ch.upper()]
	if ls not in output_list:
		output_list.append(ls)
	ls = ''
# for key in my_dict:

print(len(output_list))
