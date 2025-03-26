# message = "Hello the world"
# print(message)
#Naming and using variables 
# Contain only letters, numbers, underscores. Can start with a letter and an underscore, but not with a number. Ex: message1 not 1message
# Spaces not allow
# Avoid python keyword and function 
# Short but descriptive
# Becarefule with l (letter l) and O (letter O uppercase) with 1 and 0, numbers

# Exercise 
# 2.4
T = "Hello bae, i love you so much"
VAT = "Vo Anh Thu"
print(VAT.upper())
print(VAT.lower())
print(VAT.title())

#2.5
print('Albert Eistein once said: "A person who never made a mistake')
print('never tried anything new."')

#2.6
famous_person = "Albert Eistein"
message = "A person who never made a mistake never tried anything new."
print(famous_person + ' once said: ' + '"' + message + '"' )

#2.7
VATT =" \t Vo Anh Thu \n "
print(VATT)
print(VATT.rstrip())
print(VATT.lstrip())
print(VATT.strip())
#\t là tab thụt vào đầu dòng
#\n là dòng mới
#rstrip: xóa khoảng trắng ở bên phải
#lstrip: xóa khoảng trắng ở bên trái
#strip: xóa khoảng trắng ở 2 bên

#2.8
filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))

#Number
#2.9
print(2+6)
print(10-2)
print(48//6)
print(4*2)

#2.10
favornum = 6
mess = "So yeu thich cua toi la " + str(favornum) 
print(mess)

#Zen of python
#Simple is better than complex
#Complex is better than complicated
#Readability counts.
#Now is better than never.

import this
