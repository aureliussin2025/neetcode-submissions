import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, i1: float, i2: float = 0.0) -> float:
        if i2 == 0:
            return round((math.pi * (i1**2)), 2)
        else:
            return round(i1 * i2, 2)
    pass
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
