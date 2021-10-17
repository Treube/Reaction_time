import time 
import random
"""
Created on Mon Jul 5 22:51:20 2021

@author: Reuben
@Title: Reaction time
"""
"""The purpose of this program is to output a random sequence of 15 characters on the computer, ranging from letters on the QWERTY
   keyboard to the numbers on the keyboard. The users job is to quicky enter in the character they see as quickly as possible in order
   to test reaction time in seconds. At the end of the 15 tries, the program averages the number of seconds it took for each 

"""

print("Welcome to reaction time!")
time.sleep(1)#this delays the speech for the program 
name= input("Please enter your name => ") #ask for the users name 
time.sleep(0.5)
print("Hello",name+", welcome to reaction time")
time.sleep(2)

time.sleep(1.5)
print("""You are going to be presented with a series of characters, it is your job to 
enter the characters as quickly as possibe""")
time.sleep(2.5)
time.sleep(1)

ready = input(name+", when you are ready type the character 's' ")

#this is a sequence of the possible 
character_choices = '1234567890!@#$%^&*()_-+=qwertyuiopasdfghjklzxcvbnm' 
#this array is going to store the reaction times of the user 
Reaction_times=[]
#this array is going to store the sequence of characters
char =[]

print("READY.....\n")
time.sleep(1)
print("SET.....\n")
time.sleep(1)
print("GO!!!")
time.sleep(0.3)


for i in range(15):
    random_char = random.choice(character_choices);
    char.append(random_char)
    time.sleep(0.5)
    t_start = time.time()
    answer = input(random_char+"\n")
    while answer!=random_char:
       answer = input("Please try again ----  "+ random_char+"\n")
     
    
    t_finish = time.time()
    time_taken = t_finish-t_start
    Reaction_times.append(time_taken)
    
    
#this part averages the reaction times
total_time= 0
for e in Reaction_times:
    total_time +=e
    
Average_time= total_time/len(Reaction_times)
print()
print("Calculating your reaction time.....")
time.sleep(1.5)
print("Your average reaction time is {:.1f} seconds\n".format(Average_time))
time.sleep(1.5)


print("Below is a chart of your reaction time for each character->")
time.sleep(1.2)
print("{:<15} | Time(s)".format("Character"))
line = '-'*30
print(line)
for i in range(15):
    time.sleep(0.5)
    print("{:<15} | {:.1f}".format(char[i],Reaction_times[i]))
