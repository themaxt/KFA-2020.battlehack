import random
import Robot
import Pawn
import Overlord

# This is an example bot written by the developers!
# Use this to help write your own code, or run it against your bot to see how well you can do!

bot = None

DEBUG = 1
def dlog(str):
	if DEBUG > 0:
		log(str)


def check_space_wrapper(r, c, board_size):
	# check space, except doesn't hit you with game errors
	if r < 0 or c < 0 or c >= board_size or r >= board_size:
		return False
	try:
		return check_space(r, c)
	except:
		return None

def turn():
	global bot
	# initialize
	if bot is None:
		team = get_team()
		robottype = get_type()
		white = True if team == Team.WHITE else False
		if robottype == RobotType.PAWN:
			bot = Pawn()
		else:
			bot = Overlord()
		bot.init(white)
	"""
	MUST be defined for robot to run
	This function will be called at the beginning of every turn and should contain the bulk of your robot commands
	"""
	bot.turn()

	bytecode = get_bytecode()
	dlog('Done! Bytecode left: ' + str(bytecode))
