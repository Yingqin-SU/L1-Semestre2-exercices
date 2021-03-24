import tkinter as tk
import random as rd

demarrer = 1


def start():
    """blabla"""
    global demarrer
    if demarrer:
        mouvement()
        bouton.config(text="Arrêter")
    else:
        canvas.after_cancel(id_after)
        bouton.config(text="Démarrer")
    demarrer = 1 - demarrer


def creer_balle():
    """blabla"""
    x, y, r = 300, 200, 20
    cercle = canvas.create_oval((x-r, y-r), (x+r, y+r), fill="blue")
    nb1 = rd.randint(1, 7)
    nb2 = rd.randint(1, 7)
    return [cercle, nb1, nb2]


def mouvement():
    """blabla"""
    global id_after
    rebond1()
    canvas.move(b[0], b[1], b[2])
    id_after = canvas.after(20, lambda: mouvement(b))


def rebond1(b):
    """blabla"""
    x0, y0, x1, y1 = canvas.coords(b[0])
    if x0 <= 0 or x1 >= 600:
        b[1] = -b[1]
    if y0 <= 0 or y1 >= 400:
        b[2] = -b[2]


# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
bouton = tk.Button(racine, text="Démarrer", command=start)
bouton.grid(row=1)

balle = creer_balle()


racine.mainloop()
