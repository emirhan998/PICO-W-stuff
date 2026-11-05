import machine
import utime

adc = machine.ADC(0)

U_0 = 3.3
R_1 = 1000

while True:
    U_2 = adc.read_u16() * U_0 / 65535
    U_1 = U_0 - U_2
    I_mA = 1000 * U_1/ R_1
    R_ohm = U_2 / I_mA 
    print("gemessener Wiederstand : ", R_ohm, "K_OHM")
    