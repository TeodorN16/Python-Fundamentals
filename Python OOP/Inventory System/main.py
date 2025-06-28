class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return f"Item with name {self.name} has price: {self.price} in quantity:{self.quantity}"

    def get_total_price(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        if item not in self.items:
            self.items.append(item)
            print("Item added!")
        else:
            print("Item is already in inventory!")
    def remove_item(self,name):
        found_item=None
        for item in self.items:
            if(item.name==name):
                found_item=item
                break

        if found_item:
            self.items.remove(found_item)
            print("Item removed.")
        else:
            print("Such item was not found")



    def list_items(self):
        if (len(self.items)==0):
            print("(No items)")
        else:
            print("Inventory has: ")
            for item in self.items:
                print(item.__str__())

    def get_total_value(self):
        total=0
        for item in self.items:
            total+=item.get_total_price()
        return(f"Total value of the inventory: {total}")


# Create some items
sword = Item("Sword", 150.0, 2)
potion = Item("Health Potion", 25.0, 5)

# Create inventory and add items
inventory = Inventory()
inventory.add_item(sword)
inventory.add_item(potion)

# List all items
inventory.list_items()

# Get total value
print(inventory.get_total_value())

# Remove an item
inventory.remove_item("Sword")

# List items again
inventory.list_items()
