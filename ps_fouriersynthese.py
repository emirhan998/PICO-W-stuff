import machine
import utime
import math

form = "Rechteck"
f0 = 1
harmonics = 100

t_abtast = 0.04
T = 1.0 /f0

num_points = int(T/ t_abtast)

t = 0

while True:
    value = 0
    if form == "Rechteck":
        for k in range(1, harmonics + 1, 2) :
            value += 1.0 / k * math.sin(2*math.pi*f0*k*t)
        value *= (4 / (math.pi))
    elif form == "Sägezahn":
        for k in range(1, harmonics + 1):
            value += 1.0 / k * math.sin(2* math.pi * f0*k*t)
        value *= (2/(math.pi))
    elif form == "Sägezahn_2":
        for k in range (1,harmonics + 1):
            value += 1.0 /k*math.sin(0.5*math.pi * f0 * k * t) #ÄNDERE DIE 0.5 DAMIT SIE LANGSAM FÄLLT UND SCHNELL STEIGT!!!
        value *= (2/(math.pi))
    else:
        print(f"{form} kann ich leider nicht erzeugen")
        break
    print(value)
    utime.sleep(t_abtast)
    t= t+ t_abtast