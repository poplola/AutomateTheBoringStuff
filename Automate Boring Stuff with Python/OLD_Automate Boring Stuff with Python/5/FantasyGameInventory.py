
print('\n=====================================================================\n')

# Display inventory items
def displayInventory(myInventory):
    print('Inventory: ')
    count = 0

    for k, v in myInventory.items():
        print(v, k)
        count += v

    print(f'Total number of items: {count}')


# Add items to inventory
def addToInventory(myInventory, addedItems):
    print(f'\nThe items you will add are :\n{addedItems}')

    for k in addedItems:
        if k in myInventory.keys():
            myInventory[k] = myInventory[k] + 1          
        else:
            myInventory.setdefault(k, 1)
    return myInventory


def main():

    inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    displayInventory(inventory)
    addToInventory(inventory, dragonLoot)
    displayInventory(inventory)


if __name__ == "__main__": main()

print('\n=====================================================================\n')