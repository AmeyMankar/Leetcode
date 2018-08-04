

#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#https://leetcode.com/problems/to-lower-case/description/

def ToLowerCase(input_str):
  result = input_str.lower()
  #result = lambda input_str: input_str[:1].lower() + input_str[1:] if input_str else ''
  return(lambda input_str: input_str[:1].lower() + input_str[1:] if input_str else '')

input_str = input()
print(ToLowerCase(input_str))