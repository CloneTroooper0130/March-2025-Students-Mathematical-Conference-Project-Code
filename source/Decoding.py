from tkinter import *

code = {
    "α": "ν",
    "β": "ξ",
    "γ": "ο",
    "δ": "π",
    "ε": "ρ",
    "ζ": "σ",
    "η": "τ",
    "θ": "υ",
    "ι": "φ",
    "κ": "χ",
    "λ": "ψ",
    "μ": "ω",
    "ν": "α",
    "ξ": "β",
    "ο": "γ",
    "π": "δ",
    "ρ": "ε",
    "σ": "ζ",
    "τ": "η",
    "υ": "θ",
    "φ": "ι",
    "χ": "κ",
    "ψ": "λ",
    "ω": "μ"
}

root = Tk()
root.geometry(f"{500}x{300}")
root.resizable(False, False)
Label(text="Θέλεις να αποκωδικοποιήσεις ένα μήνυμα;").pack()
Label(text="Εισήγαγε το κλειδί σου εδω:").pack()
e = Entry()
e.pack()
b = Button(text="Αποκρυπτογράφηση")
b.pack()
l = Label()
l.pack()

def decodeMsg():
    msg = str(e.get()).lower()
    s = ""
    for i, v in code.items():
        for let in msg:
            if let == v:
                s+=i
    l.config(text=f"Το μήνυμα είναι: {s}")
    l.pack()

b.config(command=decodeMsg)
b.pack()

root.mainloop()
