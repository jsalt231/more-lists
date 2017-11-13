"""
Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one
"""

shopping_list = []
# Establishes my fantastical loop
while True:
    q1 = input("Would you like to add something to your shopping list: y/n\n")
# Asks user for input
    if q1 == "y":
        shopping_list.append(input("What would you like to add?\n"))
# Confirms user's choices
    if q1 == "n":
        print(shopping_list)
        q2 = input("Is this your finalized shopping list? y/n\n")
# Once we're all good, prints list and breaks
        if q2 == "y":
            print(shopping_list)
            break
# Allows user to remove items
        if q2 == "n":
            shopping_list.remove(input("What would you like to remove?\n"))



