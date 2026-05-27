import tkinter as tk
import random

a = random.randint(0, 9)

def controlla():
    global a

    try:
        b = int(entry.get())
    
        if b == a:
            risultato.config(
                text="Hai indovinato!",
                fg="#00ff88"
            )
        else:
            risultato.config(
                text=f"Sbagliato! Era {a}",
                fg="#ff5555"
            )

        a = random.randint(0, 9)


        entry.delete(0, tk.END)

    except ValueError:
        risultato.config(
            text="Inserisci un numero valido!",
            fg="#ffd166"
        )


finestra = tk.Tk()
finestra.title("Indovina il Numero")
finestra.geometry("450x350")
finestra.config(bg="#0f172a") 

titolo = tk.Label(
    finestra,
    text="Indovina il Numero",
    font=("Helvetica", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
titolo.pack(pady=25)

label = tk.Label(
    finestra,
    text="Scegli un numero da 0 a 9",
    font=("Helvetica", 14),
    bg="#0f172a",
    fg="white"
)
label.pack()

entry = tk.Entry(
    finestra,
    font=("Helvetica", 18),
    justify="center",
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    width=10
)
entry.pack(pady=20)

bottone = tk.Button(
    finestra,
    text="Controlla",
    font=("Helvetica", 14, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#3b82f6",
    activeforeground="black",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2",
    highlightthickness=0,
    command=controlla
)
bottone.pack()

risultato = tk.Label(
    finestra,
    text="",
    font=("Helvetica", 16, "bold"),
    bg="#0f172a"
)
risultato.pack(pady=30)

finestra.mainloop()
