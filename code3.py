class ProductNode:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.prev = None
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_product(self, product_id, name, quantity, price):
        new_product = ProductNode(product_id, name, quantity, price)
        if self.head is None:
            self.head = self.tail = new_product
        else:
            self.tail.next = new_product
            new_product.prev = self.tail
            self.tail = new_product

    def update_quantity(self, product_id, quantity):
        current = self.head
        while current:
            if current.product_id == product_id:
                current.quantity = quantity
                return True
            current = current.next
        return False

    def calculate_total_value(self):
        total_value = 0
        current = self.head
        while current:
            total_value += current.quantity * current.price
            current = current.next
        return total_value

    def display_inventory(self):
        current = self.head
        while current:
            print(f"Product ID: {current.product_id}, Name: {current.name}, Quantity: {current.quantity}, Price: {current.price}")
            current = current.next

# Example usage
inventory = Inventory()
inventory.add_product(1, "Product A", 10, 5.0)
inventory.add_product(2, "Product B", 20, 10.0)
inventory.add_product(3, "Product C", 15, 7.5)

inventory.display_inventory()
print("Total Inventory Value:", inventory.calculate_total_value())

inventory.update_quantity(2, 25)
inventory.display_inventory()
print("Total Inventory Value:", inventory.calculate_total_value())