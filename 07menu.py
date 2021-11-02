print(" ------------------------------------------------")
print("|                                                |")
print("|    07Menu                                      |")
print("|    Name : Amudha Bharathi                      |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
def hello_world():
    print("Hello World")
def goodbye_world():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")
def goodbye_person():
    print("Hello")
    name = input("What is your name ? ")
    print("Goodbye",name)
def goodbye_teacher():
    teacher = input("Teacher's name (try Mr Horan) ")
    if teacher=="Mr Horan":
       print("You are lucky, he is a great teacher") 
    else:
        print(teacher,"is an ok teacher")
def forLoop():
    for x in range (1,500):
         print(x)
def whileLoop():

   while True:
    subject = input("What is the name of this subject ")
    if subject == "IST":
        print("")
        print("")
        print(" Congratulations!!")
        print("")
        print("")
        break
    else:
        print("Not Correct - try again") 
# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
def menu():
 while option != "x":
  if option==("1"):
    print("")
    print("----Start of Output ---------------------------")
    hello_world()
    print("")
    print("----End of Output -----------------------------")
    break

  elif option==("2"):
    print("")
    print("----Start of Output ---------------------------")
    goodbye_world()
    print("")
    print("----End of Output -----------------------------")
    break
  elif option==("3"):
    print("")
    print("----Start of Output ---------------------------")
    goodbye_person()
    print("")
    print("----End of Output -----------------------------")
    break
  elif option==("4"):
    print("")
    print("----Start of Output ---------------------------")
    goodbye_teacher()
    print("")
    print("----End of Output -----------------------------")
    break
  elif option==("5"):
    print("")
    print("----Start of Output ---------------------------")
    forLoop()
    print("")
    print("----End of Output -----------------------------")
    break
  elif option==("6"):
    print("")
    print("----Start of Output ---------------------------")
    whileLoop()
    print("")
    print("----End of Output -----------------------------")
    break
    
 else:
    print("")
    print("----Start of Output ---------------------------")
    print("")
    print("invalid option")
    print("")
    print("----End of Output -----------------------------")



print("1. Hello World")
print("2. Goodbye World")
print("3. Goodbye Person")
print("4. Good Teacher")
print("5. forLoop")
print("6. whileLoop")
print("7. string Loop")
print("8. Convert to ascii")
print("9. Encode a string")
print("x. To Exit")
option=input("Enter an option ")
menu()

enter=input("Press enter to continue ")
if enter == "":
    clear()
else:
    menu()
