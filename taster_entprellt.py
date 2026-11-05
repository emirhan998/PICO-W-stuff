from machine import Pin
import utime


b= Pin(22,Pin.IN, Pin.PULL_DOWN)

z = 0

wartezeit_ms = 20

for i in range (20):
    while b.value() == 0:
        pass
    utime.sleep_ms(wartezeit_ms)
    z+= 1
    while b.value() == 1:
        pass
    utime.sleep_ms(wartezeit_ms)
    
print(z)