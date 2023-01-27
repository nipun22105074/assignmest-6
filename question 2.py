def remove(string):
    return string.replace(" ",'')
str1=input('enter the string:')
str1=remove(str1)
str2=str1[::-1]
if str1==str2:
    print('the number is a palindrome')
else:
    print('the number is not an palindrome')
    

