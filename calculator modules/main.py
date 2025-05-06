
from standard_calculator.stdcal import (
 add, sub, multiply, division,
 floor_division, mod, power as std_power
)
from scientific_calculator.scical import (
 sqrt, power as sci_power,
 log, sine, cosine, tangent
)
if __name__ == "__main__":
 a = int(input("Enter value for a: "))
 b = int(input("Enter value for b: "))
 print("\nStandard Operations:")
 print("Add:", add(a, b))
 print("Sub:", sub(a, b))
 print("Multiply:", multiply(a, b))

 if b != 0:
 print("Division:", division(a, b))
 print("Floor Division:", floor_division(a, b))
 print("Mod:", mod(a, b))
 else:
 print("Cannot perform division, floor division, or modulo by zero.")
 print("Power (std):", std_power(a, b))
 print("\nScientific Operations (using 'a'):")
 if a >= 0:
 print("Sqrt(a):", sqrt(a))
 else:
 print("Cannot compute square root of negative number.")
 print("Power(a^b):", sci_power(a, b))

 if a > 0:
 print("Log(a):", log(a))
 else:
 print("Cannot compute logarithm of non-positive number.")
 print("Sine(a°):", sine(a))
 print("Cosine(a°):", cosine(a))
 print("Tangent(a°):", tangent(a))
