class Stack:
    def __init__(self):
        self.items = []

    def even(self, items):
        for i in range(len(items)):
            if items[i] % 2 == 0:
                print(items[i])

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack(top->bottom):", self.items[::-1])


S = Stack()

#S.push(int(input("Enter a number to push onto the stack: ")))

#S.push(20)
#print("Top of the stack:", S.peek())  
#S.display()

print("Even numbers from the given list:")
S.even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

