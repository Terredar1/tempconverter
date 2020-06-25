def temp(celsius):
        msg1 = " degree Celsius are "
        msg2 = " degrees Fahrenheit."
        result = (celsius * 9/5) +32
        return str(celsius) + msg1 + str(result) + msg2

temp_in_celc = input("Enter a temperature in degrees Celsius: ")
Fahrenheit_result = temp(float(temp_in_celc))

print(Fahrenheit_result)