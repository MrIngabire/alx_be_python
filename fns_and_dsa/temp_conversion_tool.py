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
    
    # Input temperature in Celsius
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Convert Celsius to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
    
    # Input temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")

if __name__ == "__main__":
    main()
