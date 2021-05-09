import Proweb.Commands.Commands as Commands
import Proweb.Tools as Tools

import glob as glob;
import re as re;

class Snippets(Commands.Commands):

	def __init__(self):
		super().__init__();

	def cmd_list(self, DIR, *args):
		snippets = Tools.readJson("proweb.json")["snippets"];
		print("");
		for k, v in snippets.items():
			print(k + "\t\t" + v );
		print("");


	def cmd_add(self, DIR, *args):
		json = Tools.readJson("proweb.json");
		json["snippets"][args[0]] = args[1];
		Tools.writeJson("proweb.json", json);


	def cmd_rm(self, DIR, *args):
		json = Tools.readJson("proweb.json");
		json["snippets"].pop(args[0]);
		Tools.writeJson("proweb.json", json);