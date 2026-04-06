import heapq


class InventoryManager:
    def __init__(self, restock_threshold=5):
        self.products = {}
        self.categories = {}
        self.restock_queue = []
        self.restock_threshold = restock_threshold

    def add_product(self, product_id, name, quantity, price, category):
        if product_id in self.products:
            raise ValueError(f"Product ID '{product_id}' already exists.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        self.products[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "category": category
        }

        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(product_id)

        if quantity < self.restock_threshold:
            heapq.heappush(self.restock_queue, (quantity, product_id))

    def update_quantity(self, product_id, new_quantity):
        if product_id not in self.products:
            raise KeyError(f"Product ID '{product_id}' not found.")

        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.products[product_id]["quantity"] = new_quantity

        if new_quantity < self.restock_threshold:
            heapq.heappush(self.restock_queue, (new_quantity, product_id))

    def search_product(self, product_id):
        return self.products.get(product_id, None)

    def get_products_by_category(self, category):
        product_ids = self.categories.get(category, [])
        return [self.products[pid] | {"product_id": pid} for pid in product_ids]

    def get_next_restock_item(self):
        while self.restock_queue:
            quantity, product_id = heapq.heappop(self.restock_queue)

            if (
                product_id in self.products
                and self.products[product_id]["quantity"] == quantity
                and quantity < self.restock_threshold
            ):
                product = self.products[product_id]
                return {
                    "product_id": product_id,
                    "name": product["name"],
                    "quantity": quantity,
                    "price": product["price"],
                    "category": product["category"]
                }

        return None

    def delete_product(self, product_id):
        if product_id not in self.products:
            raise KeyError(f"Product ID '{product_id}' not found.")

        category = self.products[product_id]["category"]
        del self.products[product_id]

        if category in self.categories and product_id in self.categories[category]:
            self.categories[category].remove(product_id)

            if not self.categories[category]:
                del self.categories[category]

    def display_all_products(self):
        all_products = []
        for product_id, details in self.products.items():
            row = {"product_id": product_id}
            row.update(details)
            all_products.append(row)
        return all_products