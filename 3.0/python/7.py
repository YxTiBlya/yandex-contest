import math

A = list(map(int, input().split(":")))
B = list(map(int, input().split(":")))
C = list(map(int, input().split(":")))

asec = A[2] + A[1]*60 + A[0]*60*60
bsec = B[2] + B[1]*60 + B[0]*60*60
csec = C[2] + C[1]*60 + C[0]*60*60

if csec < asec:
    resptime = (24*60*60 + csec - asec) / 2
else:
    resptime = (csec - asec) / 2
    
if resptime % 1 >= 0.5:
    resptime = math.ceil(resptime)
else:
    resptime = math.floor(resptime)
bsec += resptime

hours = bsec // 3600
minuts = (bsec - 3600 * (bsec//3600)) // 60
seconds = (bsec - 3600 * (bsec//3600)) - 60 * minuts
if hours >= 24: hours = hours - 24

print(f"{hours:02}:{minuts:02}:{seconds:02}")