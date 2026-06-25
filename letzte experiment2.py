import machine
import utime
import math

VDD = 3.3
f = 1
x = machine.ADC(machine.Pin(26))
schwelle = machine.ADC(machine.Pin(27))
komperator = machine.ADC(machine.Pin(28))

pwn = machine.PWM(16)


while True:
    utime.sleep(0.05)
    t = utime.ticks_ms() / 1000 #zeit in sekunden
    pwn_wert = int((math.sin(2* math.pi * f * t) + 1) * 32767)
    pwn.duty_u16(pwn_wert) # tastgrad setzen
    print(x, schwelle , komperator)
    a = ausgang.read_u16()*VDD/65535