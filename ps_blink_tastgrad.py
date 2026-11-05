import machine
import utime

print("geben sie bitte tau ein!")
tau =float(input()) 

print(tau)
utime.sleep(5)
while tau < 0 or tau > 1:
    print("geben sie tau bitte zwischen 1 und 0 ein!")
    tau = float(input())

LED = machine.Pin(22, machine.Pin.OUT)
T_ms = 1000
T1_ms = T_ms * tau
T0_ms = T_ms - T1_ms


LED.off()

alte_zeit_ms = utime.ticks_ms()
while True:
    jetzt_ms = utime.ticks_ms()
    dt_ms = utime.ticks_diff(jetzt_ms, alte_zeit_ms)
    if LED.value ():
        if dt_ms> T1_ms: 
            LED.off()
            alte_zeit_ms = utime.ticks_ms()
        
    else:
        if dt_ms> T0_ms:
            LED.on()
            alte_zeit_ms = utime.ticks_ms()
    print(LED.value())
    
       
        