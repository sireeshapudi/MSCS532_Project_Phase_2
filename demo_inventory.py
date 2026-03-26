from inventory_manager import InventoryManager


def print_section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def main():
    inventory = InventoryManager(restock_threshold=5)

    print_section("ADDING PRODUCTS")
    inventory.add_product("P101", "Laptop", 10, 899.99, "Electronics")
    inventory.add_product("P102", "Mouse", 2, 24.99, "Electronics")
    inventory.add_product("P201", "Milk", 3, 4.99, "Groceries")
    inventory.add_product("P202", "Bread", 8, 2.99, "Groceries")
    inventory.add_product("P301", "Notebook", 4, 3.50, "Stationery")

    print("Products added successfully.")

    print_section("DISPLAYING ALL PRODUCTS")
    for product in inventory.display_all_products():
        print(product)

    print_section("SEARCH PRODUCT")
    product = inventory.search_product("P101")
    print("Search result for P101:")
    print(product)

    print_section("UPDATE QUANTITY")
    inventory.update_quantity("P101", 4)
    print("Updated quantity of P101 to 4.")
    print("New details of P101:")
    print(inventory.search_product("P101"))

    print_section("PRODUCTS BY CATEGORY")
    electronics = inventory.get_products_by_category("Electronics")
    print("Electronics category products:")
    for item in electronics:
        print(item)

    print_section("NEXT RESTOCK ITEM")
    next_item = inventory.get_next_restock_item()
    print("Highest priority restock item:")
    print(next_item)

    print_section("DELETE PRODUCT")
    inventory.delete_product("P202")
    print("Deleted product P202.")
    print("Remaining products:")
    for product in inventory.display_all_products():
        print(product)

    print_section("FINAL RESTOCK QUEUE CHECK")
    while True:
        item = inventory.get_next_restock_item()
        if item is None:
            break
        print(item)


if __name__ == "__main__":
    main()
