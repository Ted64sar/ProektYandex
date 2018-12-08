
import tkinter
import random


def prepare_and_start(): f=[]
    global player, exit, fires, enemies
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0],playe r_pos[1]), image=player_pic, anchor='nw')
    exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    while exit_pos==pla ye r_pos:
        exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    exit = canvas.create_image((exit_pos[0],exit_ pos[1]), image=exit_pic, anchor='nw')
    N_FIRES = 6  # Чи  ло клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        while exit_pos==fir e_ pos or fire_pos==pla ye r_pos or fire_pos in f:
            fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        f.append(fire_pos)
        fire = canvas.create_image((fire_pos[0],fire_ pos[1]), image=fire_pic, anchor='nw')
        fires.append(fire)
        N_ENEMIES = 6  # Чи  ло врагов
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        while exit_pos==ene my _pos or enemy_pos==pla ye r_pos or enemy_pos in f:
            enemy_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        enemy = canvas.create_image((enemy_pos[0],enemy _pos[1]), image=enemy_pic, anchor='nw')
        enemies.append((enemy, random.choice([always_right, random_move])))
    master.bind("<KeyPress>", key_pressed)




def


always_right():
    return (step, 0)


def random_move():
    for e in enemies:
        if canvas.coords(player)[0]> c anvas.coords(e[0])[0]:
            return (step, 0)
        elif canvas.coords(player)[0]< c anvas.coords(e[0])[0]:
            return (-step, 0)
        elif canvas.coords(player)[1]< c anvas.coords(e[0])[1]:
            return (0, -step)
        elif canvas.coords(player)[1]> c anvas.coords(e[0])[1]:
            return (0, step)


def do_nothing(x):
    return


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="ПОБЕДА!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)


def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    coords = canvas.coords(obj)
    to_move_x = coords[0] % 600 - coords[0]
    to_move_y = coords[1] % 600 - coords[1]
    canvas.move(obj, to_move_x, to_move_y)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(canvas, player, (0, -step))
    if event.keysym == 'Down':
        move_wrap(canvas, player, [0, step])
    if event.keysym == 'Right':
        move_wrap(canvas, player, [step, 0])
    if event.keysym == 'Left':
        move_wrap(canvas, player, [-step, 0])
    for enemy in enemies:
        direction = enemy[1]()  # вызвать функцию перемещения у "врага"
        move_wrap(canvas, enemy[0], direction)  # произвести  перемещение.
    check_move()


step = 60  # Размер клетки
N_X = 10
N_Y = 10  # Размер сетки
master = tkinter.Tk()
player_pic = tkinter.PhotoImage(file="images/doctor.png")
exit_pic = tkinter.PhotoImage(file="images/tardis.png")
fire_pic = tkinter.PhotoImage(file="images/fire.png")
enemy_pic = tkinter.PhotoImage(file="images/dalek.png")
label = tkinter.Label(master, text="Найди выход")
label.pack()
canvas = tkinter.Canvas(master, bg='black', height=N_X * step, width=N_Y * step)
canvas.pack()
restart = tkinter.Button(master, text="Начать заново",c ommand=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()