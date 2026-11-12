import utime
from machine import Pin

TRIG = Pin(21, Pin.OUT)
ECHO = Pin(20, Pin.IN)

print("geben sie eine strecke an!")
Strecke = 22

while True:
    TRIG.low()
    utime.sleep_us(2)
    TRIG.high()
    utime.sleep_us(10)
    TRIG.low()

        
    while ECHO.value() == 0:
        pulse_start = utime.ticks_us()
    while ECHO.value() == 1:
        pulse_end = utime.ticks_us()
        
    T1_us = utime.ticks_diff(pulse_end, pulse_start)
    T2_us = T1_us /1000000
    T2_us = T2_us / 2       # die distanz musst du wissen oder vorher abmessen!
    V = T2_us * Strecke
    print ( V )
    utime.sleep(1)

# 500 us = t