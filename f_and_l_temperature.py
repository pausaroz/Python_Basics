def convert_far_to_cel(fahrenheit):
    """Return the result of converting degrees fahrenheit to degrees celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_cel_to_far(celsius):
    """Return the result of converting degrees celsius to degrees fahrenheit."""
    fahrenheit = celsius*9/5 + 32
    return fahrenheit

fahrenheit_from_user = float(input("Enter a temperature in degrees F: "))
print(f"{fahrenheit_from_user} degrees F = {convert_far_to_cel(fahrenheit_from_user):.2f} degrees C")

celsius_from_user = float(input("Enter a temperature in degrees C: "))
print(f"{celsius_from_user} degrees C = {convert_cel_to_far(celsius_from_user):.2f} degrees F")
