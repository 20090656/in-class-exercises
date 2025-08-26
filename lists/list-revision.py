# # Create a shopping list with some intitial items

# shopping_list = ["apples", "bananas", "chocolate"]

# # Add an item to the List and Prompt the user to add an item to the list

# shopping_list.append("donuts")
# print(shopping_list)

# list_add = input("Add to the shopping list:\n>")
# shopping_list.append(list_add)

# print(shopping_list)

# # Prompt the user to remove something from the list

shopping_list = ["bread", "eggs", "milk"]

print("Welcome to the shopping list")
print("Please follow the prompts\n===")

edit_list = True

while edit_list == True:
    for items in shopping_list:
        print(items.title())
    add_item = input("Would you like to add something: ")
    shopping_list.append(add_item)
    for items in shopping_list:
        print(items.title())
    rm_item = input("Do you want to remove anything? ")
    rm_item = rm_item.lower()
    if shopping_list.find(rm_item) == False:
        print("nonononon")
        break
    shopping_list.remove(rm_item)
    print(shopping_list)
