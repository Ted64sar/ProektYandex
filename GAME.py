import tkinter
import random
import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow
#from ui_file import Ui_MainWindow


def prepare_and_start():

    label.config(text="Найди выход")
    f = []
    global player, exit, fires, enemies, bosses
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0], player_pos[1]), image=player_pic, anchor='nw')
    exit_pos = (random.randint(2, N_X - 2) * step, random.randint(2, N_Y - 2) * step)
    while exit_pos == player_pos:
        exit_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    exit = canvas.create_image((exit_pos[0], exit_pos[1]), image=exit_pic, anchor='nw')

    N_FIRES = 5 * regim
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        while exit_pos == fire_pos or fire_pos == player_pos or fire_pos in f:
            fire_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        f.append(fire_pos)
        fire = canvas.create_image((fire_pos[0],fire_pos[1]), image=fire_pic, anchor='nw')
        fires.append(fire)
    N_ENEMIES = 5 + regim * 4
    e = []
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        while exit_pos == enemy_pos or enemy_pos == player_pos or enemy_pos in f:
            enemy_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        e.append(enemy_pos)
        enemy = canvas.create_image((enemy_pos[0], enemy_pos[1]), image=enemy_pic, anchor='nw')
        enemies.append((enemy, random.choice([always_right, random_move, always_up, always_left, always_down, statyk, ePatrul])))
    bosses = []
    if regim >= 3:
        boss_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        while exit_pos == boss_pos or boss_pos == player_pos or boss_pos in f or boss_pos in e:
            boss_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
        boss = canvas.create_image((boss_pos[0],boss_pos[1]), image=boss_pic, anchor='nw')
        bosses.append((boss, random.choice([Hunt, patrul, Hunt, Hunt, patrul, Hunt, BigHunt])))
    master.bind("<KeyPress>", key_pressed)




