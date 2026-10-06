# Singly Linked List implementation of Stack
# Insertion and deletion are done at the head

class StackLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    # Push method
    def push(self, data):
        new_node = self.Node(data)

        new_node.next = self.top
        self.top = new_node

    # Pop method
    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None

        popped_element = self.top.data
        self.top = self.top.next

        return popped_element

    # Peek method
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None

        return self.top.data


S = StackLinkedList()

S.push(10)
S.push(20)
S.push(30)
S.push(40)

print("Top element:", S.peek())

print("Popped element:", S.pop())


print("Top element:", S.peek())


#Final list of elements in the stack

print("Final elements in the stack:")
current = S.top
while current is not None:
    print(current.data, end=" ")
    current = current.next
print() 

# Doubly Linked List implementation of Stack
# Insertion and deletion are done at the head

class StackDoublyLinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.top = None

    # Push method
    def push(self, data):
        new_node = self.Node(data)

        new_node.next = self.top

        if self.top is not None:
            self.top.prev = new_node

        self.top = new_node

    # Pop method
    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None

        popped_element = self.top.data

        self.top = self.top.next

        if self.top is not None:
            self.top.prev = None

        return popped_element

    # Peek method
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None

        return self.top.data

D = StackDoublyLinkedList()

D.push(10)
D.push(20)
D.push(30)
D.push(40)

print("Top element:", D.peek())

print("Popped element:", D.pop())



print("Top element:", D.peek())

#Final list of elements in the stack

print("Final elements in the stack:")
current = D.top
while current is not None:
    print(current.data, end=" ")
    current = current.next
print() 
