import Proweb.Conf as C

import threading
import pathlib
import os

class Input(threading.Thread):
	def __init__(self,exit, input_cbk = None, name='keyboard-input-thread'):
		self.input_cbk = input_cbk
		self.exit = exit;
		self.loop = True;
		super(Input, self).__init__(name=name)
		self.start()

	def run(self):
		while self.loop:
			folder = os.path.basename(C.DIR);
			project = str(C.P_NAME);
			a = ""
			a += f"{folder}{project} >";

			try:
				a = input(a).split(" ");
			except EOFError as e:
				break
			self.loop = self.input_cbk(*a);
		self.exit.set()