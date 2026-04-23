import machine
import utime
import urandom

BUTTON = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
LED = machine.Pin('LED', machine.Pin.OUT)


while True:
    input("Drucken sie die eingabetaste, um den Test zu starten:")
    wait_time = urandom.uniform(1,5)  #zufallig wartezit
    utime.sleep(wait_time)
    LED.on()
    start_time = utime.ticks_ms()
    
    
    while BUTTON.value() == 0:
        pass
    reaction_time = utime.ticks_diff(utime.ticks_ms(), start_time)
    print("Reaktionszeit:{:.2f} ms".format(reactions_time))
    LED.off() #LED ausschalten