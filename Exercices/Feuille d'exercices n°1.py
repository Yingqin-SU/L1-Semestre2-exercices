import tkinter as tk

def exercice_1():

    color = 'red'

    def change_color(event):
        nonlocal color
        if color == None:
            pass
        elif 100 < event.x < 400 and 100 < event.y < 300:
            color = 'blue' if color == 'red' else 'red'
            canvas.itemconfig(rectangle, fill = color)
        else:
            color = None
    
    def redemarrer():
        nonlocal color
        color = 'red'
        canvas.itemconfig(rectangle, fill=color)
    
    root = tk.Tk()

    canvas = tk.Canvas(root, bg='black', height=500, width=500)
    canvas.grid(column=0, row=0)

    bouton = tk.Button(root, text='Recommencer', command=redemarrer)
    bouton.grid(row=1)
    rectangle = canvas.create_rectangle((100, 100), (400, 300), fill="red")

    root.bind('<Button-1>', change_color)

    root.mainloop()

def exercice_2():

    liste = []
    canvas_item = []
    etat = 'Pause'

    def clique(event):
        nonlocal liste
        if event.widget == canvas and type(liste) == list:
            liste.append((event.x, event.y))
        if len(liste) == 2:
            canvas_item.append(canvas.create_line(liste[0], liste[1], fill='blue'))
        elif len(liste) == 4:
            canvas_item.append(canvas.create_line(liste[2], liste[3], fill='red'))
        elif len(liste) == 6:
            for i in canvas_item:
                canvas.delete(i)
            liste = []

    def restart():
        nonlocal etat, liste
        if etat == 'Pause':
            etat = 'Restart'
            liste = tuple(liste)
        elif etat == 'Restart':
            etat = 'Pause'
            liste = list(liste)
        bouton.configure(text=etat)

    root = tk.Tk()

    canvas = tk.Canvas(root, bg='white', height=500, width=500)
    canvas.grid(column=0, row=0)

    bouton = tk.Button(root, text='Pause', command=restart)
    bouton.grid(row=1)

    
    root.bind('<Button-1>', clique)

    root.mainloop()

def exercice_3():
    objects_croix = []
    objects_carres = []
    objects_cercles = []

    def clique(event):
        if event.x < 500 / 3 and len(objects_croix) < 4:
            objects_croix.append(canvas.create_line(event.x-50, event.y-50, event.x+50, event.y+50, fill='red'))
            objects_croix.append(canvas.create_line(event.x+50, event.y-50, event.x-50, event.y+50, fill='red'))
        elif (500/3) < event.x < (500/3*2) and len(objects_carres) < 3:
            objects_carres.append(canvas.create_rectangle(event.x-50, event.y-50, event.x+50, event.y+50, fill='red'))
        elif event.x > 500/3*2 and len(objects_cercles) < 3:
            objects_cercles.append(canvas.create_oval(event.x-50, event.y-50, event.x+50, event.y+50, fill='red'))

    def redemarrer():
        nonlocal objects_croix, objects_carres, objects_cercles
        for croix in objects_croix:
            canvas.delete(croix)
        for carre in objects_carres:
            canvas.delete(carre)
        for cercle in objects_cercles:
            canvas.delete(cercle)
        objects_croix = []
        objects_carres = []
        objects_cercles = []

    racine = tk.Tk()
    canvas = tk.Canvas(racine, width=550, height=550, bg="black")
    canvas.grid(column=0, row=0)

    bouton = tk.Button(text="Redémarrer", foreground='blue', font=("Helvetica", "25"), activeforeground="red", activebackground="black", padx=10, command=redemarrer)
    bouton.grid(column=0, row=1)

    canvas.create_line(550/3, 0 , 550/3, 550, fill='white')
    canvas.create_line(550/3*2, 0, 550/3 * 2, 550, fill='white')

    canvas.bind("<Button-1>", clique)

    racine.mainloop()

