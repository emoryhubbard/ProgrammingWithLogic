print("Please enter the items of the shopping list (type: quit to finish):")

item = 0
items = []
QUIT = "quit"

while item != QUIT:
    item = input("Item: ")
    if item != QUIT:
        items.append(item)

print("\nThe shopping list is: ")
for item in items:
    print(item)

print("\nThe shopping list with indexes is: ")
for item in items:
    print(f"{items.index(item)}. {item}")

changed = int(input("\nWhich item would you like to change? "))
new = input("What is the new item? ")
items[changed] = new

print("\nThe shopping list with indexes is: ")
for item in items:
    print(f"{items.index(item)}. {item}")
