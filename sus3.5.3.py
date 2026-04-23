import machine
import utime

def blink(zeichen):
    for symbol in zeichen:
        LED.value(1)
        t_ein= t0 if symbol=='.' else 3* t0
        utime.sleep(t_ein)
        LED.value(0)
        utime.sleep(t0)
    utime.sleep(2*t0)
    
LED = machine.Pin('LED', machine.Pin.OUT)
LED.value(0)
utime.sleep(1)
t0 = 0.3
codetabelle = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}

while True:
    wort = input("Type a word: ").upper()
    
    for buchstabe in wort:
        if buchstabe in codetabelle:
            blink(codetabelle[buchstabe])