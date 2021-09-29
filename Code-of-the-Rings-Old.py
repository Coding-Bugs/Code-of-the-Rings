from io import StringIO
from sys import stderr

def errprint(message):
    print(message, file=stderr, flush=True)

class Game:

    def __init__(self, phrase: str):
        self.phrase = phrase
        self.loc = 0
        self.stones = [" " for i in range(30)]
        # self.stones = [" ", "Z", " ", " ", "A", " ", " ", " ", " ", " ",
        #                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
        #                " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.command = ""
        self.string = ""
        self.letDict = {" " : 0, "A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, "K" : 11, "L" : 12, "M" : 13,
                        "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}

    def loop(self, steps: int, tar: int):
        if steps < abs(steps - tar):
            return steps
        else:
            return steps - tar

    def stepsBetweenLetters(self, cur: str, target: str):
        # Get number of steps between the letters 
        n1 = self.letDict[cur]
        n2 = self.letDict[target]
        mod = len(self.letDict)
        steps = ( n2 - n1 ) % mod
        # errprint(f"n1: '{cur}', n2: '{target}', steps: {steps}".format(**locals()))
        # Figure out if I want to loop forwards or backwards

        # Figure out if I want to loop forwards or backwards
        return self.loop(steps, mod)

    def getCommand(self, cur: str, tar: str):
        # Check the current stone
        steps = self.stepsBetweenLetters(cur, tar)
        errprint("Current stone steps: {steps}".format(**locals()))
        

        # # Check if other stones have the letter
        # stone_step = self.checkStones(tar, steps)
        # if stone_step < abs(steps):
        #     pass 
        # errprint("Steps to another stone: {stone_step}".format(**locals()))


        other_step = self.changeStone(tar)
        if other_step[1] < steps:
            pass
        errprint(other_step)
        uId = other_step[0]
        d = self.loc - uId
        st = other_step[1] - uId
        errprint("Steps to stone #{uId}: {d}, cost: {st}".format(**locals()))
        
        # Better to go to different stone
        if other_step[1] < abs(steps):
            idx = other_step[0]
            dist = (idx - self.loc) % len(self.stones)
        # Better to stay on current stone
        else:
            if steps < 0:
                self.command += "-" * abs(steps) + "."
            else:
                self.command += "+" * steps + "."

            self.stones[self.loc] = tar
            self.string += tar

    def checkStones(self, tar: str, steps: int):
        idx = 100
        for i in range(len(game.stones)):
            # errprint("idx: " + str(i) + ", Ch: " + str(self.stones[i]))
            if self.stones[i] == tar:
                # errprint("Matching idx: " + str(i))
                dist = (i - self.loc) % len(game.stones)
                if dist < idx:
                    idx = dist
        if idx != 100:
            return self.loop(idx, len(game.stones))
        else:
            return idx

    def changeStone(self, tar: str):
        idx = 0
        cost = 100
        for i in range(len(game.stones)):
            steps = self.stepsBetweenLetters(self.stones[i], tar)
            # errprint("Steps to stone: " + str(i) + ", steps to change letter: " + str(steps))
            if i + abs(steps) < cost:
                cost = i + abs(steps)
                idx = i
        
        return (idx, cost)
        pass
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



magic_phrase = input()
errprint(magic_phrase)

game = Game(magic_phrase)
errprint(len(game.stones))
if False:
    errprint(game.stepsBetweenLetters(" ", "A"))
    errprint(game.stepsBetweenLetters(" ", "Z"))
    errprint(game.stepsBetweenLetters("A", " "))
    errprint(game.stepsBetweenLetters("Z", " "))
    errprint(game.stepsBetweenLetters("A", "Z"))
    errprint(game.stepsBetweenLetters("Z", "A"))

idx = 0
while game.string != game.phrase:

    cur = game.stones[game.loc]
    tar = game.phrase[idx]
    game.getCommand(cur, tar)
    idx += 1
    errprint(game.command)
print(game.command)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print("+.>-.")
