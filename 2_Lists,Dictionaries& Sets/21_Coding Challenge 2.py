"""Create a list of your favourite food items, the list should have minimum 5 elements.

List out the 3rd element in the list.

Add additional item to the current list and display the list.

Insert an element named tacos at the 3rd index position of the list and print out the list elements."""

food_items = ['milk','bread','pasta','cereals','rice','chips']

# Display the 3rd item in the list

print(f"The 3rd item in the list is: {food_items[2]}")

item_appen =input("Enter the food item you want to add: ")

food_items.append(item_appen)

print(f"Updated list of food items: {food_items}")

#ask user which item they want to add

new_food = input("Enter the food item you want to add in 3rd: ")

#Add a food item to 3rd position in the list

food_items.insert(2,new_food)

#display the updated list

print(f"Updated Successfully. Here is the list of food items: {food_items}")