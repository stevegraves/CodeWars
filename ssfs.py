# Initial solution
def super_street_fighter_selection(f, p, m):
    output = []
    pos_y = p[0]
    pos_x = p[1]
    for x in m:
        if x == 'up':
            if pos_y - 1 < 0:
                output.append(f[pos_y][pos_x])
            elif f[pos_y - 1][pos_x] == '':
                output.append(f[pos_y][pos_x])
            else:
                pos_y -= 1
                output.append(f[pos_y][pos_x])
        if x == 'down':
            if pos_y + 1 > len(f) - 1:
                output.append(f[pos_y][pos_x])
            elif f[pos_y + 1][pos_x] == '':
                output.append(f[pos_y][pos_x])
            else:
                pos_y += 1
                output.append(f[pos_y][pos_x])

        if x == 'left':
            if (pos_x - 1) < 0:
                pos_x = len(f[0]) - 1
            else:
                pos_x -= 1
            while not f[pos_y][pos_x]:
                if (pos_x - 1) < 0:
                    pos_x = len(f[0]) - 1
                else:
                    pos_x -= 1
            output.append(f[pos_y][pos_x])

        if x == 'right':
            if (pos_x + 1) > len(f[0]) - 1:
                pos_x = 0
            else:
                pos_x += 1
            while not f[pos_y][pos_x]:
                if (pos_x + 1) > len(f[0]) - 1:
                    pos_x = 0
                else:
                    pos_x += 1
            output.append(f[pos_y][pos_x])
    return output

# Best practice
"""
MOVES = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

def super_street_fighter_selection(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dy, dx = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters) or not fighters[y][x]:
            y -= dy
        x = (x + dx) % len(fighters[y])
        while not fighters[y][x]:
            x = (x + dx) % len(fighters[y])
        hovered_fighters.append(fighters[y][x])
    return hovered_fighters



fighters4 = [
	[        "",     "Ryu",  "E.Honda",  "Cammy" ],
	[  "Balrog",     "Ken",  "Chun Li",       "" ],
	[    "Vega",        "", "Fei Long", "Balrog",],
    [  "Blanka",   "Guile",         "", "Chun Li"],
    [ "M.Bison", "Zangief",  "Dhalsim", "Sagat"  ],
    [  "Deejay",   "Cammy",         "", "T.Hawk" ]
]

position = (3,3)

moves =  ["left"]*2+["down"]+["right"]*4+["down"]+["left"]*4+["up"]+["right"]*2+["up"]+["right"]*3

super_street_fighter_selection(fighters4, position, moves)
"""


