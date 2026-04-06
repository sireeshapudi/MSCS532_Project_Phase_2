import time
from inventory_manager import InventoryManager


def run_performance_test():
    sizes = [100, 500, 1000, 5000]

    for size in sizes:
        inventory = InventoryManager()

        start_insert = time.time()
        for i in range(size):
            inventory.add_product(
                f"P{i}",
                f"Item{i}",
                i % 10,
                10.0 + (i % 5),
                f"Category{i % 5}"
            )
        end_insert = time.time()

        start_search = time.time()
        for i in range(size):
            inventory.search_product(f"P{i}")
        end_search = time.time()

        start_category = time.time()
        inventory.get_products_by_category("Category1")
        end_category = time.time()

        start_restock = time.time()
        for _ in range(20):
            inventory.get_next_restock_item()
        end_restock = time.time()

        print(f"\nDataset Size: {size}")
        print(f"Insertion Time: {end_insert - start_insert:.6f} seconds")
        print(f"Search Time: {end_search - start_search:.6f} seconds")
        print(f"Category Retrieval Time: {end_category - start_category:.6f} seconds")
        print(f"Restock Retrieval Time: {end_restock - start_restock:.6f} seconds")


if __name__ == "__main__":
    run_performance_test()