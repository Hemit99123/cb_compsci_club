# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data (value)
        self.next = None  # Pointer to the next node (default is None)
        
# Define the LinkedList class (continued with common operations)
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list (attribute)

    # Method to add a node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node object
        if self.head is None:  # If the list is empty, make this node the head (the start of the linked list)
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next != None: #Continue traversing list unless there is no next node
            current = current.next
        current.next = new_node  # Link the new node at the end

    # Method to display the list
    def display(self):
        current = self.head  # Start from the head
        while current:
            print(current.data, end=" -> ")  # Print the data
            current = current.next  # Move to the next node
        print("None")  # End of the list

    # Method to insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Make the new node the head

    # Method to search for a value in the list
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:  # Check if the current node has the value
                return True
            current = current.next  # Move to the next node
        return False

    def delete(self, target):
        current = self.head  # Start from the head
        previous = None      # Keep track of the previous node

        while current: 
            if current.data == target:
                if previous is None:  # If target is in the head node
                    self.head = current.next
                else:  # Target is somewhere in the middle or end
                    previous.next = current.next
                return  # Exit after deleting the node
            previous = current  # Move the previous pointer
            current = current.next  # Move to the next node
    
    