# Global variables for conversion factors
celsius_to_fahrenheit_factor = 9.0 / 5.0
fahrenheit_to_celsius_factor = 5.0 / 9.0

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    global celsius_to_fahrenheit_factor
    return celsius * celsius_to_fahrenheit_factor + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    global fahrenheit_to_celsius_factor
    return (fahrenheit - 32) * fahrenheit_to_celsius_factor

# Main program
def main():
    print("Temperature Converter")
    print("---------------------")
    
    # Ask user for temperature value
    temperature = float(input("Enter the temperature value: "))
    
    # Ask user for the unit of the temperature
    unit = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ").upper()
    
    converted_temperature = None
    
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temperature = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {converted_temperature} Fahrenheit.")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temperature = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {converted_temperature} Celsius.")
    else:
        print("Invalid input. Please enter 'C' or 'F'.")
        return
    
if __name__ == "__main__":
    main()
