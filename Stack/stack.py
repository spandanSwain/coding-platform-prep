class Stack:
    def __init__(self, l: list = []) -> None:
        self.stack = l[:]
    
    def push(self, x: int) -> None:
        self.stack += [x]

    def pop(self) -> int:
        if self.stack == []: raise IndexError("No element in stack")
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        return val

    @property
    def top(self) -> int:
        if self.stack == []: raise IndexError("No element in stack")
        return self.stack[-1]

    def traverse(self) -> None:
        for item in self.stack: print(item, end=" ")

if __name__ == "__main__":
    s = Stack([1,2,3,4,5])
    print("Push 6")
    s.push(6)
    print("item at top is ", end=" ")
    print(s.top)
    print("stack items are")
    s.traverse()
    
    print(f"\nPopped item is {s.pop()}")
    print("item at top is ", end=" ")
    print(s.top)
    print("stack items are")
    s.traverse()