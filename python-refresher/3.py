# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda x: x % 2 == 0, numbers))


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")
