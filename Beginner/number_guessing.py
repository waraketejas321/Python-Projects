import random 
num = random.randint(1, 100)

n = 1
attempts = 0
print("Enter your guess: ")
while (n<=10):
    guess = int(input())
    if (num==guess):
        print("yay! you guess right.")
        break

    elif (num>guess):
        print("Oops! you guess lower.")
        attempts += 1

    else:
        print("Oops! you guess higher.")
        attempts += 1
    n += 1


print("No of attempts you have taken are: ", attempts)
print("Score: ", (10-attempts)*100, "/1000")
