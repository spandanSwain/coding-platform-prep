class Queue:
    def __init__(self, l: list = []) -> None:
        self.queue = l[:]

    def Enqueue(self, x: int) -> None:
        self.queue += [x]
    
    def Dequeue(self) -> int:
        if self.isEmpty: raise IndexError("No items in the queue")
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val

    @property
    def front(self) -> int:
        if self.isEmpty: raise IndexError("No items in the queue")
        return self.queue[0]

    @property
    def isEmpty(self) -> bool:
        return self.queue == []

    def Traverse(self) -> None:
        for item in self.queue: print(item, end=" ")

if __name__ == "__main__":
    q = Queue([1,2,3,4,5])
    print("Pushed 6")
    q.Enqueue(6)
    print(f"Item at front is: {q.front}")
    print("All items are: ", end=" ")
    q.Traverse()
    
    print("\nRemove item from front ", end=" ")
    q.Dequeue()
    print(f"\nItem at front is: {q.front}")
    print("All items are: ", end=" ")
    q.Traverse()

