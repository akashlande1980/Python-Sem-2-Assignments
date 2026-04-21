from collections import deque

class Queue:
    def __init__(self):
    
        self.queue = deque()

    def enqueue(self, item):
        
        self.queue.append(item)

    def safe_dequeue(self):
        
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            return self.queue.popleft()

    def peek(self):
        
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def is_empty(self):
    
        return len(self.queue) == 0

    def size(self):

        return len(self.queue)

def menu():
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Enqueue element")
        print("2. Dequeue element")
        print("3. Peek front element")
        print("4. Check if queue is empty")
        print("5. Get queue size")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("Enter the element to enqueue: ")
            queue.enqueue(item)
            print(f"Element '{item}' enqueued to the queue.")
        
        elif choice == '2':
            dequeued_item = queue.safe_dequeue()
            if dequeued_item is not None:
                print(f"Dequeued element: {dequeued_item}")
        
        elif choice == '3':
            front_item = queue.peek()
            if front_item is not None:
                print(f"Front element: {front_item}")
            else:
                print("Queue is empty.")
        
        elif choice == '4':
            if queue.is_empty():
                print("The queue is empty.")
            else:
                print("The queue is not empty.")
        
        elif choice == '5':
            print(f"Queue size: {queue.size()}")
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()