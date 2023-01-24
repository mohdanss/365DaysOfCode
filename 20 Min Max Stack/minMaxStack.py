# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        
    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)

    def getMin(self):
        return min(self.stack)

    def getMax(self):
        return max(self.stack)
