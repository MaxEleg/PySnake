from tkinter import *
from random import randrange
from Snake import Snake


# Déclarations des fonctions

# Cette fonction permet de réinitialiser le jeu

def new_game():
    global dx, dy, x, y, eat, flag, snake, fullSnake, coord_fullSnake, direction, coord_eyes, eyes, score, f, flag2

    flag2 = 0

    can1.delete(ALL)

    can1.create_rectangle(0, 0, 10, 300, fill="black")
    can1.create_rectangle(0, 0, 500, 10, fill="black")
    can1.create_rectangle(490, 0, 500, 300, fill="black")
    can1.create_rectangle(0, 300, 500, 290, fill="black")

    snake.reset()

    fullSnake = [can1.create_rectangle(snake.body[0][0], snake.body[0][1], snake.body[0][2], snake.body[0][3], fill="green")]

    eyes = [can1.create_oval(snake.eyes[0][0], snake.eyes[0][1], snake.eyes[0][2], snake.eyes[0][3], fill="yellow")]
    eyes.append(can1.create_oval(snake.eyes[0][4], snake.eyes[0][5], snake.eyes[0][6], snake.eyes[0][7], fill="yellow"))

    eat = 0

    x = randrange(10, 480, 10)
    y = randrange(10, 280, 10)
    f = can1.create_oval(x, y, x + 10, y + 10, fill="red")

    dx = 5
    dy = 0
    direction = 2
    score = 0

    if flag == 0:
        flag = 1
        move()

# Cette fonction permet d'effectuer une pause en cours de partie

def pause(event):
    global flag, pause, flag2
    if flag2 != 1:
        if flag == 1:
            pause = can1.create_text(250, 150, font=('Fixedsys', 18), text="PAUSE")
            flag = 0
        elif flag == 0:
            flag = 1
            can1.delete(pause)
            move()


# Cette fonction va permettre de mettre le serpent en mouvement de manière automatique

def move():
    global dx, dy, x, y, eat, flag, f, fullSnake, snake, coord_fullSnake, direction, coord_eyes, eyes, score, flag2

    # Si le serpent mange une proie on l'allonge d'un carré et cela
    # en fonction de la direction afin que le nouveau carré soit bien
    # dessiné à la suite du dernier carré composant le serpent

    if snake.body[0][0] == x and snake.body[0][1] == y:
        can1.delete(f)
        eat = 1
        coord = len(snake.body[0])#len(coord_fullSnake)
        score = score + 100

        #     # On rajoute un nouveau carré dans notre liste de carrés
        coordinates = snake.moveHead(direction)
        fullSnake.append(can1.create_rectangle(coordinates[0], coordinates[1], coordinates[2], coordinates[3], fill="green"))

    food()

    # Les coordonnées de chaque carré prendront les coordonnées du carré qui le succède
    # cela permettra à chacun des carré de se suivre et d'obtenir l'effet du serpent :)

    i = 4
    j = 1

    snake.moveBody(direction, len(fullSnake), dx, dy)

    i = 4
    j = 1

    # Si le serpent touche le mur la partie s'arrête

    if snake.body[0][0] >= 490 or snake.body[0][0] <= 0 or snake.body[0][1] >= 290 or snake.body[0][1] <= 0:
        flag = 0
        flag2 = 1
        loose = can1.create_text(250, 150, font=('Fixedsys', 18), text="Score : " + str(score))

    # Si les coordonnées du 1er carré sont égales aux coordonnées d'un des autres carrés composant le serpent
    # cela signifie qu'il s'est recoupé par conséquent la partie s'arrête :p


    while j < len(fullSnake):
        if snake.body[0][0] == snake.body[0][i] and snake.body[0][1] == snake.body[0][i + 1] and snake.body[0][2] == \
                snake.body[0][i + 2] and snake.body[0][3] == snake.body[0][i + 3]:
            flag = 0
            flag2 = 1
            loose = can1.create_text(250, 150, font=('Fixedsys', 18), text="Score : " + str(score))
        i += 4
        j += 1

    i = 0
    j = 0

    if flag != 0:

        # On redéfinie les coordonnées des yeux de notre cher serpent

        can1.coords(eyes[0], snake.eyes[0][0], snake.eyes[0][1], snake.eyes[0][2], snake.eyes[0][3])
        can1.coords(eyes[1], snake.eyes[0][4], snake.eyes[0][5], snake.eyes[0][6], snake.eyes[0][7])

        while j < len(fullSnake):
            # On redéfinie les coordonnées de chacun des carré
            # composant le corps du serpent

            can1.coords(fullSnake[j], snake.body[0][i], snake.body[0][i + 1], snake.body[0][i + 2], snake.body[0][i + 3])

            i += 4
            j += 1

    if flag > 0:
        fen1.after(50, move)


