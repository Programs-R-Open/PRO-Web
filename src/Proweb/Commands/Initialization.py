import Proweb.Commands.Commands as Commands

import Proweb.Utils.Html.Html as html
import Proweb.Utils.Html.Tag as Tag

import Proweb.Tools as Tools
import Proweb.Conf as C

import os





class Asking:
	def __init__(self, question):
		self.resolved = False;
		self.question = question
		self.dict = {};

	def on(self, answer, func):
		self.dict[answer] = func;
		return self;

	def default(self, func):
		self.defaultFunc = func;
		return self;

	def end(self):
		self.answer = input(self.question);
		if (self.answer in self.dict):
			self.dict[self.answer]();
		elif hasattr(self, "defaultFunc"):
			self.defaultFunc();
		else:
			print("Sorry but that is not a valid value")
			self.end();


class Initialization(Commands.Commands):
	def __init__(self):
		super().__init__();
		self.props = {};

	def call1(self, *args):
		if Tools.exists(C.DIR / "proweb.json"):
			return print("there is another project in this folder");

		#Asking("Project type [F]rontend [B]ackend [L]ib [C]ustom")
		#.on("E", emptySnippets)
		#.on("D", defaultSnippets);

		question = Asking("Snippets [E]mpty [D]efault:")
		question.on("E", self.emptySnippets)
		question.on("D", self.defaultSnippets)
		question.end();

		#Asking("Project type [F]rontend [B]ackend [L]ib [C]ustom")
		#.on("E", emptySnippets)
		#.on("D", defaultSnippets);


	def emptySnippets(self):
		pass;

	def defaultSnippets(self):
		self.props["snippets"] = {
			"GET":"document.querySelector",
			"GETALL":"document.querySelectorAll",
			"NEW":"document.createElement",
			"CHILD":"appendChild",
			"EVENT":"addEventListener"
		}

	def defaultFront(self):
		document = Tag.Document();
		doctype = Tag.DeclTag("DOCTYPE html");
		html = Tag.Tag("html")
		head = Tag.Tag("head");
		title = Tag.Tag("title");
		body = Tag.Tag("body");


		title.child("##NAME##");
		head.child(title);
		html.child(head);
		html.child(body);
		document.child(doctype)
		document.child(html);
		index = document.toHtml();

	def call(self, *args):
		if not Tools.exists(C.DIR / "proweb.json"):
			index = "";

			self.props["name"] = input("Name: ");
			self.props["elements"] = "./IN/ELEMENTS/";
			snips = input("Snippets [E]mpty [D]efault:");
			if snips == "E":
				self.props["snippets"] = {};
				index = "";
			elif snips == "D":
				self.props["snippets"] = {
					"GET":"document.querySelector",
					"GETALL":"document.querySelectorAll",
					"NEW":"document.createElement",
					"CHILD":"appendChild",
					"EVENT":"addEventListener"
				}

				document = Tag.Document();
				doctype = Tag.DeclTag("DOCTYPE html");
				html = Tag.Tag("html")
				head = Tag.Tag("head");
				title = Tag.Tag("title");
				body = Tag.Tag("body");


				title.child("##NAME##");
				head.child(title);
				html.child(head);
				html.child(body);
				document.child(doctype)
				document.child(html);
				index = document.toHtml();

			else:
				print("No project was created");
				return

			Tools.writeJson(C.PROJ / "proweb.json", self.props);
			Tools.mkdir(C.FRONT);
			Tools.mkdir(C.FRONT / "IN");
			Tools.mkdir(C.FRONT / "IN" / "CSS");
			Tools.mkdir(C.FRONT / "IN" / "JS");
			Tools.mkdir(C.FRONT / "IN" / "ELEMENTS");
			Tools.mkfile(C.FRONT / "IN" / "index.html", index);


			Tools.mkdir(C.BACK);
			os.chdir(C.BACK)
			os.system("npm init");
			os.system("npm install express");
			os.chdir("..")
			server = """const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('./Frontend/IN/'))

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`)
})
""";

			Tools.mkfile(C.BACK / "index.js", server);


			#self.cmd_process();
			
		else:
			print("there is another project in this folder");

