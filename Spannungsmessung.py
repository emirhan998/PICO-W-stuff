import machine
import utime

adc = machine.ADC(0)

U_0 = 3.3

while True:
    U_2 = adc.read_u16() * U_0 / 65535
    print("gemessene spannung U_2: ", U_2, "V")
    utime.sleep(1)