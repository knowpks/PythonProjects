import random
# Setting up
name = ""  # the name of the person who will be asking the Magic 8-Ball

# a “Yes” or “No” question you’d like to ask the Magic 8-Ball
question = "Will I win the lottery?"

answer = ""  # store the answer of the Magic 8-Ball

# Generating a random number

random_number = random.randint(1, 9)
print(random_number)

# Control Flow

if (random_number == 1):
    answer = "Yes - definitely"
elif (random_number == 2):
    answer = "It is decidedly so"
elif (random_number == 3):
    answer = "Without a doubt"
elif (random_number == 4):
    answer = "Reply hazy, try again"
elif (random_number == 5):
    answer = "Ask again later"
elif (random_number == 6):
    answer = "Better not tell you now"
elif (random_number == 7):
    answer = "My sources say no"
elif (random_number == 8):
    answer = "Outlook not so good"
elif (random_number == 9):
    answer = "Very doubtful"
else:
    answer = "Error"



# Seeing the result

#What if the asker does not provide a name, such that the value of name is an empty string?
if (name == ""):
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + "Outlook not so good")
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
  
