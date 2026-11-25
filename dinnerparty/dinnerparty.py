import random

num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {input(): 0 for _ in range(num_friends)}
    total_amount = float(input("\nEnter the total amount:\n"))
    lucky_choice = input("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    if lucky_choice == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"\n{lucky_one} is the lucky one!")
        split_value = round(total_amount / (num_friends - 1), 2)
        for name in friends:
            friends[name] = 0 if name == lucky_one else split_value
    else:
        print("\nNo one is going to be lucky")
        split_value = round(total_amount / num_friends, 2)
        for name in friends:
            friends[name] = split_value
    print()
    print(friends)
