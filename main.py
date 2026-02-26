import shapes

def main():
    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = input("Enter the number of your choice: ")
    
    try:
        if choice == '1':
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                raise ValueError("Radius must be positive.")
            print(f"The area of the circle is: {shapes.area_circle(radius):.2f}")
        
        elif choice == '2':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be positive.")
            print(f"The area of the rectangle is: {shapes.area_rectangle(length, width):.2f}")
        
        elif choice == '3':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            if base <= 0 or height <= 0:
                raise ValueError("Base and height must be positive.")
            print(f"The area of the triangle is: {shapes.area_triangle(base, height):.2f}")
        
        else:
            print("Invalid choice. Please choose a valid option.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
