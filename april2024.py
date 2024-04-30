# IBM PONDER THIS APRIL 2024

'''
tower of hanoi
0. Take disk "1" from its rod and move it clockwise to another rod.
1. Take disk "1" from its rod and move it counterclockwise to another rod.
2. Take a disk which is not "1" and move it to another rod.

three stacks, a b and c. we will have a list of stacks.
'''

class HanoiPuzzle:
    def __init__(self, n, n_towers = 3):
        self.n_towers = n_towers
        self.n = n
        self.towers = [[i for i in range(n,0,-1)],
                       [],
                       []]
    
    def print(self):
        for tower in self.towers:
            print(tower)
    
    def isWin(self):
        return self.towers == [[],
                               [i for i in range(self.n,0,-1)],
                               []]
        # return not self.towers[0] and not self.towers[2]
    
    def move(self, move_type):
        x = self.indexOfLittlest()
        if type(move_type) == str:
            move_type = int(move_type)
        if move_type == 0:
            self.move0()
        elif move_type == 1:
            self.move1()
        elif move_type == 2:
            self.move2()
    
    def indexOfLittlest(self):
        for i, tower in enumerate(self.towers):
            if tower and tower[-1] == 1:
                return i
        raise(AssertionError,"something's wrong with the towers")

    def move0(self):
        # 0. Take disk "1" from its rod and move it clockwise to another rod.
        x = self.indexOfLittlest() # always succeeds
        self.towers[(x+1)%3].append(self.towers[x].pop())

    def move1(self):
        # 1. Take disk "1" from its rod and move it counterclockwise to another rod.
        x = self.indexOfLittlest() #always succeeds
        self.towers[(x-1)%3].append(self.towers[x].pop())

    def move2(self):
        # 2. Take a disk which is not "1" and move it to another rod.
        x = self.indexOfLittlest()
        
        # every ring is stacked in one tower
        if not self.towers[(x + 1) % 3] and not self.towers[(x - 1) % 3]:
            return
        
        # one tower exists and the other is empty
        elif not self.towers[(x + 1) % 3] and self.towers[(x - 1) % 3]:
            self.towers[(x + 1) % 3].append(self.towers[(x - 1) % 3].pop())
            return
        elif self.towers[(x + 1) % 3] and not self.towers[(x - 1) % 3]:
            self.towers[(x - 1) % 3].append(self.towers[(x + 1) % 3].pop())
            return

        # both towers have items and should be compared
        if self.towers[(x + 1) % 3][-1] > self.towers[(x - 1) % 3][-1]:
            middle = (x - 1) % 3
            largest = (x + 1) % 3
        else:
            middle = (x + 1) % 3
            largest = (x - 1) % 3
        self.towers[largest].append(self.towers[middle].pop())


def compute(puzzle, move_string, n_steps):
    for step in range(n_steps):
        puzzle.move(int(move_string[(step) % len(move_string)]))
    return puzzle.isWin()

def computeBoth(p1, m1, p2, m2, steps):
    for step in range(steps):
        p1.move(int(m1[(step) % len(m1)]))
        p2.move(int(m2[step % len(m2)]))
    print("P1: ", p1.isWin())
    print("P2: ", p2.isWin())


def stepsToWin(puzzle, move_string):
    i = 0
    while True:
        puzzle.move(move_string[i % len(move_string)])
        i += 1
        if puzzle.isWin():
            return i
        if i > 10000:
            return False

def stepsToWinBoth(puzzle1, move_string1, puzzle2, move_string2, upper_bound = 10000):
    #find the number of steps it takes until both games are in a winnning state
    i = 0
    while True:
        puzzle1.move(int(move_string1[i % len(move_string1)]))
        puzzle2.move(int(move_string2[i % len(move_string2)]))
        i += 1
        if puzzle1.isWin() and puzzle2.isWin():
            return i
        if i > upper_bound:
            return False

def stepsToWinMany(puzzles, movestrings, upper_bound = 10000000):
    i = 0
    while True:
        for x in range(len(puzzles)):
            puzzles[x].move(movestrings[x][i % len(movestrings[x])])
        i += 1
        if all([puzzle.isWin() for puzzle in puzzles]):
            return i
        if i > upper_bound:
            return False

A = HanoiPuzzle(7)
moveA = "12021121120020211202121"
B = HanoiPuzzle(10)
moveB = "0211202112002"

print(stepsToWinBoth(A, moveA, B, moveB, upper_bound=70000000))
# >>> 16511310

A = HanoiPuzzle(7)
moveA = "12021121120020211202121"
B = HanoiPuzzle(10)
moveB = "0211202112002"
C = HanoiPuzzle(9)
moveC = "20202020021212121121202120200202002121120202112021120020021120211211202002112021120211200212112020212120211"
print(stepsToWinMany([A,B,C],[moveA,moveB,moveC],2000000000))
# >>> 1169723214