# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
#  and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, 
#  how much will you have to pay?
from ast import And


price = 3
total = 0
little_mermaid = 3
brother_bear = 5
hercules = 1
movies = [little_mermaid, brother_bear, hercules]
for movie in movies:
    total += movie * price
print('total cost is: ', total)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380,
#  and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
total = 0
google = 400
amazon = 380
facebook = 350
total = google * 6 + facebook * 10 + amazon * 4
print('total earned this week is: ', total)

# A student can be enrolled to a class only if the class is not full and
#  the class schedule does not conflict with her current schedule.
if class_full == False AND conflict = False:
    then can_enroll = True
    else can_enroll = False

# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific 
# amount of products.
offer_valid = True if:
    (items_purchased > 3 AND offer_expired == False) OR
    premium_member == True


username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
if len(password) >= 5:
    valid = True
else:
    valid = False

print(valid)

# the username must be no more than 20 characters
if len(username) <= 20:
    valid = True
else:
    valid = False
print(valid)

# the password must not be the same as the username
if username != password:
    valid = True
else:
    valid = False
print(valid)

# bonus neither the username or password can start or end with whitespace
if username[0] == ' ':
    valid = False
elif password[0] == ' ':
    valid = False
else:
    valid = True
print(valid)











