

class player:
    def play(self):
        print("the player is playing cricket.")
class Batsman(player):
    def play(self):
        print("the Batsman is batting.")
class Bowler(player):
    def play(self):
        print("the Bowler is bowling.")

    
batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()