import random
import os

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


def clear(): return os.system('cls')


# define array
arr = [["#", "#", "#", "#", "#", "#", "#", "#"],
       ["#", ".", ".", ".", ".", ".", ".", "#"],
       ["#", ".", "#", "#", "#", ".", ".", "#"],
       ["#", ".", ".", ".", "#", ".", "#", "#"],
       ["#", "X", "#", ".", ".", ".", ".", "#"],
       ["#", "#", "#", "#", "#", "#", "#", "#"]]

# fungsi cetak map


def cetak_map():

    print()

    for i in arr:
        print(i)
    print()


print("Tampilkan Area sebelum ada lokasi Treasure")
cetak_map()

# inisialisai status treasure_ketemu
treasure_ketemu = False

# inisialiasi jejak arah
jejak_arah = []

# inisialisai awal koordinat xy
x = 0
y = 0

# random lokasi $ di koordinat yang valuenya titik (.)
free_area = False
while (free_area != True):
    x = random.randint(0, 5)
    y = random.randint(0, 7)

    # set lokasi tresure($) jika lokasi berisi tanda titik (.) /area bebas
    if arr[x][y] == ".":

        free_area = True
        # set lokasi tresure
        arr[x][y] = "$"


print("Tampilkan Area setelah ada lokasi Treasure (Random)")
cetak_map()


# ----------------- MULAI MENCARI TREASUE-------------------
# set lokasi awal X
pointer = {}
pointer['x'] = 4
pointer['y'] = 1


def geser_bawah(_pointer, map):

    _treasure_ketemu = False
    _free_area = False

    x = _pointer['x'] + 1
    y = _pointer['y']

    if map[x][y] == "$":
        _treasure_ketemu = True
    elif ((map[x][y] == ".") or (map[x][y] == "X")):
        _free_area = True
        _pointer['x'] = x
        _pointer['y'] = y
        arr[x][y] = "X"
        jejak_arah.append("DOWN")
        print("GESER BAWAH")

    return _pointer, _free_area, _treasure_ketemu


def geser_kiri(_pointer, map):

    _treasure_ketemu = False
    _free_area = False

    x = _pointer['x']
    y = _pointer['y']-1

    if map[x][y] == "$":
        _treasure_ketemu = True
    elif ((map[x][y] == ".") or (map[x][y] == "X")):
        _free_area = True
        _pointer['x'] = x
        _pointer['y'] = y
        arr[x][y] = "X"
        jejak_arah.append("LEFT")
        print("GESER KIRI")

    return _pointer, _free_area, _treasure_ketemu


def geser_kanan(_pointer, map):

    _treasure_ketemu = False
    _free_area = False

    x = _pointer['x']
    y = _pointer['y'] + 1

    if map[x][y] == "$":
        _treasure_ketemu = True
    elif ((map[x][y] == ".") or (map[x][y] == "X")):
        _free_area = True
        _pointer['x'] = x
        _pointer['y'] = y
        arr[x][y] = "X"
        jejak_arah.append("RIGHT")
        print("GESER KANAN")

    return _pointer, _free_area, _treasure_ketemu


def geser_atas(_pointer, map):

    _treasure_ketemu = False
    _free_area = False

    x = _pointer['x']-1
    y = _pointer['y']

    if map[x][y] == "$":
        _treasure_ketemu = True
    elif ((map[x][y] == ".") or (map[x][y] == "X")):
        _free_area = True
        _pointer['x'] = x
        _pointer['y'] = y
        arr[x][y] = "X"
        jejak_arah.append("UP")
        print("GESER ATAS")

    return _pointer, _free_area, _treasure_ketemu

# fungsi untuk menangakap event dari keyboard


def key(event):

    _treasure_ketemu = False

    if event.keysym == 'Escape':
        root.destroy()
    else:
        if(event.keysym == "Up"):
            _treasure_ketemu = geser_atas(pointer, arr)[2]
        elif(event.keysym == "Down"):
            _treasure_ketemu = geser_bawah(pointer, arr)[2]
        elif(event.keysym == "Right"):
            _treasure_ketemu = geser_kanan(pointer, arr)[2]
        elif(event.keysym == "Left"):
            _treasure_ketemu = geser_kiri(pointer, arr)[2]

        # bersihkan layar console
        clear()

        # cetak hasil
        cetak_map()
        print("Log : ")
        print(jejak_arah)
        print()
        if(_treasure_ketemu):
            print("TREASURE FOUND")


root = tk.Tk()
print()
print("Silahkan Gunakan tombol Arah KIRI,KANAN,ATAS & BAWAH pada Keyboard dan (Escape untuk exit) :")
root.bind_all('<Key>', key)
root.withdraw()
root.mainloop()
