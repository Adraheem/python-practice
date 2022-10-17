import string
#
# word = input("Enter a word: ")
# key = int(input("Enter a key to code with: "))
# abc = string.ascii_lowercase
# inverse = abc[key:] + abc[:key]
# print(word.translate(str.maketrans(abc, inverse)))


str_b = "my name is simbi"
str_b = str_b[:5] + "y" + str_b[6:]
print(str_b)
