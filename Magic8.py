import random
name = "N"

question = "Will I win the lottery?"

answer = ""

# Generating a random number

random_number = random.randint(1,9)
print(random_number)

# Control Flow 

if random_number == 1:
  answer = "It is decidely so"
elif random_number == 2:
  answer = "Yes definitely"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"


# Seeing the result:

print(f"{name} asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")