# Cette fonction va permettre de générer au hasard de la nourriture dans le canevas

def food():
    global eat, x, y, f, snake
    if eat == 1:
        x = randrange(10, 480, 10)
        y = randrange(10, 280, 10)
        i = 0
        i2 = 0

        # Afin d'éviter de générer de la nourriture sur le serpent
        # j'utilise ce bout de code qui s'occupera de générer un nouveau de tas de nourriture
        # si les coordonnées du précédent sont égales aux coordonnées d'un carré composant
        # le corps du serpent

        while i < len(snake.body[0]):
            i2 = 1
            if x == snake.body[0][i] and y == snake.body[0][i + 1]:
                while x == snake.body[0][i] and y == snake.body[0][i + 1]:
                    x = randrange(10, 480, 10)
                    y = randrange(10, 280, 10)
                i = 0
                i2 = 0
            if i2 == 1:
                i += 4
        f = can1.create_oval(x, y, x + 10, y + 10, fill="red")
        eat = 0


# Ces fonction vont permettrent de contrôler le serpent
# à l'aide des touches fléchées du clavier

def left(event):
    global dx, dy, direction, coord_fullSnake, coord_eyes, eyes
    if direction != 2:
        dx = -5
        dy = 0
        direction = 1


def right(event):
    global dx, dy, direction
    if direction != 1:
        dx = 5
        dy = 0
        direction = 2


def up(event):
    global dx, dy, direction
    if direction != 4:
        dx = 0
        dy = -5
        direction = 3


def down(event):
    global dx, dy, direction
    if direction != 3:
        dx = 0
        dy = 5
        direction = 4

# Définition du canevas (espace de jeu)

fen1 = Tk()
fen1.title("SNAKE")
can1 = Canvas(fen1, width=500, height=300, bg="light blue")

# Définition des touches qui permettront de déplacer le serpent

can1.bind_all("<Left>", left)
can1.bind_all("<Right>", right)
can1.bind_all("<Up>", up)
can1.bind_all("<Down>", down)
can1.bind_all("<p>", pause)

can1.grid(row=0, column=0, rowspan=10)

# On crée le bouton New game qui va permettre de réinitialiser la partie

Button(fen1, text="New game", font=("Fixedsys"), command=new_game).grid(row=4, column=1, sticky=N, padx=5)
Button(fen1, text="Quit", font=("Fixedsys"), command=fen1.destroy).grid(row=6, column=1, sticky=N)

# Délimitations des limites (Création des murs)
# que le serpent ne doit outre passer pour ne pas finir dans le mur

can1.create_rectangle(0, 0, 10, 300, fill="black")
can1.create_rectangle(0, 0, 500, 10, fill="black")
can1.create_rectangle(490, 0, 500, 300, fill="black")
can1.create_rectangle(0, 300, 500, 290, fill="black")

# Création du serpent

snake = Snake()

# Définition des coordonnées de départ du serpent

fullSnake = [ can1.create_rectangle(snake.body[0][0], snake.body[0][1], snake.body[0][2], snake.body[0][3], fill="green")]

# On lui dessine ses yeux

eyes = [can1.create_oval(snake.eyes[0][0], snake.eyes[0][1], snake.eyes[0][2], snake.eyes[0][3], fill="yellow")]
eyes.append(can1.create_oval(snake.eyes[0][4], snake.eyes[0][5], snake.eyes[0][6], snake.eyes[0][7], fill="yellow"))

# Définition du drapeau ( indicateur permettant d'arrêter le programme )

flag = 1
eat = 0

# On dessine le 1er tas de nourriture

x = randrange(10, 480, 10)
y = randrange(10, 280, 10)
f = can1.create_oval(x, y, x + 10, y + 10, fill="red")

# Définition des pas d'avancement du serpent

dx = 5
dy = 0

# Etant donné que le serpent avance vers la droite
# on assigne 2 à direction qui correspond à la
# fonction right() afin que rien ne soit chamboulé

direction = 2

# Le compteur de score

score = 0
pause = 0

# Ce compteur va permettre de ne pas remettre
# le jeu en route à l'aide de la touche pause
# dans le cas où le joueur aurait perdu :p

flag2 = 0
move()
fen1.mainloop()

