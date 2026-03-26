import unittest
from inventory_manager import InventoryManager


class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        self.inventory = InventoryManager(restock_threshold=5)
        self.inventory.add_product("P101", "Laptop", 10, 899.99, "Electronics")
        self.inventory.add_product("P102", "Mouse", 2, 24.99, "Electronics")
        self.inventory.add_product("P201", "Milk", 3, 4.99, "Groceries")

    def test_add_product(self):
        self.inventory.add_product("P301", "Notebook", 7, 3.50, "Stationery")
        self.assertIn("P301", self.inventory.products)
        self.assertEqual(self.inventory.products["P301"]["name"], "Notebook")

    def test_duplicate_product_id(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product("P101", "Laptop 2", 5, 1000, "Electronics")

    def test_update_quantity(self):
        self.inventory.update_quantity("P101", 4)
        self.assertEqual(self.inventory.products["P101"]["quantity"], 4)

    def test_search_product_found(self):
        result = self.inventory.search_product("P102")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Mouse")

    def test_search_product_not_found(self):
        result = self.inventory.search_product("P999")
        self.assertIsNone(result)

    def test_get_products_by_category(self):
        result = self.inventory.get_products_by_category("Electronics")
        self.assertEqual(len(result), 2)

    def test_get_next_restock_item(self):
        item = self.inventory.get_next_restock_item()
        self.assertIsNotNone(item)
        self.assertIn(item["product_id"], ["P102", "P201"])

    def test_delete_product(self):
        self.inventory.delete_product("P201")
        self.assertNotIn("P201", self.inventory.products)

    def test_negative_quantity_add(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product("P400", "Pen", -1, 1.50, "Stationery")

    def test_negative_price_add(self):
        with self.assertRaises(ValueError):
            self.inventory.add_product("P401", "Pen", 5, -1.50, "Stationery")


if __name__ == "__main__":
    unittest.main()
