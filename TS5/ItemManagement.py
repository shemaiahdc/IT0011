class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Error: Item ID already exists.")
            return
        if price < 0:
            print("Error: Price cannot be negative.")
            return
        self.items[item_id] = Item(item_id, name, description, price)
        print("Item added successfully.")

    def view_items(self):
        if not self.items:
            print("No items available.")
            return
        for item in self.items.values():
            print(item)

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        if price is not None and price < 0:
            print("Error: Price cannot be negative.")
            return
        item = self.items[item_id]
        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        if price is not None:
            item.price = price
        print("Item updated successfully.")

    def delete_item(self, item_id):
        if item_id not in self.items:
            print("Error: Item not found.")
            return
        del self.items[item_id]
        print("Item deleted successfully.")


def item_management():
    manager = ItemManager()

    while True:
        print("\nMenu:")
        print("[A] - Add Item")
        print("[V] - View Items")
        print("[U] - Update Item")
        print("[D] - Delete Item")
        print("[Q] - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'Q':
            print("Exiting the program.")
            break

        if choice == 'A':
            try:
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.add_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid input for price. Please enter a numeric value.")

        elif choice == 'V':
            manager.view_items()

        elif choice == 'U':
            try:
                item_id = input("Enter item ID to update: ")
                name = input("Enter new item name (leave blank to keep current): ")
                description = input("Enter new item description (leave blank to keep current): ")
                price_input = input("Enter new item price (leave blank to keep current): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name if name else None, description if description else None, price)
            except ValueError:
                print("Error: Invalid input for price. Please enter a numeric value.")

        elif choice == 'D':
            item_id = input("Enter item ID to delete: ")
            manager.delete_item(item_id)

        else:
            print("Invalid choice. Please try again.")


# Call the function
item_management()