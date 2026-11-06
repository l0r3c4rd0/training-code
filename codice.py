import winsound
import time

codice_morse={ 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
decifrabile=True
morse=""
stringa=input("dammi una stringa da decifrare in codice morse: ").upper()

for elemento in stringa:
    if not elemento in codice_morse:
        decifrabile=False
        #se rileva un carattere diverso da quelli del diz mette il flag a False per nn far eseguire nulla

if decifrabile:
    for elemento in stringa:
        morse+=" "+codice_morse[elemento]
        #scrivo il determinato valore in codice morse dedicato alla lettera e lo inserisco in una stringa
    for elemento in morse:
        #scorro ogni elemento per poi far suonare
        if elemento==".":
            winsound.Beep(550,240) 
            #Beep(frequenza,durata)
        elif elemento=="-":
            winsound.Beep(550,720)
        elif elemento==" ":
            time.sleep(1.68)
#nn possibile fare un interfaccia grafica con customthinker pk blocca il programma 