# Basic Understanding On How to Convert an Array to a LinkedList In Python!!!

# First We need to create a Node Class
#We Initialized the Node class 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# Now We have to Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data,end="->")
            current_node = current_node.next
        print("None")
def array_to_linked_list(arr):
    linked_list = LinkedList()
    for i in arr:
        linked_list.append(i)
    return linked_list
if __name__ == '__main__':
    arr = eval(input("Enter the Array : "))
    linked_list = array_to_linked_list(arr) 
    linked_list.print_list()

# input : [1,2,3,4]
# output : 1-> 2-> 3-> 4-> None

# Clear Explanation on this Code
# Node Class:

# This class represents a single node in the linked list.
# Each node has two attributes: data to store the value of the node and next to store a reference to the next node in the linked list.



# LinkedList Class:

# This class represents the linked list itself.
# It has an attribute head which points to the first node in the linked list.
# It provides methods to manipulate the linked list, such as append to add elements to the end of the list and print_list to print the elements of the list.


# array_to_linked_list Function:

# This function takes an array (arr) as input and converts it into a linked list.
# It initializes an empty linked list (linked_list).
# It iterates over each element in the array and appends it to the linked list using the append method of the LinkedList class.
# Finally, it returns the converted linked list.


# Main Block:

# In the main block, the user is prompted to input an array.
# The array_to_linked_list function is called with the input array, and the resulting linked list is stored in the variable linked_list.
# Then, the print_list method of the LinkedList class is called to print the elements of the converted linked list.