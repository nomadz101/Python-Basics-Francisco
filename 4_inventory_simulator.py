# Inventory System Simulator

inventory = {}

def add_product():
    name = input("Enter product name: ").strip()
    if name in inventory:
        print("Product already exists. Use 'restock' to add more quantity.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        if quantity < 0 or price < 0:
            print("Quantity and price must be non-negative.")
            return
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"Product '{name}' added successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for quantity and price.")

def restock_product():
    name = input("Enter product name to restock: ").strip()
    if name not in inventory:
        print("Product not found.")
        return
    try:
        add_qty = int(input("Enter quantity to add: "))
        if add_qty < 0:
            print("Quantity must be non-negative.")
            return
        inventory[name]["quantity"] += add_qty
        print(f"Product '{name}' restocked with {add_qty} units.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def purchase_product():
    name = input("Enter product name to purchase: ").strip()
    if name not in inventory:
        print("Product not found.")
        return
    try:
        purchase_qty = int(input("Enter quantity to purchase: "))
        if purchase_qty <= 0:
            print("Quantity must be greater than zero.")
            return
        if purchase_qty > inventory[name]["quantity"]:
            print("Insufficient stock available.")
            return
        inventory[name]["quantity"] -= purchase_qty
        total_cost = purchase_qty * inventory[name]["price"]
        print(f"Purchased {purchase_qty} units of '{name}' for ${total_cost:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def total_inventory_value():
    total = sum(info["quantity"] * info["price"] for info in inventory.values())
    print(f"\n📦 Total Inventory Value: ${total:.2f}")

def list_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")
    for name, info in inventory.items():
        print(f"- {name}: {info['quantity']} units at ${info['price']:.2f} each")

def show_menu():
    print("\n--- Inventory System Simulator ---")
    print("1. Add New Product")
    print("2. Restock Product")
    print("3. Purchase Product")
    print("4. View Inventory")
    print("5. View Total Inventory Value")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            add_product()
        elif choice == '2':
            restock_product()
        elif choice == '3':
            purchase_product()
        elif choice == '4':
            list_inventory()
        elif choice == '5':
            total_inventory_value()
        elif choice == '6':
            print("Exiting Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()
