from machine import Pin
import utime

led_pin = 15
frequenz = 100
tastgrad = 0.5



T_ms = int(1000/frequenz)
T1_ms = int(T_ms * tastgrad)
led = Pin(led_pin, Pin.OUT)

while True:
    led.on()
    utime.sleep_ms(T1_ms)
    led.off()
    utime.sleep_ms(T_ms- T1_ms)