import utime
import machine

LED= machine.Pin('LED', machine.Pin.OUT)
t0 = 0.3

LED.value(0)
utime.sleep(1)

for i in range (3):
    LED.value(1)
    utime.sleep(t0)
    LED.value(0)
    utime.sleep(t0)
    
utime.sleep(2 * t0)
for i in range(3):
    LED.value(1)
    utime.sleep(3* t0)
    LED.value(0)
    utime.sleep(t0)
    
utime.sleep(2* t0)
for i in range (3):
    LED.value(1)
    utime.sleep(t0)
    LED.value(0)
    utime.sleep(t0)