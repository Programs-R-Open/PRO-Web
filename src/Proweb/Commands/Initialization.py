import Proweb.Commands.Commands as Commands

import Proweb.Utils.Html.Html as html
import Proweb.Utils.Html.Tag as Tag

import Proweb.Tools as Tools
import Proweb.Conf as C

import os


class Initialization(Commands.Commands):
	def __init__(self):
		super().__init__();

	def call(self, *args):
		if not Tools.exists(C.DIR / "proweb.json"):
			props = {};
			index = "";

			props["name"] = input("Name: ");
			props["elements"] = "./IN/ELEMENTS/";
			snips = input("Snippets [E]mpty [D]efault:");
			if snips == "E":
				props["snippets"] = {};
				index = "";
			elif snips == "D":
				props["snippets"] = {
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

			Tools.writeJson(C.PROJ / "proweb.json", props);
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

