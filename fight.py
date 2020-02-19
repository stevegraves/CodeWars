def fight(r1, r2, tactics):
    while r1['tactics'] or r2['tactics']:
        if r1['speed'] >= r2['speed']:
            if r1['tactics']:
                r2['health'] -= tactics[r1['tactics'][0]]
                r1['tactics'].pop(0)
                if r2['health'] <= 0:
                    return "{} has won the fight.".format(r1['name'])
            if r2['tactics']:
                r1['health'] -= tactics[r2['tactics'][0]]
                r2['tactics'].pop(0)
                if r1['health'] <= 0:
                    return "{} has won the fight.".format(r2['name'])
        else:
            if r2['tactics']:
                r1['health'] -= tactics[r2['tactics'][0]]
                r2['tactics'].pop(0)
                if r1['health'] <= 0:
                    return "{} has won the fight.".format(r2['name'])
            if r1['tactics']:
                r2['health'] -= tactics[r1['tactics'][0]]
                r1['tactics'].pop(0)
                if r2['health'] <= 0:
                    return "{} has won the fight.".format(r1['name'])
    if r1['health'] > r2['health']:
        return "{} has won the fight.".format(r1['name'])
    elif r2['health'] > r1['health']:
        return "{} has won the fight.".format(r2['name'])
    else:
        return "The fight was a draw."



robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"]}
robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21,
           "tactics": ["missile", "missile", "missile", "missile"]}
tactics = {"punch": 20, "laser": 30, "missile": 35}

fight(robot_1, robot_2, tactics)