import MazeHandling as mh

def createMaze():
    print("Please enter the width and height of your desired maze:")
    width, height = map(int, input().split())
    if width < 5 or height < 5:
        print("We\'re sorry, but our generation algorithm doesn't work for mazes smaller than 5 in each dimention.")
        exit()
    return mh.Maze(width, height)

def printHelpMessage():
    # TODO: Make a proper help message
    print("We\'ll make this later")

if __name__ == "__main__":
    print("Welcome to maze thingy!")
    current_maze = createMaze()
    while True:
        print(current_maze.mazeToString())
        command = input("Your input: (type h for help)\n")
        if (command == 'q'):
            exit()
        elif (command == 'h'):
            printHelpMessage()
        elif (command == 'r'):
            current_maze = createMaze()
        else:
            print("Unrecognised command. Type h for help.")
