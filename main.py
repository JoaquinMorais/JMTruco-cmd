from JMTrucoCmd import Game
from JMTrucoCmd.functions.bots import get_bots
game = Game(objective=5)

game.start(bot=get_bots(name='jesus'))