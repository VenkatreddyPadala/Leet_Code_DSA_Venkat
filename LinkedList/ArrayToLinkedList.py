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
arr = eval(input("Enter the Array : "))
linked_list = array_to_linked_list(arr) 
linked_list.print_list()

