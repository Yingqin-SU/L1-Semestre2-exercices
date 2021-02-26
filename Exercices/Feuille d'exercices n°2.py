import tkinter as tk
from random import randint

def exercice_1():

    cpt = 0

    def creer_balle():
        return [canvas.create_oval((280, 180), (320, 220), fill='blue'), randint(1, 7), randint(1, 7)]

    def mouvement():
        if cpt % 2 == 1:
            rebond1(balle)
            rebond2(balle)
            canvas.move(balle[0], balle[1], balle[2])
            canvas.after(30, mouvement)
            bouton.config(text='Arrêter')
        else:
            bouton.config(text='Démarrer')
    
    def change_text(event):
        nonlocal cpt
        if event.widget == bouton:
            cpt += 1

    def rebond1(balle):
        if canvas.coords(balle[0])[0] < 0 or canvas.coords(balle[0])[2] > 600:
            balle[1] *= -1
        if canvas.coords(balle[0])[1] < 0 or canvas.coords(balle[0])[3] > 400:
            balle[2] *= -1

    def rebond2(balle):
        x0, y0, x1, y1 = canvas.coords(balle[0])
        if x1 > 640:
            canvas.coords(balle[0], (-40, y0, 0, y1))
        if y1 > 440:
            canvas.coords(balle[0], (x0, -40, x1, 0))

    root = tk.Tk()
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=600, height=400, bg='black')
    canvas.grid()
    balle = creer_balle()
    bouton = tk.Button(root, text='Démarrer', command=mouvement)
    bouton.grid(row=1)
    
    root.bind('<Button-1>', change_text)

    root.mainloop()
    

def exercice_2():

    LARGEUR = 600
    HAUTEUR = 400
    COULEUR_QUADR = 'white'
    cpt = 0
    liste_rectangle = []

    def creer_rectangle(x0, y0, x1, y1):
        canvas.create_rectangle((x0, y0), (x1, y1), fill='black')
        centerx = x0 + (x1 - x0) // 2
        centery = y0 + (y1 - y0) // 2
        balle = creer_balle(centerx, centery, centerx+5, centery+5)
        return [balle, [x0, y0, x1, y1]]

    def creer_balle(x0, y0, x1, y1):
        return [canvas.create_oval((x0, y0), (x1, y1), fill='blue'), randint(1, 7), randint(1, 7)]

    def quadrillage(n, m):
        dec_x = LARGEUR // n
        dec_y = HAUTEUR // m

        for i in range(n):
            for j in range(m):
                liste_rectangle.append(creer_rectangle(dec_x*i, dec_y*j, dec_x*(i+1), dec_y*(j+1)))

        x0, x1 = 0, LARGEUR
        y = 0
        while y <= HAUTEUR:
            canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
            y += dec_y
        y0, y1 = 0, LARGEUR
        x = 0
        while x <= LARGEUR:
            canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
            x += dec_x

    def mouvement():
        if cpt % 2 == 1:
            for rectangle in liste_rectangle:
                rebond1(rectangle)
                canvas.move(rectangle[0][0], rectangle[0][1], rectangle[0][2])
            canvas.after(30, mouvement)
            bouton.config(text='Arrêter')
        else:
            bouton.config(text='Démarrer')
    
    def change_text(event):
        nonlocal cpt
        if event.widget == bouton:
            cpt += 1

    def rebond1(rectangle):
        if canvas.coords(rectangle[0][0])[0] < rectangle[1][0] or \
                    canvas.coords(rectangle[0][0])[2] > rectangle[1][2]:
            rectangle[0][1] *= -1
        if canvas.coords(rectangle[0][0])[1] < rectangle[1][1] or \
                    canvas.coords(rectangle[0][0])[3] > rectangle[1][3]:
            rectangle[0][2] *= -1

    root = tk.Tk()
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=LARGEUR, height=HAUTEUR, bg='black')
    canvas.grid()
    quadrillage(6, 5)
    bouton = tk.Button(root, text='Démarrer', command=mouvement)
    bouton.grid(row=1)

    root.bind('<Button-1>', change_text)

    root.mainloop()

# exercice_1()
# exercice_2()