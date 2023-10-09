from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setpos(-280, 250)
        self.write(f'Level {self.level}', False, align='left', font=FONT)

    def level_inc(self):
        self.level += 1
        self.clear()
        self.write(f'Level {self.level}', False, align='left', font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.write(f'GAME OVER', False, align='center', font=FONT)