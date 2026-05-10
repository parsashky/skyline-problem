import tkinter as tk
from functools import cmp_to_key

def func(a, b):
    if a[0] != b[0]:
        return a[0] - b[0]
    return a[1] - b[1]

buildings = [
    [1, 11, 5], [2, 6, 7], [3, 13, 9],
    [12, 7, 16], [14, 3, 25],
    [19, 18, 22], [23, 13, 29], [24, 4, 28]
]

wall = []
for i in range(len(buildings)):
    left = buildings[i][0]
    height = buildings[i][1]
    right = buildings[i][2]
    wall.append([left, -height, i])
    wall.append([right, height, i])

wall.sort(key=cmp_to_key(func))

WIDTH, HEIGHT = 1100, 420
SCALE_X, SCALE_Y = 25, 12

root = tk.Tk()
root.title("Skyline - Step by Step")

canvas = tk.Canvas(root, width=800, height=HEIGHT, bg="white")
canvas.pack(side=tk.LEFT)

panel = tk.Frame(root, width=300)
panel.pack(side=tk.RIGHT, fill=tk.Y)

status = tk.Label(panel, font=("Arial", 11), justify="left")
status.pack(pady=10)

heap_box = tk.Listbox(panel, font=("Consolas", 11), height=14)
heap_box.pack(padx=10, pady=5, fill=tk.BOTH)

btn = tk.Button(panel, text="Next Step ▶", font=("Arial", 13))
btn.pack(pady=10)

activeBuildings = set()
leftWallHeight = set([0])
skyline = []
top = 0
step = 0

def drawBuildings():
    for i, (l, h, r) in enumerate(buildings):
        if i in activeBuildings:
            if h == top:
                color = "#0066ff"
            else:
                color = "#1f8640"
        else:
            color = "#9e4d4d"

        canvas.create_rectangle(
            l*SCALE_X, HEIGHT,
            r*SCALE_X, HEIGHT - h*SCALE_Y,
            fill=color, outline="black"
        )

def drawSkyline():
    for i in range(1, len(skyline)):
        x1, y1 = skyline[i-1]
        x2, _ = skyline[i]
        canvas.create_line(
            x1*SCALE_X, HEIGHT - y1*SCALE_Y,
            x2*SCALE_X, HEIGHT - y1*SCALE_Y,
            fill="red", width=3
        )

def updateHeap():
    heap_box.delete(0, tk.END)
    for h in sorted(leftWallHeight, reverse=True):
        mark = " <==" if h == top else ""
        heap_box.insert(tk.END, f"{h}{mark}")

def nextStep():
    global step, top

    if step >= len(wall):
        status.config(text="Finished")
        return

    x, h, idx = wall[step]
    step += 1

    if h < 0:
        activeBuildings.add(idx)
        leftWallHeight.add(-h)
        action = f"start building {idx}"
    else:
        activeBuildings.remove(idx)
        leftWallHeight.remove(h)
        action = f"end building {idx}"

    curTop = max(leftWallHeight)
    if curTop != top:
        skyline.append([x, curTop])
        top = curTop

    canvas.delete("all")
    drawBuildings()
    drawSkyline()
    updateHeap()

    status.config(text=f"x={x}\n{action}\ncurrent top={top}")

btn.config(command=nextStep)

drawBuildings()
updateHeap()
root.mainloop()