def settings():

    class MyWidget(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.pushButton.clicked.connect(self.run)

        def run(self):
            f = open('GAME_SETTINGS.txt', 'w')
            # repson
            f.write('R2-D2.png BB8.png R-4.png C3PO.png CHOPPER.png' + '\n')
            if self.radioButton_2.isChecked():
                f.write('1' + '\n')
            elif self.radioButton_3.isChecked():
                f.write('2' + '\n')
            elif self.radioButton_9.isChecked():
                f.write('3' + '\n')
            elif self.radioButton_4.isChecked():
                f.write('4' + '\n')
            elif self.radioButton.isChecked():
                f.write('5' + '\n')
            else:
                f.write('1' + '\n')
            # rpotiv
            f.write('stormtrooper.png death-stormtrooper.png trade-federation-droid.png' + '\n')
            if self.radioButton_6.isChecked():
                f.write('1' + '\n')
            elif self.radioButton_7.isChecked():
                f.write('2' + '\n')
            elif self.radioButton_8.isChecked():
                f.write('3' + '\n')
            else:
                f.write('1' + '\n')
            # prepyat
            f.write('hole.png mine.png bust-droid.png' + '\n')
            if self.radioButton_10.isChecked():
                f.write('1' + '\n')
            elif self.radioButton_11.isChecked():
                f.write('2' + '\n')
            elif self.radioButton_5.isChecked():
                f.write('3' + '\n')
            else:
                f.write('1' + '\n')
            #strazh
            f.write('Fazma.png general_grivus.png grand_inkvizitor.png' + '\n')
            if self.radioButton_12.isChecked():
                f.write('1' + '\n')
            elif self.radioButton_13.isChecked():
                f.write('2' + '\n')
            elif self.radioButton_14.isChecked():
                f.write('3' + '\n')
            else:
                f.write('1' + '\n')
            #level
            if self.radioButton_15.isChecked():
                f.write('1' + '\n')
            elif self.radioButton_16.isChecked():
                f.write('2' + '\n')
            elif self.radioButton_17.isChecked():
                f.write('3' + '\n')
            elif self.radioButton_18.isChecked():
                f.write('4' + '\n')
            else:
                f.write('3' + '\n')

    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
    prepare_and_start


def always_right():
    return (step, 0)

def always_left():
    return (-step, 0)

def always_up():
    return (0, step)

def always_down():
    return (0, -step)

def statyk():
    return (0, 0)

def random_move():
    for e in enemies:
        if canvas.coords(player)[0] > canvas.coords(e[0])[0]:
            return (step, 0)
        elif canvas.coords(player)[0] < canvas.coords(e[0])[0]:
            return (-step, 0)
        elif canvas.coords(player)[1] < canvas.coords(e[0])[1]:
            return (0, -step)
        elif canvas.coords(player)[1] > canvas.coords(e[0])[1]:
            return (0, step)
def BigHunt():
    for b in bosses:
        hway = []
        if canvas.coords(player)[0] > canvas.coords(b[0])[0]:
            hway.append(step)
        elif canvas.coords(player)[0] < canvas.coords(b[0])[0]:
            hway.append(-step)
        else:
            hway.append(-step)
        if canvas.coords(player)[1] > canvas.coords(b[0])[1]:
            hway.append(step)
        elif canvas.coords(player)[1] < canvas.coords(b[0])[1]:
            hway.append(-step)
        else:
            hway.append(-step)
    for e in enemies:
        if e[1] != random_move():
            e[1] = random_move()
    return tuple(hway)


def Hunt():
    for b in bosses:
        hway = []
        if canvas.coords(player)[0] > canvas.coords(b[0])[0]:
            hway.append(step)
        elif canvas.coords(player)[0] < canvas.coords(b[0])[0]:
            hway.append(-step)
        else:
            hway.append(-step)
        if canvas.coords(player)[1] > canvas.coords(b[0])[1]:
            hway.append(step)
        elif canvas.coords(player)[1] < canvas.coords(b[0])[1]:
            hway.append(-step)
        else:
            hway.append(-step)
    return tuple(hway)

def ePatrul():
    for b in enemies:
        hway = []
        flag = True
        if canvas.coords(exit)[0] == canvas.coords(b[0])[0]:
            flag = False
            hway = (0, step)

        elif canvas.coords(exit)[0] > canvas.coords(b[0])[0] and flag:
            hway.append(step)
        elif canvas.coords(exit)[0] < canvas.coords(b[0])[0] and flag:
            hway.append(-step)
        elif flag:
            hway.append(-step)
        if canvas.coords(exit)[1] > canvas.coords(b[0])[1] and flag:
            hway.append(step)
        elif canvas.coords(exit)[1] < canvas.coords(b[0])[1] and flag:
            hway.append(-step)
        elif flag:
            hway.append(-step)
        elif canvas.coords(exit)[0] > canvas.coords(b[0])[0] and not(flag):
            hway = (step, step)
        elif canvas.coords(exit)[0] < canvas.coords(b[0])[0] and not(flag):
            hway = (-step, -step)
        elif canvas.coords(exit)[1] < canvas.coords(b[0])[0] and not(flag):
            hway = (step, -step)
        elif canvas.coords(exit)[1] < canvas.coords(b[0])[0] and not(flag):
            hway = (-step, step)


    return tuple(hway)

def patrul():
    for b in bosses:
        hway = []
        flag = True
        if canvas.coords(exit)[0] == canvas.coords(b[0])[0]:
            flag = False
            hway = (0, step)

        elif canvas.coords(exit)[0] > canvas.coords(b[0])[0] and flag:
            hway.append(step)
        elif canvas.coords(exit)[0] < canvas.coords(b[0])[0] and flag:
            hway.append(-step)
        elif flag:
            hway.append(-step)
        if canvas.coords(exit)[1] > canvas.coords(b[0])[1] and flag:
            hway.append(step)
        elif canvas.coords(exit)[1] < canvas.coords(b[0])[1] and flag:
            hway.append(-step)
        elif flag:
            hway.append(-step)
        elif canvas.coords(exit)[0] > canvas.coords(b[0])[0] and not(flag):
            hway = (step, step)
        elif canvas.coords(exit)[0] < canvas.coords(b[0])[0] and not(flag):
            hway = (-step, -step)
        elif canvas.coords(exit)[1] < canvas.coords(b[0])[0] and not(flag):
            hway = (step, -step)
        elif canvas.coords(exit)[1] < canvas.coords(b[0])[0] and not(flag):
            hway = (-step, step)


    return tuple(hway)



def do_nothing(x):
    return


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="ПОБЕДА!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Поражение!")
            master.bind("<KeyPress>", do_nothing)
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text="Поражение!")
            master.bind("<KeyPress>", do_nothing)
    for b in bosses:
        if canvas.coords(player) == canvas.coords(b[0]):
            label.config(text="Поражение!")
            master.bind("<KeyPress>", do_nothing)


def move_wrap(canvas, obj, move):
    canvas.move(obj, move[0], move[1])
    coords = canvas.coords(obj)
    to_move_x = coords[0] % 720 - coords[0]
    to_move_y = coords[1] % 720 - coords[1]
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
    if event.keysym == 'Space':
        move_wrap(canvas, player, [0, 0])
    for enemy in enemies:
        direction = enemy[1]()
        move_wrap(canvas, enemy[0], direction)
    for boss in bosses:
        direction = boss[1]()
        move_wrap(canvas, boss[0], direction)

    check_move()


step = 60
N_X = 12
N_Y = 12
master = tkinter.Tk()
with open('GAME_SETTINGS.txt', 'r') as inp:
    f = inp.read().split('\n')[0::]
    files = f[::2]
    ind = f[1::2]
regim = int(files[4]) - 1
label = tkinter.Label(master, text="Найди выход")
label.pack()
restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start)
restart.pack()
settings = tkinter.Button(master, text="Настройки", command=settings)
settings.pack()
canvas = tkinter.Canvas(master, bg='black', height=N_X * step, width=N_Y * step)
canvas.pack()

player_pic = tkinter.PhotoImage(file="images/"+str(files[0].split()[int(ind[0])-1]))
exit_pic = tkinter.PhotoImage(file="images/tardis.png")
fire_pic = tkinter.PhotoImage(file="images/"+str(files[2].split()[int(ind[2])-1]))
enemy_pic = tkinter.PhotoImage(file="images/"+str(files[1].split()[int(ind[1])-1]))
boss_pic = tkinter.PhotoImage(file="images/"+str(files[3].split()[int(ind[3])-1]))
regim = int(files[4]) - 1

prepare_and_start()
master.mainloop()
