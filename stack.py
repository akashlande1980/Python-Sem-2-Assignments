class Stack:
    def __init__(self):
        
        self.stack = []

    def push(self, item):
        
        self.stack.append(item)

    def safe_pop(self):
        
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()

    def peek(self):
        
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        
        return len(self.stack) == 0

    def size(self):
        
        return len(self.stack)

def menu():
    stack = Stack()
    
    while True:
        print("\nMenu:")
        print("1. Push element to stack")
        print("2. Pop element from stack")
        print("3. Peek top element")
        print("4. Check if stack is empty")
        print("5. Get stack size")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("Enter the element to push: ")
            stack.push(item)
            print(f"Element '{item}' pushed to stack.")
        
        elif choice == '2':
            popped_item = stack.safe_pop()
            if popped_item is not None:
                print(f"Popped element: {popped_item}")
        
        elif choice == '3':
            top_item = stack.peek()
            if top_item is not None:
                print(f"Top element: {top_item}")
            else:
                print("Stack is empty.")
        
        elif choice == '4':
            if stack.is_empty():
                print("The stack is empty.")
            else:
                print("The stack is not empty.")
        
        elif choice == '5':
            print(f"Stack size: {stack.size()}")
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()