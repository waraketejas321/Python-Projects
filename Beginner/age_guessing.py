# In this program the computer guesses your age in maximum of 10 tries
min = 0
max = 100
tries = 10
for i in range(tries):
    age = int((min+max)/2)
    print(f"Are you {age} years old ?")
    ans = input().lower()
    if (ans == 'more'):
        min = age
    
    elif (ans == 'less'):
        max = age

    elif (ans == 'correct'):
        print("Yeah! I am right.")
        break
    

