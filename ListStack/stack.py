class stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
