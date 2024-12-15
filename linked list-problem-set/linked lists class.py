# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data (value)
        self.next = None  # Pointer to the next node (default is None)

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list
        self.tail = None  # Initialize the tail of the linked list

    # Method to add a node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node object
        if self.head is None:  # If the list is empty, make this node the head and tail
            self.head = new_node
            self.tail = new_node
            return
        # Link the new node at the end and update the tail
        self.tail.next = new_node
        self.tail = new_node

    # Method to display the list
    def display(self):
        current = self.head  # Start from the head
        while current:
            print(current.data, end=" -> ")  # Print the data
            current = current.next  # Move to the next node
        print("None")  # End of the list

    # Method to reverse the linked list
    def reverse(self):
        # Initialize pointers
        prev = None  # Previous node, initially None
        current = self.head  # Start with the head node

        # Traverse the list and reverse the pointers
        while current:
            next_node = current.next  # Temporarily store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move the previous pointer to the current node
            current = next_node       # Move to the next node

        # Update the head and tail pointers
        self.tail = self.head  # The old head becomes the tail
        self.head = prev       # The last processed node becomes the new head