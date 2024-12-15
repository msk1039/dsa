class customer:
    def __init__(self, name, contact_info , service ):
        self.name = name
        self.contact_info = contact_info
        self.service = service
        self.status = "Pending"
        self.next = None


class CustomerService:
    def __init__(self):
        self.head = None

    def add_customer(self, name, contact_info, service):
        current = self.head
        while current.next:
            current=current.next

        new_customer = customer(name, contact_info, service)
        current.next = new_customer

    def process_current_customer(self):
        if self.head is None:
            return None
        self.head.status = "In Progress"
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
        for status, customers in statuses.items():
            if customers:
                print(f"Customers With {status} Status")
                for customer in customers:
                    print(f"   -Customer : {customer}")