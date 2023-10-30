class Item:
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_total(self):
        return self.price 

class Bill:
    def _init_(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item.calculate_item_total() for item in self.items)
        return total

def main():
    bill = Bill()

    while True:
        print("\nOptions:")
        print("1. Add item to the bill")
        print("2. Print bill and exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = float(input("Enter item quantity(in KG): "))

            item = Item(item_name, item_price, item_quantity)
            bill.add_item(item)
        elif choice == '2':
            total = bill.calculate_total()
            print("\nBill Summary:")
            for item in bill.items:
                print(f"{item.name} - Price: ${item.price}, Quantity(in KG): {item.quantity}")
            print(f"Total: ${total}")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

if _name_ == "_main_":
    main()
