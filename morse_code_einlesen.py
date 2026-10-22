from machine import Pin
import utime


pin = Pin(22,Pin.IN, Pin.PULL_DOWN) #taster eingang
wort= ""


codetabelle = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", "..-.": "E",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K",
    ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U",
    "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

startzeit = utime.ticks_ms()
  
while True :
    dauer = utime.ticks_diff(utime.ticks_ms(), startzeit)
    if pin.value()== 1:
        if 70 <= dauer <= 150:
            startzeit = utime.ticks_ms()
            wort = "."
        if 250<= dauer<=400:
            startzeit = utime.ticks_ms()
            wort = "-"

    if pin.value() == 0:
        if 70 <= dauer <= 150:
            wort = " "
            startzeit = utime.ticks_ms()
    print(wort)
    
#state abfragen, old state new state vergleichen if t < langegrunddauer dann . else -
    #wann ist das signal hoch und wann ist das signal runtergegangen
    #if state = old state skip/ continue 