v = 121

guess = 1

while v > guess*guess:
   guess += 1

print guess



v = 10


v = float(v)
tolerance = v * 1.e-4
guess = v
#guess = 0.5 * (v + 1.)

while abs(v - guess*guess) > tolerance:
   guess = 0.5 * (guess + v / guess)

print guess

v = 10
result = v

v1 = v
while v1 > 0:
   result *= v1
   v1 -= 1

print result
