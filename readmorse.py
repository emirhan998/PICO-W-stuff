from machine import Pin
import utime

pin = Pin(22, Pin.IN, Pin.PULL_DOWN) # taster eingang
wort = ""

codetabelle = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", "..-.": "E",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K",
    ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

startzeit = utime.ticks_ms()
  
while True:
    if pin.value() == 1:
        startzeit = utime.ticks_ms()
        
        if pin.value() == 0:
            endzeit = utime.ticks_ms()
            dauer = utime.ticks_diff(endzeit, startzeit)
            
            if 70 <= dauer <= 150:
                wort = "."
                startzeit = utime.ticks_ms()
                
            elif 250 <= dauer <= 400:
                wort = "-"
                startzeit = utime.ticks_ms()
                
            else:
                wort = " "

for buchstabe in wort:
        if buchstabe in codetabelle:
            print(codetabelle[buchstabe])
#state abfragen, old state new state vergleichen if t < langegrunddauer dann . else -
    #wann ist das signal hoch und wann ist das signal runtergegangen
    #if state = old state skip/ continue 