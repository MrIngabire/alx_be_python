# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division
        result = numerator / denominator
        
        # Return the result
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
