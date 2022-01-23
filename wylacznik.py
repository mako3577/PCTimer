import tkinter
import os


def wylacz():
    h = godziny.get()
    m = minuty.get()
    czas_sekundy = h*3600 + m*60
    os.system(f"shutdown /s /t {czas_sekundy}")


def anuluj():
    os.system(f'shutdown /a')


width = 320
height = 240

root = tkinter.Tk()
root.geometry(f'{width}x{height}')

root.columnconfigure(0, weight=int(width/4))
root.columnconfigure(1, weight=int(width/4))
root.columnconfigure(2, weight=int(width/4))
root.columnconfigure(3, weight=int(width/4))

label = tkinter.Label(root, text='Hours').grid(row=0, column=0)
label1 = tkinter.Label(root, text='Minutes').grid(row=0, column=2)

godziny = tkinter.Scale(root, from_=0, to=12, orient=tkinter.VERTICAL)
godziny.grid(column=1, row=0)

godziny.set(1)

minuty = tkinter.Scale(root, from_=0, to=59, orient=tkinter.VERTICAL)
minuty.grid(column=3, row=0)


potwierdz = tkinter.Button(root, text='Accept', background='green', command=wylacz)
potwierdz.place(rely=2/4, relwidth=1, relheight=1/4)

anuluj = tkinter.Button(root, text='Cancel', background='red', command=anuluj)
anuluj.place(rely=3/4, relwidth=1, relheight=1/4)


root = tkinter.mainloop()
