#!/usr/bin/env python
# coding: utf-8


# is_two takes a single parameter, x that is a int or a string, and will return a bool value 
# if x is either a number or string 2
def is_two(x):
    # check to see if value = string or number 2
    if (x == 2) or (x == '2'):
        return True
    return False


# WALKTHROUGH:
#     
#     When we pass the number 2 the if statement evaluates True so the return True branch is executed.  
#     We will see True printed in our console/notebook


is_two(2)



# is_vowel takes a single parameter, x that is a character, and will return a bool value if x is or is not a vowel
def is_vowel(x):
    # converts to an uppercase character and checks if it is in a list of vowels
    if x.upper() in ['A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False


# WALKTHROUGH:
# 
# When we pass the letter g the if statement converts to uppercase and evaluates False because the letter is not in the vowel set, so the return False branch is executed. We will see False printed in our console/notebook
# 
# When we pass the letter i the if statement converts to uppercase and evaluates True because the letter is in the vowel set, so the return True branch is executed. We will see True printed in our console/notebook
# 


print(is_vowel('g'))
print(is_vowel('i'))



# is_consonant takes a single parameter, x that is a character, and will return a bool value if x is or is 
# not a consonant
def is_consonant(x):
    # converts to an uppercase character and checks if it is NOT in a list of vowels. 
    if x.upper() not in ['A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False


# WALKTHROUGH:
# 
# When we pass the letter h the if statement converts to uppercase and evaluates True because the letter is not in the vowel set, so the return True branch is executed. We will see True printed in our console/notebook
# 
# When we pass the letter a the if statement converts to uppercase and evaluates False because the letter is in the vowel set, so the return False branch is executed. We will see False printed in our console/notebook


print(is_consonant('h'))
print(is_consonant('a'))



# fix_string takes a single parameter, x that is a word, and will return the word with the first letter capitalized
# if it begins with a consonant
def fix_string(x):
    # checks the first letter for a consonant using the is_consonant function
    if is_consonant(x[0]) == True:
        # if the first letter is a consonant it replaces the first letter with an uppercase version and adds
        # the rest of the word
        return (x[0].upper() + x[1:])
    # if the word does not begin with a consonant it returns the original word
    return x


# WALKTHROUGH:
# 
# When we pass the word 'cheese' the if statement checks the first letter to see if it is a consonant by using the is_consonant function we previously defined.  If it is a consonanct the True branch returns the first letter as an uppercase character 'C' and then appends the rest of the original word 'heese' (C + heese = Cheese)
# 
# if the first letter consonant check evaluates false the other branch returns the original word

fix_string('cheese')



# calculate_tip takes two parameters, tip a number between 0 and 1, and total a number
# function will return the amount to tip
def calculate_tip(tip, total):
    # returns the total multiplied by the tip percentage
    return (tip * total)


# WALKTHROUGH:
# 
# When we pass the tip, .15 and the total 198 the function returns the product of the two parameters

calculate_tip(.15,198)



# apply_discount takes two parameters, the price a number, and discount a number representing the percentage
# function will return the price after the discount is applied
def apply_discount(price, discount):
    # discount is divided by 100 to get the percentage, then multiplied by the price to get amount off and 
    # subtracted from the price for final cost
    return (price - (price * (discount/100)))


# WALKTHROUGH:
# 
# When we pass the price and discount parameters the function returns the price after subtracting the discount, which is calulated by dividing the discount by 100 and multiplying by the price.


apply_discount(100, 20)



# handle_commas takes one parameter, 'text' a string that is a number and commas
# function will return the number without the commas
def handle_commas(text):
    #initialize output variable
    outstring = ''
    # for each character in the input text test if it is not a comma, and add the character to the output if it 
    # is not
    for char in text:
        if char != ',':
            outstring += char
    return outstring


# WALKTHROUGH:
# 
# First an empty string is initialized to hold our output.  Then when we pass "1,000,000" to the function it evaluates each letter using a for loop.  For each letter it determines if the character is a comma.  If it is not a comma, it adds the character to the output string.  If the character is a comma it skips to the next iteration of the loop.  Once all characters are checked the output string is returned.


handle_commas('1,000,000')



# get_letter_grade takes one parameter, grade which is a number between 1-100
# function will return a letter grade based upon the range previously provided
def get_letter_grade(grade):
    # check for A range and return if true
    if grade >= 88:
        return 'A'
    # check for B range and return if true
    elif grade >= 80:
        return 'B'
    # check for C range and return if true
    elif grade >= 67:
        return 'C'
    # check for D range and return if true
    elif grade >= 60:
        return 'D'
    # if none of the other ranges were found return F
    else:
        return 'F'


# WALKTHROUGH:
# 
# When we pass 56 the first four if/elif branches all evaluate false so it skips to the else statement and returns false

get_letter_grade(56)



# remove_vowels takes one parameter, stuff a string
# function will return the string with the vowels removed
def remove_vowels(stuff):
    # initialize output string
    output = ''
    # iterate through each letter
    for letter in stuff:
        # if the letter is a consonant add it to the output, otherwise move to the next character
        if is_consonant(letter) == True:
            output += letter
    return output


# WALKTHROUGH:
# 
# First the empty string output is initialized to hold our output.  When the for loop is initiated each character is evaluated to see if it is a consonanct, and and if so it is added to the output.  If it wasn't a consonant it proceeded to the next character until the entire word was evaluated.  Then the output string is returned.

remove_vowels("hello.  How are you?")



# normalize_name takes one parameter, astring which is a string, and will return a valid python identifier
# function returns the input with non-alphanumeric characters removed, leading and trailing whitespace removed,
# everything lowercase, and spaces replaced with underscores
def normalize_name(astring):
    # initialize output
    output = ''
    # for each character in the input
    for char in astring:
        # convert whitespace to _
        if char == ' ':
            output += '_'
        # remove non-alphanumeric
        elif char.isalnum():
            output += char
    # now that the characters have been replaced and put in the output string,
    # perform operations on the output to convert it
    
    # make lowercase
    output = output.lower()
    #remove leading _'s by checking for _ at the first character and removing until we get to another character
    while output[0] == '_':
        output = output[1:]
    #remove trailing _'s by checking for _ at the last character and removing until we get to another character
    while output[-1]== '_':
        output = output[:-1]
    return output


# WALKTHROUGH:
# 
# First the empty string output is initialized to hold our output.  When the first for loop is initiated each character is evaluated to see if it is a whitespace character and if so it is converted to an underscore and added to the output.  If it wasn't whitespace then the character is then evaluated to see if it is alpha-numeric.  If it is it is added to the output, otherwise it is skipped.  Output now contains the original astring input with special characters eliminated and whitespece converted to underscores.  Next the string is converted to lowercase.  Then a while loop checks the first character for underscore.  If it is an underscore it updates the output to the original minus the underscore.  As soon as it encounters a non-underscore it moves on.  The process is then repeated on the last character to remove underscores.  The output is now fully converted and returned back.


normalize_name('   #h 89uii  ')



# cumulative_sum takes one parameter, numbers a list of numbers, and returns a list that is the cumulative sum of 
# the numbers in the list

def cumulative_sum(numbers):
    # initialize output list
    output = []
    # iterate through each number in the original list starting with the second number going through the last number
    for i in range(1, len(numbers)+1):
        # append the sum of the numbers from the first number through the current number to the output list
        output.append(sum(numbers[0:i]))
    return output


# WALKTHROUGH:
# 
# The list of numbers 2,1,3,4 is passed to the function.  First the empty list is initialized to hold our output.  A loop then begins with an index (i) starting at 1 and counting up to the number of numbers in the list (4)
# For each iteration of the loop the output string has number added that is the sum of the first number through the i value.  On the first loop it appends the sum of:  the first number (2) through the number with the index of i.  This includes only the first number.  On the second loop it appends the sum of: the first number through the number with the index of 2.  This includes 2 and 1, so 3 is appended.  This continues through the entire string returning [2,3,6,10]


cumulative_sum([2,1,3,4])



# twelveto24 accepts a string in the format 10:45AM or 4:30PM and returns a string 
# representing the time in 24-hour format

def twelveto24(time):
    #break the string into components that can be evaluated. Evaluated from end since hour can be 1 or 2 digits
    
    #last two chars as ampm
    ampm = time[-2:]
   
    #minutes as minutes
    minutes = time[-4:-2]
    
    #hours as hours saved as int for math
    hours = int(time[-7:-5])
    
    #add 12 to hours if PM and not 12:XX PM
    if ampm == 'PM' and hours != 12:
        hours += 12
        
    #set hours 0 if AM and 12:XX
    if ampm == 'AM' and hours == 12:
        hours = 0
        
    # convert hours back to str
    hours = str(hours)
    
    # add leading zero if only hours is one digit
    if len(hours) == 1:
        hours = '0' + hours
   
    # concat hours and minutes
    output = hours + minutes
    return output    
    


# WALKTHROUGH:
# 
# The time '9:45AM' is passed to the function.  The time is broken into components:
#     string variable ampm is set to the last to characters of the input ('AM')
#     string viaiable minutes is set to the minutes ('45')
#     int variable hours stores the value of the hours (9)
# The ampm is checked for PM and if it was 12 is added to hours (as long as hours are not 12)
# The hours would be changed to zero if it's 12:XX AM
# The hours are then converted back to a string '9'
# The hour is checked for only one digits, and a leading 0 is added if necessary
# The minute and hour strings are then added together and the output returned



twelveto24('9:45AM')


# WALKTHROUGH:
# 
# The time '12:45AM' is passed to the function. The time is broken into components: string variable ampm is set to the last to characters of the input ('PM') string viaiable minutes is set to the minutes ('45') int variable hours stores the value of the hours (12) The ampm is checked for PM and if it had been 12 is added to hours (as long as hours are not 12) The hours were then checked and set to zero because it's 12:XX AM.  The hours are then converted back to a string '12' The hour is checked for only one digits, and a leading 0 is added if necessary.  The minute and hour strings are then added together and the output returned


twelveto24('12:45AM')


# col index accepts a string in the format of a spreadsheet column name, and returns the index # of the column

def col_index(column):
    # initialize output variable
    output = 0
    
    # loop from 1 to X where x is the length of the column name
    for i in range(1, len(column)+1):
        # using -i to start at end of name, make the character uppercase
        letter = column[-i].upper()
        # get ordinal value of letter and subtract 64 to get cypher value (A=1, B=2, etc)
        value = ord(letter) - 64
        # add the value of the letter to the total
        output += value
        # test if this is the first loop.  If not, add 25 each iteration through to account for A-, A--, etc
        if i > 1:
            output += 25
    # return final count
    return output
        

# WALKTHROUGH:
# 
# The string 'ABC' is passed to the function and the output variable is initialized.  We then start a loop that goes from 1 to 3, the number of characters in the column name.  In the first loop the last letter 'C' is selected and made uppercase.  We then get the ordinal value of the character which is 67, and subtract 64 to get the cypher value 3.  That 3 is then added to the output.  The if loop is not executed because i is not greater than 1.  On the next loop i is 2 so we get the second to last character 'B' and make it uppercase.  We get the ordinal value 66 and subtract 64 to get the cypher value 2 which is added to the output.  The if evaluates as true, and we add 25 to the output to account for this being the next digit in a base-26 counting system.  The process continues using the 'A', getting the cypher value 1 and adding it to the output, as well as another 25 for the third digit in the base-25 counting system. Now that all digits were tested the output is returned as the column index number.


col_index("ABC")




