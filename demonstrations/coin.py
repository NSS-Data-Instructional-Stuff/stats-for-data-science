from scipy.stats import binom
import random

class CoinFlipper():
    def __init__(self):
        fair = random.random() < 0.5
        if fair:
            self._p = 0.5
        else:
            self._p = round(random.normalvariate(0.5, 0.05), 2)
            while abs(self._p - 0.5) <= 0.03:
                self._p = round(random.normalvariate(0.5, 0.05), 2)
                
    def flip(self, number_flips):
        if number_flips > 10:
            print("Sorry, I can't flip more than 10 times at once.")
        else:
            print (f"The coin landed on heads {binom.rvs(p = self._p, n = number_flips)} times.")
        
    def is_fair(self):
        if self._p == 0.5:
            print('This coin is fair.')
        else:
            print(f'This coin is not fair. The true probability of heads is {self._p}.')
