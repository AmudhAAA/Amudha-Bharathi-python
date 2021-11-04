print(" ------------------------------------------------")
print("|                                                |")
print("|    10EncodeAString                             |")
print("|    Name : Amudha Bharathi                      |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
str = input("What is your string? ")
encode = ""
for element in str:
    encode_element = chr(ord(element)+1)
    print(element, "=", encode_element)
    encode += encode_element
    print(encode)
