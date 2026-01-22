"""
simple interest= p * r * t / 100
"""
print("Hello Everyone, Let's calculate Simple Interest")
p=float(input("What's your principal amount: "))
r=float(input("What's your real interest rate: "))
t=float(input("What's your time (in years): "))
SI= p *r * t / 100
print("Simple Interest for", "principal amount invested=",p,"Rs", "for",t," years", "at the rate of interest=", r, "is", SI,"Rs")