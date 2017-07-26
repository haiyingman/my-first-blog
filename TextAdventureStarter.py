start = '''
You are sixteen years old. Your mother makes a few dollars a day working in a shoe factory. You have three younger siblings.
For the past few days, your mom has been terribly ill.
She asks you to go to her side and says "I am sorry, but are you willing to fill
in for me again today?"
'''
bad = '''
There will be no source of income today, and your family will starve.
'''
sad = '''
You are now walking to the factory alone in a thunderstorm where working hours are from 9 to 9.
You can always turn back now. Do you want to?
'''
walk = '''
You are walking for 30 minutes and finally arrive at the factory door. You tie your hair
and put on your face mask. You put on your gloves as well, but realize they have broken.
You will not be getting another pair and would have to bare handedly deal with hazardous
materials. Do you still want to stay?
'''






print(start)


print(" Type ")

print("Type 'yes' to say yes or 'no' to say no.")
user_input = input()
if user_input == "yes":
    print(" Yea, I'll do it. Get better.")
    print(sad)

elif user_input == "no":
    print(" I can't do it again. I'm sorry.")
    print(bad)
    done = True

print(" Type ")
print("Type 'yes' to say yes or 'no' to say no.")
user_input = input()
if user_input == "yes":
    print(" Yikes, it'll be a thirty minute walk. Hopefully I don't get sick.")
    print(walk)

elif user_input == "no":
    print(" I can't do it. I'm going back")
    print(bad)
    done = True
