"""
Erlend Sanden

erlend.h.sanden@gmail.com


Imports libraries
"""


import pygame, random, time, math

"""
Creates class as requested from the assignment
"""


class dice:

    """
    Init function. Size is the width and length of the window. Size is the paramter of the function

    """
    def __init__(self, size):

        """
        Creates a dictionary which are the values that can be set by the user.
        """
        color_dict = {"black" : [0, 0, 0], "white" : [255, 255, 255], "red" : [255, 0, 0], "green" : [0, 255, 0], "blue": [0,0,255], "yellow": [255, 255, 0], "pink": [255, 192, 203],
        "brown": [165, 42, 42], "purple": [128, 0, 128], "orange": [255, 165, 0], "grey": [128, 128, 128]}
        """
        The user types in the x and y-positions. self.size//2 is the midpoint of the window. Top and left value of the window is equal to 0. Right and bottom value is equal to self.size 
        """
        self.size = size
        self.x = int(input("Write x-position "))
        self.y = int(input("Write y-position "))
        self.ace_size = int(self.size//20)
        self.x_midpoint = int(self.size//2)+self.x
        self.y_midpoint = int(self.size // 2) + self.y
        self.left = 10+self.x
        self.top = 10+self.y
        self.right = int(self.size - 1)+self.x
        self.bottom = int(self.size - 1)+self.y

        print("These are the colour options (black and white default): ")
        for i in color_dict:
            print(i)


        """
        Sets die and spotcolor to default black and white
        """


        self.dicecolor = color_dict.get("white")
        self.spotcolor = color_dict.get("black")


        self.diecolorinput = input("Enter colour of die ").lower()
        self.spotcolorinput = input("Enter color of eyes ").lower()

        if self.diecolorinput == "":
            pass
        else:
            self.dicecolor = color_dict.get(self.diecolorinput)

        if self.spotcolorinput == "":
            pass
        else:
            self.spotcolor = color_dict.get(self.spotcolorinput)


        self.d = pygame.display.set_mode((int(size*2), int(size*2)))
        self.display = pygame.display.set_caption("Dice simulator")


        """
        def rolling draws the eyes of the die. It rolls between 3 to 20 times. 
        
        """


    def rolling(self):

        self.pos_correct = int(self.size/2)
        rolls = random.randint(3,20)

        for i in range(rolls):
            self.d.fill(self.dicecolor)
            self.n = random.randint(1, 6)
            if self.n % 2 == 1:
                pygame.draw.circle(self.d, self.spotcolor, (self.pos_correct+self.x_midpoint, self.pos_correct+self.y_midpoint), self.ace_size)
            if self.n == 2 or self.n == 3 or self.n == 4 or self.n == 5 or self.n == 6:
                pygame.draw.circle(self.d, self.spotcolor, (self.pos_correct+self.left,self.pos_correct+self.bottom), self.ace_size)
                pygame.draw.circle(self.d, self.spotcolor, (self.pos_correct+self.right, self.pos_correct+self.top), self.ace_size)
            if self.n == 4 or self.n == 5 or self.n == 6:
                pygame.draw.circle(self.d, self.spotcolor, (self.pos_correct+self.left, self.pos_correct+self.top), self.ace_size)
                pygame.draw.circle(self.d, self.spotcolor, (self.pos_correct+self.right, self.pos_correct+self.bottom), self.ace_size)
            if self.n == 6:
                pygame.draw.circle(self.d, self.spotcolor, (self.pos_correct+self.x_midpoint, self.pos_correct+self.top), self.ace_size)
                pygame.draw.circle(self.d, self.spotcolor, (self.pos_correct+self.x_midpoint, self.pos_correct+self.bottom), self.ace_size)

            time.sleep(0.5)
            pygame.display.flip()
            if(i==rolls-1):
                pygame.display.flip()
                print("Lucky number is: ", self.n)
                input("Press enter to exit program")



size = int(input("Enter a size value "))
roll = dice(size)
roll.rolling()



