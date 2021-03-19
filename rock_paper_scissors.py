import random

lst = ["r", "p", "s"]
lst1 = ["Rock", "Paper", "Scissors"]

comp_c = random.choice(lst)

print("Enter your choice: ")
your_c = input().lower()
ind1 = lst.index(your_c)

ind = lst.index(comp_c)
comp_choice = lst1[ind]
your_choice = lst1[ind1]

if (your_c in lst):
    if (comp_c == "r"):
        if (your_c == "p"):
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("Yay! you won.")

        elif (your_c == "s"):
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("Oops! you loose it.")

        else:
            print("It's a tie!")

    elif (comp_c == "p"):
        if (your_c == 's'):
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("Yay! you won.")

        elif (your_c == 'r'):
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("Oops! you loose it.")

        else:
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("It's a tie!")

    else:
        if (your_c == 'r'):
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("Yay! you won.")

        elif (your_c == 'p'):
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("Oops! you loose it.")

        else:
            print("Computer choose: ", comp_choice)
            print("You choose: ", your_choice)
            print("It's a tie!")






else:
    print("Enter valid choice!(r-rock, p-paper, s-scissor")
