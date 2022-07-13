#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prompt the user for a day of the week, print out whether the day is Monday or not


# In[5]:


what_day = input("what day is it?  ")

if what_day.upper() == "MONDAY":
    print("It's Monday!!!")
else:
    print ("Not Monday")


# In[6]:


# prompt the user for a day of the week, print out whether the day is a weekday or a weekend


# In[10]:


weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekend = ['saturday', 'sunday']

is_it_weekend = input("What day is it?  ")

if is_it_weekend.lower() in weekdays:
    print("it's a weekday!")
elif is_it_weekend.lower() in weekend:
    print("it's a weekend")
else: 
    print("that's not a day!")


# In[11]:


# # create variables and make up values for

# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours


# In[17]:


week_hours = 48
hourly_rate = 12.50
paycheck = 0

if week_hours > 40:
    paycheck = ((week_hours - 40) * (hourly_rate * 1.5)) + 40 * hourly_rate
else:
    paycheck = week_hours * hourly_rate
    
print('$', "{:.2f}".format(paycheck))


# In[18]:


# While

# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.


# In[19]:


i = 5

while i <= 15:
    print(i)
    i += 1
    


# In[20]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.


# In[23]:


i = 0
while i <= 100:
    print(i)
    i += 2


# In[24]:


# Alter your loop to count backwards by 5's from 100 to -10.


# In[25]:


i = 100
while i >= -10:
    print(i)
    i -= 5


# In[26]:


# Create a while loop that starts at 2, and displays the number squared on each line while
# the number is less than 1,000,000. Output should equal:


# In[27]:


i = 2
while i < 1000000:
    print(i)
    i = i**2


# In[28]:


# Write a loop that uses print to create the output shown below


# In[29]:


i = 100
while i > 0:
    print(i)
    i -= 5


# In[30]:


# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.


# 

# In[ ]:





# In[36]:


number = int(input("give me a number:  "))

i = 1
while i <= 10:
    print(number," x ", i, " = ", number *10)
    i += 1


# In[37]:


# Create a for loop that uses print to create the output shown below.


# In[47]:


i = 1

while i < 10:
    j = 1
    while j <= i:
        print(i,end = '')
        j +=1
    print("")
    i += 1


# In[48]:


# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement 
# to output all the odd numbers between 1 and 50, except for the number the user entered.


# In[50]:





# In[7]:


while i < 1:
    number = input("give me an odd number between 1 and 50:  ")
    if (number.isdigit() == True) and (int(number) <= 50) and (int(number) >=1) and (int(number) %2 == 1):
        break
    
number = int(number)

print("Number to skip is:  ", number)

j=1
while j < 50:
    if j == number:
        print('Yikes! Skipping number: ',number)
        j += 2
        continue
    print('Here is an odd number: ',j)
    j += 2



        
    
    
        


# In[88]:


# # The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
#  also note that the input function returns a string, so you'll need to convert this to a numeric type.)


# In[6]:


i = 0
while i < 1:
    number = input("give me a positive number between 1 and 50:  ")
    if (number.isdigit() == True) and (int(number) <= 50) and (int(number) >=1):
        break
    
number = int(number)

j=0
while j <= number:
    print(j)
    j+=1


    
    
        


# In[5]:


# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
    number = input("give me a positive number between 1 and 50:  ")
    if (number.isdigit() == True) and (int(number) <= 50) and (int(number) >=1):
        break
        
j=int(number)
while j >= 0:
    print(j)
    j-=1


# In[99]:


# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

i = 0

while i <= 99:
    i+=1
    if i%3==0 and i%5==0:
        print('FizzBuzz')
        continue
    if i%3==0:
        print('Fizz')
        continue
    if i%5==0:
        print('Buzz')
        continue
    print(i)
    


# In[ ]:


# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
while True:
    number = int(input("What number would you like to go up to?  "))

    print("Here is your table!")
    print("")
    print("number | squared | cubed")
    print("------ | ------- | -----")

    i = 1
    pipe = "|  "
    while i <= number:
        print(f"{i : <7}{pipe : <1}{i**2 : <7}{pipe : <1}{i**3 : <9}")
        i +=1
    check = input("Would you like to continue? (Y/N)")
    if check == 'Y':
        continue
    else:
        break


# In[126]:


# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

while True:
    grade = int(input("enter the numerical grade  :"))
    if grade >= 88:
        print("The grade is A")
    elif grade >= 80:
        print("The grade is B")
    elif grade >= 67:
        print("The grade is C")
    elif grade >= 60:
        print("The grade is D")
    else:
        print("The grade is F")
    check = input("Would you like to continue? (Y/N)")
    if check == 'Y':
        continue
    else:
        break


# In[2]:





# In[ ]:




