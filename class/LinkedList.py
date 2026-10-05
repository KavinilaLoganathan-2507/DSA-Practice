class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBeginning(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return
        else:
            self.tail.next = newnode
            self.tail = newnode

    def insertAtPosition(self, data, position):
        if position == 1:
            self.insertAtBeginning(data)
        else:
            newnode = Node(data)
            temp = self.head
            for _ in range(1, position - 1):
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode

    def updatePosition(self, position, data):
        temp = self.head
        for _ in range(1, position):
            temp = temp.next
        temp.data = data

    def updateData(self, old, ne):
        temp = self.head
        while temp is not None:
            if temp.data == old:
                temp.data = ne
            temp = temp.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("null")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insertAtBeginning(20)
    l1.insertAtBeginning(40)
    l1.insertAtBeginning(60)
    l1.insertAtPosition(50, 3)
    l1.insertAtEnd(80)
    l1.insertAtEnd(100)
    l1.updatePosition(2, 55)
    l1.updateData(60, 70)
    l1.display()
    
    
class Node:
    def __init__(self, num):
        self.data = num
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
       
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def update(self, data, position):
        temp = self.head
        for _ in range(1, position):
            temp = temp.next
        temp.data = data

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("null")

if __name__ == "__main__":
    l1 = LinkedList()
    

    l1.insertAtBeginning(10)  
    l1.insertAtBeginning(20)  
    l1.insertAtBeginning(30)  
   
    l1.update(60, 1)         
    l1.update(40, 2)          
    l1.update(30, 3)         
    
    l1.display()

    
    
#Update 
class Node:
    def __init__(self, num):
        self.data = num
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def update(self, data, position):
        temp = self.head
        for _ in range(1, position):
            temp = temp.next
        temp.data = data

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("null")


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insertAtEnd(10)
    l1.insertAtEnd(20)
    l1.insertAtEnd(30)
    l1.update(60, 1)
    l1.update(40, 2)
    l1.update(30, 3)
    l1.display()
    
#delete

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteAtBeginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    def deleteAtPosition(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head
        for _ in range(1, position - 1):
            if temp is not None:
                temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("NULL")


if __name__ == "__main__":
    list_obj = LinkedList()

    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)

    list_obj.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    print("Original List:")
    list_obj.display()

    list_obj.deleteAtBeginning()
    print("After deleting beginning:")
    list_obj.display()

    list_obj.deleteAtEnd()
    print("After deleting end:")
    list_obj.display()

    list_obj.deleteAtPosition(2)
    print("After deleting position 2:")
    list_obj.display()


#doubly linked list
#insertion
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        new_node.prev = None

       
        if self.head is not None:
            self.head.prev = new_node

    
        self.head = new_node

    
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be None.")
            return

        new_node = Node(data)

        new_node.next = prev_node.next

        
        prev_node.next = new_node

    
        new_node.prev = prev_node

        
        if new_node.next is not None:
            new_node.next.prev = new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.next = None

    
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next

       
        last.next = new_node

       
        new_node.prev = last

   
    def print_list(self):
        node = self.head
        print("Traversal in forward direction:")
        while node is not None:
            print(f"{node.data}", end=" <-> ")
            last = node
            node = node.next
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

   
    dll.insert_at_end(6)

   
    dll.insert_at_beginning(7)

  
    dll.insert_at_beginning(1)

    dll.insert_at_end(8)

    dll.insert_after(dll.head.next, 9)


    dll.print_list()
    
    #delete
    
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

  
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

   
    def delete_head(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

  
    def delete_tail(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

 
        if self.head.next is None:
            self.head = None
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.prev.next = None


    def delete_by_value(self, key):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        curr = self.head

        if curr.data == key:
            self.delete_head()
            return

       
        while curr is not None and curr.data != key:
            curr = curr.next

       
        if curr is None:
            print(f"Value {key} not found in the list.")
            return

        if curr.next is not None:
            curr.next.prev = curr.prev
        
       
        if curr.prev is not None:
            curr.prev.next = curr.next

  
    def print_list(self):
        node = self.head
        if node is None:
            print("Empty List")
            return
        while node is not None:
            print(f"{node.data}", end=" <-> ")
            node = node.next
        print("None")



if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    print("Original List:")
    dll.print_list()

    # 1. Delete Head
    dll.delete_head()
    print("\nAfter deleting head (10):")
    dll.print_list()

    # 2. Delete Tail
    dll.delete_tail()
    print("\nAfter deleting tail (40):")
    dll.print_list()

    # 3. Delete by Value
    dll.delete_by_value(20)
    print("\nAfter deleting value 20:")
    dll.print_list()

#update
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

  
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

   
    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

 
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be None.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    
    def delete_head(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    
    def delete_tail(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if self.head.next is None:
            self.head = None
            return

        last = self.head
        while last.next is not None:
            last = last.next

        last.prev.next = None

    
    def delete_by_value(self, key):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        curr = self.head

       
        if curr.data == key:
            self.delete_head()
            return

        while curr is not None and curr.data != key:
            curr = curr.next

        if curr is None:
            print(f"Value {key} not found in the list.")
            return

      
        if curr.next is not None:
            curr.next.prev = curr.prev
        
        if curr.prev is not None:
            curr.prev.next = curr.next

  
    def print_list(self):
        node = self.head
        if node is None:
            print("Empty List")
            return
        while node is not None:
            print(f"{node.data}", end=" <-> ")
            node = node.next
        print("None")

    def print_list_reverse(self):
        node = self.head
        if node is None:
            print("Empty List")
            return
        
        while node.next is not None:
            node = node.next
            
        
        print("Reverse Traversal:")
        while node is not None:
            print(f"{node.data}", end=" <-> ")
            node = node.prev
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    print("--- Testing Insertions ---")
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(10)
    dll.insert_after(dll.head.next, 25) 
    dll.print_list() 

    print("\n--- Testing Deletions ---")
    dll.delete_by_value(25)
    print("After deleting middle value 25:")
    dll.print_list()
    
    dll.delete_head()
    print("After deleting head:")
    dll.print_list()

    print("\n--- Double-Checking Links (Reverse) ---")
    dll.print_list_reverse()

#circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    
                                                                                  