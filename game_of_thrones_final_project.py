print ('Hello! Welcome to my game!')

House_Lannister = 0
House_Stark = 0

print ('Question 1')
print ('Uhhh..your betrothed ends up being a murdering psychopath')
print ('a.) marry then anyways...could be entertaining.')
print ('b.) RUN THE EFF AWAY!!!')
answer = raw_input ('Pick one!')
if answer == "a":
    House_Lannister = 1

print ('Question 2')
print ("The Iron Throne is empty...what's your strategy?")
print ('a.) Alliances and bribes!')
print ("b.) War-it's effective...and fighting is fun!")
answer_2 = raw_input ('Pick one!')
if answer_2 ==  "a":
    House_Lannister = House_Lannister + 1

print ('Question 3: What do you hate more?')
print ('a.) Cold.')
print ('b.) Heat.')
answer_3 = raw_input ('Pick one!')
if answer_3 == "a":
    House_Lannister = House_Lannister +1 

print ('Question 4: Choose a non-human character...')
print ('a.) White Walkers')
print ("b.) Three eyed raven")
answer_4 = raw_input ('Pick one!')
if answer_4 == "a":
    House_Lannister = House_Lannister +1 

print ("Question 5: Your friend is having a birthday party and you don't really feel like going, you...")
print ('a.) Make up an excuse not to go, stay in and watch Netflix.')
print ('b.) Go and pretend to have a good time.')
answer_5 = raw_input ('Pick one!')
if answer_5 == "a":
    House_Lannister = House_Lannister +1 


if House_Lannister < 3:
    print ('House Stark. You are a good person and that is reflected in every aspect of your life, you hold yourself to a higher standard. You highly value honor.')
elif House_Lannister >= 3: 
    print ('House Lannister. You are extremely ambitious. You always pay your debts and are willing to do whatever it takes to get what you want, even if that means not always doing the right thing.')

