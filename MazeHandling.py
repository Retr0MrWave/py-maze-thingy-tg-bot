import MazeGeneration as mg
import random

class Maze:
    def __init__(self, width, height):
        self.maze_arr = mg.generateMaze(width, height)

        potential_player = [1, 1]
        while (self.maze_arr[potential_player[0]][potential_player[1]] != 'c'):
            potential_player = [random.randint(1, width//2), random.randint(1, height//2)]
        self.player = potential_player
        
        potential_exit = [width-1, height-1]
        while (self.maze_arr[potential_exit[0]][potential_exit[1]] != 'c'):
            potential_exit = [random.randint(width//2 + 1, width-1), random.randint(height//2 + 1, height-1)]
        self.exit = potential_exit
    
    def movePlayer(self, direction):
        x, y = self.player[0], self.player[1]
        if direction == 'w':
            if self.maze_arr[x-1][y] != 'w':
                self.player[0] -= 1
        elif direction == 's':
            if self.maze_arr[x+1][y] != 'w':
                self.player[0] += 1
        elif direction == 'a':
            if self.maze_arr[x][y-1] != 'w':
                self.player[1] -= 1
        elif direction == 'd':
            if self.maze_arr[x][y+1] != 'w':
                self.player[1] += 1
    
    def mazeToString(self):
        res = ""
        for i in range(0, len(self.maze_arr)):
            for j in range(0, len(self.maze_arr[0])):
                if [i, j] == self.player:
                    res += "@ "
                elif [i, j] == self.exit:
                    res += "E "
                elif self.maze_arr[i][j] == 'w':
                    res += "▮ "
                elif self.maze_arr[i][j] == 'c':
                    res += "▯ "
                else:
                    res += str(self.maze_arr[i][j]) + " "    
            res += '\n'
        return res
