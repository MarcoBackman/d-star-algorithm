

def stateNameToCoords(name):
    '''                   x  y
        from x1y2 return [1, 2]
        from x5y4 return [5, 4]
    '''


    return [
        int(name.split('x')[1].split('y')[0]), 
        int(name.split('x')[1].split('y')[1])
    ]

# util function to display the path to the goal
def displayPath():
    pass


# add obstacles to the grid
def addObstacles():
    pass



# save output snapshots of grid
def saveGrid():
    pass 


# save output snapshots of grid
def profile():
    pass
