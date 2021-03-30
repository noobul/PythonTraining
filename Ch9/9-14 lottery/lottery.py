from random import choice

"""Lotery class"""
class Lottery:
    def __init__(self):
        self.pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

    def play(self):
        """ 
        Play method used to create a list with the results of a lottery run
        """
        results = []
        for x in range(4):
            result = choice(self.pool)
            results.append(result)
        return results