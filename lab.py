from math import pi, atan

def solve(a,b):
    if a==0 and b==0: return None
    elif b==0: return 0
    elif a==0: return pi/2
    elif a<0: return atan(b/a) + pi
    elif b<0: return atan(b/a) + 2*pi
    else: return atan(b/a)

