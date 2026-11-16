# strings as collector of character
# 0 1 2 3 4 5 6 7 8 9
# H E L L O W O R L D

text=input("Enter a string:")

print("*"*10+"Indexing and slicing "+"*"*10)

print("first character:", text[0])

print("last character:", text[-1])

print("first 3 character:", text[0:3])

print("from index 3 on words:", text[3:])

print("Reverse of the text:"), text[::-1]

print("second character :",text[::2])

print("-*"*10+"case conversion "+"*"*10)

print("uppercase:", text.upper())

print("lower case:", text.lower())

print("swap case :", text.swapcase())

print("*"*10+"count occurences "+"*"*10)

sub = input("enter a character or substring ")

print("'"+ sub+ "'occurs", text.count(sub),"times(s)")

print("*"*10+"Replace a word "+"*"*10)

old = input("enter the word to replace:")

new = input("enter the new word :")

print("after replacing :", text.replace(old, new))

print("*"*10+" split and join "+"*"*10)

word = text.split( )

print("after split :", word)

print("after join:"), "-".join(word)

print("*"*10+"starts with and ends with "+"*"*10)

start = input(" enter the substring to check at the start: ")

end = input(" enter the substring to check at the end : ")

print(" start with'" + start + "':", text.startswith(start))

print(" ends with '" +end + "':", text.endswith(end))
 