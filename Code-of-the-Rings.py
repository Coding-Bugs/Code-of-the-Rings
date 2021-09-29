from sys import stderr

def errprint(message):
    print(message, file=stderr, flush=True)

class Game:

    def __init__(self, phrase: str):
        self.phrase = phrase
        self.words = [i for i in phrase.split(" ")]
        self.word_idx = 0

        self.loc = 0
        self.len_stone = 30
        self.stones = [" " for i in range(self.len_stone)]

        self.command = ""
        self.string = ""
        
        self.letDict = {" " : 0, "A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10, "K" : 11, "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26}
        self.numDict = {0 : " ", 1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G", 8 : "H", 9 : "I", 10 : "J", 11 : "K", 12 : "L", 13 : "M", 14 : "N", 15 : "O", 16 : "P", 17 : "Q", 18 : "R", 19 : "S", 20 : "T", 21 : "U", 22 : "V", 23 : "W", 24 : "X", 25 : "Y", 26 : "Z"}  
    
    def parseInput():
        for word in words:
            div = []
            sub = word[0]
            for ch in word:
                if ch == sub:
                    pass


    def moveN(self, n: int):
        self.loc = (self.loc + n) % self.len_stone
        if n > 0:
            # errprint("Positive Move")
            self.command += ">" * n
        else:
            # errprint("Negative Move")
            self.command += "<" * abs(n)


    def findNextSpace():
        pass


    def loop(self, steps: int, tar: int):
        if steps < abs(steps - tar):
            return steps
        else:
            return steps - tar


    def stepsToLetter(self, cur: str, target: str):
        n1 = self.letDict[cur]
        n2 = self.letDict[target]
        mod = len(self.letDict)
        steps = ( n2 - n1 ) % mod   

        return self.loop(steps, mod)


    def changeStoneN(self, n: int):
        newLetter = self.numDict[(self.letDict[self.stones[self.loc]] + n) % 27]
        self.stones[self.loc] = newLetter
        # errprint("stone #{self.loc} new letter: {newLetter}".format(**locals()))
        if n > 0:
            # errprint("Positive Stone Inc")
            self.command += "+" * n
        else:
            # errprint("Negative Stone Inc")
            self.command += "-" * abs(n)

    def addLetter(self):
        self.command += "."
        pass


def main():
    magic_phrase = input()
    game = Game(magic_phrase)
    errprint(magic_phrase)

    for letter in magic_phrase:
        steps = game.stepsToLetter(game.stones[game.loc], letter)
        nxt = game.stepsToLetter(game.stones[(game.loc + 1) % game.len_stone], letter)
        temp = abs(nxt) + 1
        
        if letter == game.stones[game.loc]:
            # errprint("Cheaper to Stay")
            game.addLetter()
        elif abs(nxt) + 1 < abs(steps):
            # errprint("Cheaper to Move")
            game.moveN(1)
            game.changeStoneN(nxt)
            game.addLetter()
        else:
            # errprint("Cheaper to Change")
            game.changeStoneN(steps)
            game.addLetter()

    print(game.command)


if __name__ == "__main__":
    main()