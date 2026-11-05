import machine
import utime

LED = machine.Pin(22, machine.Pin.OUT)
T_ms = 1000
tau = 0.5
T1_ms = T_ms * tau
T0_ms = T_ms - T1_ms

LED.off()

alte_zeit_ms = utime.ticks_ms()
while True:
    jetzt_ms = utime.ticks_ms()
    dt_ms = utime.ticks_diff(jetzt_ms, alte_zeit_ms)
    if LED.value ():
        LED.off()
        alte_zeit_ms = utime.ticks_ms()
        
    else:
        if dt_ms> T0_ms:
            LED.on()
            alte_zeit_ms = utime.ticks_ms()
        print(LED.value())
        utime.sleep_ms(100)