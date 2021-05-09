import Proweb.ProcessJS as JS
import Proweb.Tools as Tools
import Proweb.Conf as C

import Proweb.Utils.Html.Html as html
import glob as glob
import re as re

HTMLS = {};


from html.entities import name2codepoint;
from html.parser import HTMLParser;
import Proweb.Utils.Html.Tag as Tag

import re;

class HTMLParserImpl(HTMLParser):

	def __init__(self):
		super().__init__();
		self.document = Tag.Document();
		self.current = None;



	def handle_starttag(self, tag, attrs):
		print("Start tag:", tag)
		for attr in attrs:
			print("     attr:", attr)
		

		if tag.startswith("pro-"):
			pass
		else:
			t = Tag.Tag(tag, attrs);
			self.addChild(t);
			self.current = t;


	def handle_endtag(self, tag):
		print("End tag  :", tag)

		self.current = self.current.parent;


	def handle_data(self, data):
		data = re.sub(r"\s+", "", data);
		if (data != ""):
			self.addChild(data);
			print("Data     :", data)


	def handle_comment(self, data):
		print("Comment  :", data)


	def handle_entityref(self, name):
		c = chr(name2codepoint[name])
		print("Named ent:", c)


	def handle_charref(self, name):
		if name.startswith('x'):
			c = chr(int(name[1:], 16))
		else:
			c = chr(int(name))
		print("Num ent  :", c)


	def handle_decl(self, data):
		print("Decl     :", data)

		t = Tag.DeclTag(data);
		self.addChild(t);


	def addChild(self, child):
		if type(self.current) == Tag.Tag:
			self.current.child(child)
		else:
			self.document.child(child);


	def toHtml(self):
		return self.document.toHtml();


parser = HTMLParserImpl()



def searchLibs(OUT):
	global HTMLS
	files = list(OUT.glob("**/*.html"));

	for file in files:
		name = file.name[:-5]
		HTMLS[name] = {}
		HTMLS[name]["link"] = file; 
		HTMLS[name]["process"] = False;


def addScript(path):
	script = "<script src='" + path + "'></script>\n";
	HTMLS["index"]["text"] = HTMLS["index"]["text"].replace("</body>", "</body>" + script);


def processJS(name, args = []):
	file = list(C.DIR.glob(f"**/{name}.js"))
	if file:
		snippets = Tools.readJson("proweb.json")["snippets"];
		print("JS: " + name);
		text = Tools.read(file[1]);

		for arg in args:
			print("arg:" + arg);
			text = arg + ";" + text;

		for k, v in snippets.items():
			k = "(?<=[\s\.])" + k + "\(";
			text = re.sub(k, v + "(", text);


		path = "EXT/JS/" + name + ".js"
		Tools.write(C.DIR / path , text);
		addScript("./JS/" + name + ".js");


def processHTML(name):
	global parser, HTMLS;
	parser.feed(HTMLS[name]["text"]);


def processChild(name):
	lista = re.findall(r"<(pro-[^\s]*)(.*)>(.*)</pro-.*>", HTMLS[name]["text"]);

	for item, args, content in lista:
		if not HTMLS[item]["process"]:
			process(item, args);

		HTMLS[name]["text"] = re.sub("<" + item + ".*>.*</" + item +">", HTMLS[item]["text"], HTMLS[name]["text"]);



def process(name, arg=[]):
	global HTMLS

	print("HTML: " + name);

	HTMLS[name]["text"] = Tools.read(HTMLS[name]["link"]);
	
	processJS(name, arg);
	processHTML(name);

	HTMLS[name]["process"] = True;



def call(*args):
	global HTMLS

	IN = C.DIR / "IN";
	OUT = C.DIR / "OUT";
	EXT = C.DIR / "EXT";

	Tools.rm(EXT);
	Tools.mkdir(EXT);
	Tools.mkdir(EXT / "JS");

	Tools.rm(OUT);
	Tools.cp(IN, OUT);

	searchLibs(OUT);
	process("index")
	processJS("tools");


	Tools.write(EXT / "index.html" , HTMLS["index"]["text"]);

	Tools.cp(OUT / "CSS", EXT / "CSS");

	Tools.rm(OUT)
	print("fin");