# List to Dictionary Function for Fantasy Game Inventory
"""
Imagine that a vanquished dragon’s loot is represented as a list of strings like this: dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item.

Output should be:

Inventory: 
45 gold coin 
1 rope
1 ruby
1 dagger
Total number of items: 48
"""

def addToInventory(inventory, addedItems): 
    # your code goes here

    inventoryKeys = inventory.keys()
    for item in addedItems:
        if item in inventoryKeys:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

def displayInventory(inventory):
    total = 0
    print("\nInventory:")
    for k, v in inventory.items():
        total += v
        print(f"{v} {k}")
    print(f"Total number of items: {total}")

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
print("\n")