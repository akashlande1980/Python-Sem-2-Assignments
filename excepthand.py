try:
    
    numerator = 10
    denominator = int(input("Enter a number: "))
    result = numerator / denominator
except ZeroDivisionError:
    
    print("Error: Denominator cannot be 0.")
except ValueError:
    
    print("Error: Invalid input. Please enter a valid number.")
else:
    
    print(f"The result is {result}.")
finally:
    
    print("Execution finished.")