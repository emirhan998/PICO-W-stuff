from machine import Pin

b= Pin(22, Pin.IN,Pin.PULL_DOWN)

z = 0
print("bitte 20 mal den taster drücken")

for i in range(20):
    while b.value() == 0:
        pass
    z += 1
    while b.value() == 1:
        pass
print(z)