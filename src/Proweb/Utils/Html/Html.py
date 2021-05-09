from html.entities import name2codepoint;
from html.parser import HTMLParser;
import Proweb.Utils.Html.Tag as Tag

import re;

class HTMLParserImpl(HTMLParser):

	def __init__(self):
		super().__init__();
		self.textIn="";
		self.document = Tag.Document();
		self.current = None;


	def setText(self, text):
		self.textIn = text;



	def handle_starttag(self, tag, attrs):
		print("Start tag:", tag)
		for attr in attrs:
			print("     attr:", attr)
		
		
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
