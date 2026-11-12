from machine import Pin,ADC,PWM
import utime

frequenz = 500
tastgrad = 1

adc_faktor = 3.3 / 65535

adc = ADC(Pin(26))
pwm = PWM(Pin(15))
pwm.freq(frequenz)
pwm.duty_u16(int(tastgrad * 65535))

alte_zeit = utime.ticks_ms()
while True:
    jetzt = utime.ticks_ms()
    if utime.ticks_diff(jetzt, alte_zeit) >= 30:
        adc_wert = adc.read_u16()
        u = adc_wert * adc_faktor
        print(f"{u:.3f}")
        alte_zeit = jetzt