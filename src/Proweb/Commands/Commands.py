import Proweb.Output as Output 
import Proweb.Tools as Tools


import glob as glob;
import re as re;

class Commands():

	def __init__(self):
		pass

	def call(self, *args):
		fn = getattr(self, f"cmd_{args[0]}", None)
		if fn is not None:
			r = not fn(*args[1:])			 
		else:
			print(f"No function call: {args[0]}");
			r = True
		return r

	def cmd_help(self, *args):
		"""Help command"""
		fn = filter(lambda fn: "cmd_" in fn, dir(self))
		for name in fn:
			f = getattr(self, name, None);
			Output.printCol(3, name, f.__doc__);
