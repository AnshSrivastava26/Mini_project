inventory = {}
def add_item(item_name, quantity):
    """Add an item to the inventory"""
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def remove_item(item_name, quantity):
    """Remove an item from the inventory"""
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
        else:
            print("Error: Not enough quantity available to remove.")
    else:
        print("Error: Item not found in inventory.")

def display_inventory():
    """Display the current inventory"""
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")