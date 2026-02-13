import math;
n1 = float(input("Enter n1 number"))
n2 = float(input("Enter n2 number"))
print("Difference is",abs(n1-n2))
if abs(n1-n2)<=0.001:
    print("Close")
else:
    print("Not close")
