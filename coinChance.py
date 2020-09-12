import random

class Flip:
    def __init__(self, amount):
        self.amount = amount
        self.heads = []
        self.tails = []

    def spin(self):
        i = 0
        while i < self.amount:
            flip = random.choice([0, 1])
            if flip == 0: self.heads.append(flip)
            if flip == 1: self.tails.append(flip)

            i += 1

        return self

    def percent(self):
        h_chance = len(self.heads)/self.amount * 100
        t_chance = len(self.tails)/self.amount * 100

        return f"Heads: {h_chance}%, Tails: {t_chance}%"

coinFlip = Flip(1000).spin().percent()

print(coinFlip)