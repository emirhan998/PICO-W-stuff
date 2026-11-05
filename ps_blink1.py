import machine
import utime

LED = machine.Pin(22,machine.Pin.OUT)

while True:
    LED.toggle()
    utime.sleep(0.5)
    print(LED.value())