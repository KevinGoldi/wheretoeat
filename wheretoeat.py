import random
from tkinter import *

fenster = Tk()
fenster.title("Die magische Essmuschel")
fenster.geometry("300x200")
fenster.resizable(width=False, height=False)
fenster.config(background="lightblue")

def button_action():
    answer = randomise()
    anweisungs_label.config(text="Heute gehts zum:\n\
    " + answer,background="lightgreen")

def randomise():
    answer = ""
    answer_token = random.randint(0, 4)

    if answer_token == 0:
        answer = Lokale[0]
    elif answer_token == 1:
        answer = Lokale[1]
    elif answer_token == 2:
        answer = Lokale[2]
    elif answer_token == 3:
        answer = Lokale[3]
    elif answer_token == 4:
        answer = Lokale[4]

    return answer

Lokale = ["China Man", "Döner Jude", "McDreck", "Subway", "Pizzabomber"]


### tkinter GUI-Aufbau
# Label und Buttons erstellen.
go_button = Button(fenster, text="Go!", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)

anweisungs_label = Label(fenster, text="Heute gehts zum:\n\
    #######")
info_label = Label(fenster, text="Drücke 'Go!' um dein heutiges Essensziel zu bestimmen.\n\
Drücke Beenden um das Programm zu schließen.")

# Nun fügen wir die Komponenten unserem Fenster hinzu.
info_label.grid(row=0, column=1, pady=10)
anweisungs_label.grid(row=2, column=1, pady=10)
go_button.grid(row=1, column=1, padx=0)
exit_button.grid(row=3, column=1, pady=15)

fenster.mainloop()

