class Climbing:
    def climbstairs(self, n: int)->int:
        '''
        Two ways to climb, by 1 step or 2 step, so this function give you all possible solutions
        to reach the top given by n.
        '''

        step_1 = 1
        step_2 = 2

        possible_ways = 0
        counter = True

            