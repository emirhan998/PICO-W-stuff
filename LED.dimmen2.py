from machine import Pin,PWM
import utime

led_pin = 15
frequenz = 40
sleepy_day = 5
sleepy_night = 20

pwm = PWM(Pin(led_pin))
pwm.freq(frequenz)

while True:
    for i in range (101):
        tastgrad = i / 100
        pwm.duty_u16(int(tastgrad * 65535))
        utime.sleep_ms(sleepy_day)
        
    for i in range(100, -1, -1):
        tastgrad = i / 100
        pwm.duty_u16(int(tastgrad* 65535))
        utime.sleep_ms(sleepy_night)