#Create a circular queue to manage drive-thru orders, ensuring fair processing and minimal wait times. Implement features to add, process, and track orders in a round-robin manner

class customer:
    def __init__(self, name, contact_info, service):
        self.name = name
        self.contact_info = contact_info
        self.service = service
        self.status = "Pending"
        self.next = None


class CustomerService:
    def __init__(self):
        self.head = None

    def add_customer(self, name, contact_info, service):
        if self.head is None:
            self.head = customer(name, contact_info, service)
            self.head.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_customer = customer(name, contact_info, service)
        new_customer.next = self.head
        current.next = new_customer

    def process_current_customer(self):
        if self.head is None:
            return None
        self.head.status = "In Progress"
        self.head = self.head.next
        return self.head

    def complete_current_customer(self):
        if self.head is None:
            return None
        removed_customer = self.head
        removed_customer.status = "Completed"
        self.head = self.head.next
        return removed_customer

    def display_customer_by_status(self):
        statuses = {"Pending": [], "In Progress": [], "Completed": []}
        current = self.head
        while current:
            statuses[current.status].append(current.name)
            current = current.next
            if current == self.head:
                break
        for status, customers in statuses.items():
            if customers:
                print(f"Customers With {status} Status")
                for customer in customers:
                    print(f"   -Customer : {customer}")




service = CustomerService()

service.add_customer("Customer 1", "1234567890", "Service 1")
service.add_customer("Customer 2", "1234567890", "Service 2")
service.add_customer("Customer 3", "1234567890", "Service 3")
service.add_customer("Customer 4", "1234567890", "Service 4")
service.add_customer("Customer 5", "1234567890", "Service 5")


print("Customers in queue:")
service.display_customer_by_status()

print("\nProcessing current customer...")
service.process_current_customer()

print("\nCompleting current customer...")
service.complete_current_customer()

print("\nCustomers in queue after processing:")
service.display_customer_by_status()