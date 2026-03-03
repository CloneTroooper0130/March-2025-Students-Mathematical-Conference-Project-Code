from tkinter import *
from random import randint

code = "αβγδεζηθικλμνξοπρστυφχψω"

root = Tk()
root.resizable(False, False)
root.geometry(f"{500}x{300}")
Label(text="Θέλεις ένα κλειδί κρυπτογραφίας;").pack()
Label(text="Εισάγετε τον επιθυμητό αριθμό γραμμάτων του κλειδιού σας:").pack()
e = Entry()
e.pack()
b = Button(text="Δημιούργησε κλειδί!")
b.pack()
l = Label(text="Το κλειδί σου είναι: ΔΕΝ ΕΧΕΤΕ ΔΗΜΙΟΥΡΓΗΣΕΙ ΚΛΕΙΔΙ ΑΚΟΜΑ!")
l.pack()

def generateKey():
    amount = int(e.get())
    s = ""
    for x in range(1, amount):
        s+=code[randint(1, len(code))]
    l.config(text=f"Το κλειδί σου είναι: {s}")
    l.pack()

b.config(command=generateKey)
b.pack()

root.mainloop()
