from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        # with open("Data.text") as data:
        #     read(data )
        
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

    def update_scoreboard(self):
        self.clear()
        self.write( arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
 
    def reset(self):
        if self.score > self.high_score:
            self.high_score  = self.score
            self.score = 0
            self.update_scoreboard()