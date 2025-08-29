import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#okno
root = tk.Tk()
mainFrame = tk.Frame(root)
mainFrame.pack()
root.geometry('400x200')  # nastavení rozměrů okna (šířka x výška)
root.title('Tisk obálek')

nadpis = ttk.Label(master=mainFrame, text='Tisk obálek', font='Arial 15 bold')
nadpis.pack()

def kontrola_alert():
    messagebox.showinfo("Info", "Stisknuto btnKontrola")

# tlačítka vedle sebe v jedné řadě
button_frame = tk.Frame(mainFrame)
button_frame.pack(pady=20)

btnKontrola = ttk.Button(master=button_frame, text='Kontrola', command=kontrola_alert)
btnKontrola.pack(side="left", padx=10)

btnTisk = ttk.Button(master=button_frame, text='Tisk obalek')
btnTisk.state(['disabled'])
btnTisk.pack(side="left", padx=10)


#run
mainFrame.mainloop()