class Node:
    def __init__(self, patient_data):
        self.data = patient_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_patient(self, patient_data):
        new_node = Node(patient_data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("Patient with id",patient_data['id'],"added successfully")

    def remove_patient(self, patient_id):
        current = self.head
        prev = None
        while current:
            if current.data['id'] == patient_id:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return current.data  
            prev = current
            current = current.next
        print("Patient with ID", patient_id, "not found.")
        return None

    def display_queue(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def search_patient(self, patient_id):
        current = self.head
        while current:
            if current.data['id'] == patient_id:
                return current
            current=current.next
        print("patient not found")

    def priority_move(self, patient_id):
        if not self.head:
            return
        current = self.head
        prev = None
        while current and current.data['id'] != patient_id:
            prev = current
            current = current.next
        if current and prev:
            prev.next = current.next
            current.next = self.head
            self.head = current

def update(self, patient_id, new_info):
    patient = self.search(patient_id)
    if patient:
        patient.data.update(new_info)
        print("New info of patient added successfully")
    else:
        print("Patient not found!")

queue = LinkedList()
queue.add_patient({'id': 1, 'name': 'Jay', 'condition': 'Urgent'})
queue.add_patient({'id': 2, 'name': 'Pranav', 'condition': 'Stable'})
queue.add_patient({'id': 3, 'name': 'Atharva', 'condition': 'Critical'})
queue.add_patient({'id': 4, 'name': 'Mayank', 'condition': 'Stable'})

print("Current Queue:")
queue.display_queue()
remove_id = int(input("\nEnter patient ID to remove: "))
removed_patient = queue.remove_patient(remove_id)
if removed_patient:
    print("Removed patient:",removed_patient)
else:
    print("Patient not found or queue is empty.")

print("\nQueue after removal:")
queue.display_queue()
priority_id = int(input("\nEnter patient ID to move to priority: "))
queue.priority_move(priority_id)

print("\nQueue after priority move:")
queue.display_queue()

print("\nSearching for patient with ID 2:")
print(queue.search(2).data)

print("\nUpdating patient with ID 2:")
queue.update(2, {'id': 2, 'name': 'Pranav', 'condition': 'Critical'})
queue.display_queue()