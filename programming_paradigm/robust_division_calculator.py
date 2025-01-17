def safe_divide(numerator, denominator):
    try:
        x = float(numerator) / float(denominator)
        result = f"The result of the division is {x}"
        return result

    except ZeroDivisionError:    
        result = f"Error: Cannot divide by zero."
        return result

    except ValueError:
        result = f"Error: Please enter numeric values only."
        return result
        
    else:
        pass

    finally:
        pass
