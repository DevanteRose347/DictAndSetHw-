# <!-- 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list -->
def store():
    shopping_cart = {}
    
    while True:
        item = input("please enter item or Enter quit to quit! and delete to delete! : ").strip()  
        
        if item.strip().lower() != 'quit' and item.strip().lower() !='delete':
            quantity = input("please enter amount of item or Enter quit to quit! and delete to delete! : ")
            shopping_cart[item] = quantity
        
        
        elif item.strip().lower() == 'delete' or quantity.strip().lower() == 'delete':
            delete = input("please enter item you want to delete! : ")
            del(shopping_cart[delete])
        
        else:
            for item, quantity in shopping_cart.items():
                print(f"{item} {quantity} is in shopping cart")
            break
       

        print(shopping_cart)  
   
store()


# <!-- 2) Set Practice
# Remove all duplicates from the following list

nums_list = [1, 1, 1, 2, 2, 3, 5, 6, 4, 12, 11, 12, 12, 14, 16, 16, 16, 1, 1, 1, 2, 2]
my_list = list(set(nums_list))
print(my_list)
# Out put the intersection of the following the following sets.
set1 = {20, 24, 26, 27}
set2 = {26, 35, 63, 27}
set7 = set1.intersection(set2)
print(set7)

# Output the difference between the following sets
set3 = {100, 65, 89, 200}
set4 = {65, 103, 54, 200}
set5 = set3.difference(set4)
set6 = set4.difference(set3)
print(set5)
print(set6)