def exercice_4():
    rayon = 25
    etat = 'Pause'

    def pause():
        nonlocal etat, rayon
        if etat == 'Restart':
            etat = 'Pause'
            rayon = int(rayon)
        else:
            etat = 'Restart'
            rayon = str(rayon)
        bouton.configure(text=etat)

    def clique(event):
        nonlocal rayon
        if type(rayon) == int:
            if 250 - rayon < event.x < 250 + rayon and 250 - rayon < event.y < 250 + rayon:
                if rayon >= 15:
                    rayon -= 5
                    canvas.coords(rectangle, 250 - rayon, 250 - rayon, 250 + rayon, 250 + rayon)
            else:
                if event.widget == canvas and rayon <= 100:
                    rayon += 5
                    canvas.coords(rectangle, 250 - rayon, 250 - rayon, 250 + rayon, 250 + rayon)

    root = tk.Tk()

    canvas = tk.Canvas(root, bg='white', height=500, width=500)
    canvas.grid(column=0, row=0)
    rectangle = canvas.create_rectangle((250 - rayon, 250 - rayon), (250 + rayon, 250 + rayon), fill='red')

    bouton = tk.Button(root, text='Pause', command=pause)
    bouton.grid(row=1)

    
    root.bind('<Button-1>', clique)

    root.mainloop()


def exercice_5():

    cpt = 0
    firstline_x = 200
    secondline_x = 400
    firstline_move = 0
    secondline_move = 0
    
    def recommencer():
        nonlocal firstline_x, secondline_x, firstline, secondline
        canvas.delete(firstline)
        canvas.delete(secondline)
        firstline_x = 200
        secondline_x = 400
        firstline = canvas.create_line((firstline_x, 0), (firstline_x, 600), fill='red')
        secondline = canvas.create_line((secondline_x, 0), (secondline_x, 600), fill='blue')

    def clique(event):
        nonlocal cpt, firstline_x, firstline_move, secondline_x, secondline_move
        if event.widget == canvas:
            if firstline_x > event.x:
                firstline_move = -10
            else:
                firstline_move = 10
            firstline_x += firstline_move
            if secondline_x > event.x:
                secondline_move = -10
            else:
                secondline_move = 10
            secondline_x +=  secondline_move
            canvas.move(firstline, firstline_move, 0)
            canvas.move(secondline, secondline_move, 0)
        if cpt % 2 == 0:
            canvas.itemconfig(firstline, fill='blue')
            canvas.itemconfig(secondline, fill='red')
        else:
            canvas.itemconfig(firstline, fill='red')
            canvas.itemconfig(secondline, fill='blue')
        cpt += 1

    root = tk.Tk()

    canvas = tk.Canvas(root, bg='white', height=600, width=600)
    canvas.grid(column=0, row=0)
    firstline = canvas.create_line((firstline_x, 0), (firstline_x, 600), fill='red')
    secondline = canvas.create_line((secondline_x, 0), (secondline_x, 600), fill='blue')

    bouton = tk.Button(root, text='Recommencer', command=recommencer)
    bouton.grid(row=1)

    
    root.bind('<Button-1>', clique)

    root.mainloop()

def exercice_6():

    def clique(event):
        nonlocal color
        if event.widget == canvas:
            if 0 < event.x < 50 and 0 < event.y < 50:
                color = 'green'
            elif 0 < event.x < 50 and 50 < event.y < 100:
                color = 'yellow'
            elif 0 < event.x < 50 and 100 < event.y < 150:
                color = 'blue'
            elif event.y < 500 and event.x < 500:
                color = 'black'
            canvas.itemconfig(cercle, fill=color, outline=color)
            liste.append(color)

    def annuler():
        nonlocal liste
        if len(liste) > 1:
            liste = liste[:-1]
            canvas.itemconfig(cercle, fill=liste[-1], outline=liste[-1])

    root = tk.Tk()
    liste = []
    color = 'black'

    canvas = tk.Canvas(root, bg='white', height=500, width=500)
    canvas.grid(column=0, row=0)
    canvas.create_rectangle((0, 0),(50, 50), fill='green')
    canvas.create_rectangle((0, 50),(50, 100), fill='yellow')
    canvas.create_rectangle((0, 100),(50, 150), fill='blue')

    cercle = canvas.create_oval((225, 225), (275, 275), fill='black')

    bouton = tk.Button(root, text='Annuler', command=annuler)
    bouton.grid(row=1)

    
    root.bind('<Button-1>', clique)

    root.mainloop()


# exercice_1()
# exercice_2()
# exercice_3()
# exercice_4()
# exercice_5()
# exercice_6()