FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global celsius
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global fahrenheit
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR  + 32
    return fahrenheit

temperature = float(input("Enter the temperature to convert: "))

temperature_measurment = str(input('Is this temperature in Celsius or Fahrenheit? (C/F): '))

match temperature_measurment:
    case 'F':
        convert_to_celsius(temperature)
        print(str(temperature)+'°F is', str(celsius)+'°C')

    case 'C':
        convert_to_fahrenheit(temperature)
        print(str(temperature)+'°C is', str(fahrenheit)+'°F')

    case _:
        print("Invalid temperature. Please enter a numeric value.")    
