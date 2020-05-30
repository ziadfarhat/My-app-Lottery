import random
import os
# list used for the winning lottery numbers
wn = []

# List used for users to pick their numbers
un = []
#clear the page
clear = lambda: os.system('cls')
clear()
print ("                                 WELCOME TO THE LOTTERY GAME !!!  ")
print("")

for i in range (6):
  a = random.randint(1,42)
  # Checking if this number have already been picked
  while a in wn:
    # if its picked before , have to append another one
    a = random.randint(1,42)
  
  # Now, let's append it to our list.
  wn.append(a)
  # Sort the numbers
  wn.sort()
  
 
# users asked to pick the numbers

for j in range (6):
    b = int(input("Please pick a number between 1 and 42 \n"))
    if 0 <= b <= 42:
            un.append(b)
    else:
            input("Error! Invalid input. Press any key to continue...")
            b = int(input("Please pick a number between 1 and 42 \n"))
            un.append(b)
    
un.sort()
# clear the page 
clear = lambda: os.system('cls')
clear()
#print the result
print("                             HERE THE RESULT !!!")
print("")
print(" the Lottery numbers")
print (wn)
print("this the numbers you picked")
print (un)
print ("")
#compare between two list to see the matching numbers
same_num = set(wn) & set(un)
print ("this is the numbers you match")
print(same_num)

c = len(same_num)
print(c)

#condition to display the result
if c == 6:
    print("congratulation you won")
else:
    print("Sorry try again ")





