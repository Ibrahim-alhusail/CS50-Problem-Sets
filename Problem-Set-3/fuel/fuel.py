'''
Fuel Gauge

Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains,
output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

def main():
    x,y = get_fractions()
    tank = int(x/y * 100)
    if tank >= 99:
        print("F")
    elif tank <= 1:
        print("E")
    else:
        print(f"{tank}%")

def get_fractions():
    while True:
        try:
            frac = input("Fraction: ")
            x,y = frac.split("/")

            try:
                x,y = int(x), int(y)
            except ValueError:
                raise ValueError("X and Y must both be valid integers")
            
            if y == 0:
                raise ZeroDivisionError("Can't divide on a 0")
            elif x > y:
                raise ValueError("X is greater than Y")
            elif x < 0 or y < 0:
                raise ValueError("X or Y can't be none negative")
        except Exception as e:
            print(e)
            pass
        else:
            return x,y

main()