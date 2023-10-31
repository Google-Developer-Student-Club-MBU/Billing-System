# Define a class called Item to represent individual items in a bill
class Item:
    # Constructor to initialize an item with its name, price, and quantity
    def _init_(self, name, price, quantity):
        self.name = name  # Name of the item
        self.price = price  # Price of the item
        self.quantity = quantity  # Quantity of the item (in KG)

    # Method to calculate the total cost of the item (price per KG)
    def calculate_item_total(self):
        return self.price

# Define a class called Bill to represent a bill containing multiple items
class Bill:
    # Constructor to initialize an empty bill with a list of items
    def _init_(self):
        self.items = []  # List to store items in the bill

    # Method to add an item to the bill
    def add_item(self, item):
        self.items.append(item)

    # Method to calculate the total cost of all items in the bill
    def calculate_total(self):
        total = sum(item.calculate_item_total() for item in self.items)
        return total

# Define the main function to interact with the user and manage the bill
def main():
    bill = Bill()  # Create a new bill object

    while True:
        print("\nOptions:")
        print("1. Add item to the bill")
        print("2. Print bill and exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = float(input("Enter item quantity (in KG): ")

            # Create a new Item object with the provided details
            item = Item(item_name, item_price, item_quantity)

            # Add the item to the bill
            bill.add_item(item)
        elif choice == '2':
            # Calculate the total cost of the bill
            total = bill.calculate_total()

            # Display the bill summary
            print("\nBill Summary:")
            for item in bill.items:
                print(f"{item.name} - Price: ${item.price}, Quantity (in KG): {item.quantity}")
            print(f"Total: ${total}")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

# Check if the script is being run as the main program
if _name_ == "_main_":
    main()  # Call the main function to start the bill management program
