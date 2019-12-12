# ---------------------------------------------------------------------
# import modules
# ---------------------------------------------------------------------


import string
import time
import sys
import random


# ---------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------


# find out if the name user input is in correct format
def true_name(msg):
    for i in msg:
        if i in string.punctuation:
            return False
        elif i.isnumeric():
            return False
        else:
            return True


# Remove all the unnecessary characters in the string
# From A3 Q10
def remove_punctuation(input_string):
    out_string = ''
    input_string = input_string.strip()
    for i in input_string:
        if i not in string.punctuation:
            out_string+=i
    return out_string


# list contains all the zodiacs
zodiac = ['aries', 'taurus', 'gemini', 'cancer', 'leo','virgo', \
          'libra', 'scorpio', 'sagittarius', 'capricorn', \
          'aquarius', 'pisces']



# see if the user input is in the twelve zodiacs
def zodiac_exist(msg):
    # remove unncessary information
    msg = msg.lower()
    msg = remove_punctuation(msg)
    if msg in zodiac:
        return True
    else:
        return False



# dictionary contains the msg according to the score
zodiac_dict = {
    'low' : "That wasn't too bad, but apparently you both have \
something to improve on. Try to be more patient with him or her the \
next time when you are in a argument might help. =)",
    
    "medium" : "This is a great score. You can understand each other \
better than anyone else could! Nevertheless, you could still get \
some disagreements. Try to listen better next time.",
    
    "high" : "Wow! This is the perfect score! I believe that you are \
each other's soulmate! Carry on!"
    
}



# randomly give the score

def result():
    score = random.choice(range(70,101))
    print('Magical Tree: You get the score: ')
    print(score)
    
    # print the msg according to the score
    if score <80:
        print(zodiac_dict["low"])
    elif score >= 80 and score < 90:
        print(zodiac_dict["medium"])
    else:
        print(zodiac_dict["high"])



# From https://stackoverflow.com/questions/3160699/python-progress-bar
# mimic progress bar
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x,                                          "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")



# ---------------------------------------------------------------------
# Final Function
# ---------------------------------------------------------------------

# Final function that leads a chat

def magical_tree():
    """Main function to run our chatbot."""
    # Greeting our user
    print('Welcome to the magical tree. This tree could tell you \
the compatibility between you and your beloved one.')
    time.sleep(1)
    print("Let's meet him!")
    time.sleep(1)
    print('Magical Tree: Hello, my friend. Nice to meet you! First, \
please tell me your name: ')
    
    # get message from user
    msg = input('INPUT :\t')
    
    # let user reenter their name if the input contains other characters besides letters
    while not(true_name(msg)):
        print("Magical Tree: That's not your true name. \
Don't try to fool me. Now tell me your true name: ")
        msg = input('INPUT :\t')
        
    # greet the user and get their zodiac    
    print('Magical Tree: Hello ' + msg.capitalize() + \
          '. \nWould you tell me your zodiac please?')
    user_z = input('INPUT :\t')
    
    # let user reenter his/her zodiac if the input is not valid
    while not(zodiac_exist(user_z)):
        print("Magical Tree: Sorry! We don't have that zodiac. \
Please try again: ")
        user_z = input('INPUT :\t')
       
    # acknowledge what user put in
    print('Magical Tree: Oh! ' + user_z.capitalize() + \
          ' is actually my favorite zodiac,', end = ' ')
    
    if remove_punctuation(user_z).lower() == 'aquarius':
        print('because we have the same zodiac!')
    else:
        print('because ' + user_z.capitalize() + ' is amazing!')
    
    time.sleep(1)
    
    # get the beloved one's zodiac
    print("Magical Tree: Ok. Tell me secretly which zodiac does you \
beloved one have: ")
    love_z = input('INPUT :\t')
    
    # let user reenter his/her zodiac if the input is not valid
    while not(zodiac_exist(love_z)):
          print("Magical Tree: Sorry! We don't have that zodiac. \
Please try again: ")
          love_z = input('INPUT :\t')
        
    # acknowledge what user put in
    print('Magical Tree: Emmmm...'+user_z.capitalize() +' and '           +love_z.capitalize() +'! Interesting combination.')
    
    # mimic the progress bar
    print('Magical Tree: Let me do the calculation. Mami Mami Hong!')
    for i in progressbar(range(100), "Computing: ", 40):
        time.sleep(0.05)
    result()
    print("Here are all my answers! Good luck my friend!")



