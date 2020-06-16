import random

number = random.randint(1,101)

x = 0
y = 12
name = x or y

print(r"//\\")

s = ""

for i in range(2, 10, 2):
		s += str(i)

print(s)

while True:

    answer = input('Input number: ')
    if not answer or answer == "Exit":
        continue

    if not answer.isdigit():
        print("Write right number")
        continue

    user_answer = int(answer)

    if user_answer < number:
        print ("Our number is bigger")
    elif user_answer > number:
        print ("Our number is smaller")
    else:
        print("Congrats!")
        break
