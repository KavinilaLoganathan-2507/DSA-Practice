class StackArr:

    def __init__(self):
        self.size = int(input("Enter the size of the stack: "))
        self.stack = [0] * self.size
        self.top = -1

    # Push method to add an element to the stack
    def push(self, data):
        if self.top == self.size - 1:
            print("Stack is full.")
            return
        else:
            self.top += 1
            self.stack[self.top] = data

    # Pop method to remove an element from the stack
    def pop(self):
        if self.top == -1:
            print("Stack is empty.")
            return None

        popped_element = self.stack[self.top]

        self.stack[self.top] = 0
        self.top -= 1

        return popped_element
    #peek method to view the top element of the stack
    def peek(self):
            if self.top == -1:
                print("Stack is empty.")
                return None
            else:
                return self.stack[self.top]


s = StackArr()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("Stack:", s.stack)
print("Top:", s.top)

print("Popped element:", s.pop())
print("Stack after pop:", s.stack)
print("Top:", s.top)




