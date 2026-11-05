import machine
import utime
import urandom

BUTTON = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
LED = machine.Pin("LED",machine.Pin.OUT)

while True:
    input("drücken sie die taste um den test zu starten:")
    wait_time = urandom.uniform(1,5)
    utime.sleep(wait_time)
    LED.on()
    start_time = utime.ticks_ms()
    
    while not BUTTON.value():
        pass
    reaction_time = utime.ticks_diff(utime.ticks_ms(), start_time)
    print(f"Reaktionszeit : {reaction_time} ms")
    LED.off()