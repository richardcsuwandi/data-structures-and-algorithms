class Stack:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def peek(self):
        if self.is_empty():
            print('The stack is empty')
        else:
            return self.data[self.__len__()-1]

    def pop(self):
        if self.is_empty():
            print('The stack is empty')
        else:
            return self.data.pop()
