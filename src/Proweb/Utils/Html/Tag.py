import Proweb.Utils.Html.Utils as html


class Document:
	def __init__(self):
		self.childs = [];
	
	def __str__(self):
		s = ""

		for child in self.childs:
			s +="\n" + str(child);

		return s;

	def child(self, tag):
		if type(tag) == Tag: 
			tag.parent = self;
		self.childs.append(tag);

	def toHtml(self, tab=0):
		s = "";

		for child in self.childs:
			if type(child) == Tag or type(child) == DeclTag: 
				s += child.toHtml();
			else:
				s += child + "\n";


		return s;




class Tag:
	def __init__(self, tag, attr={}):
		self.tag =  tag;
		self.attr = attr;
		self.childs = [];
		self.parent = None;

	def __str__(self):
		s = ""

		for child in self.childs:
			s +="\n" + str(child);

		return self.tag + s;

	def child(self, tag):
		if type(tag) == Tag: 
			tag.parent = self;
		self.childs.append(tag);

	def toHtml(self, tab=0):
		s = ("\t" * tab) + html.startTag(self.tag, self.attr)+"\n";

		for child in self.childs:
			if type(child) == Tag or type(child ) == DeclTag: 
				s += child.toHtml(tab + 1);
			else:
				s += ("\t" * (tab + 1)) + child + "\n";

		s += ("\t" * tab) + html.endTag(self.tag) + "\n";


		return s;


class DeclTag:
	def __init__(self, decl):
		self.decl = decl;
		self.parent = None;

	def __str__(self):
		return self.tag;


	def toHtml(self, tab=0):
		s = ("\t" * tab) + html.declTag(self.decl) + "\n";

		return s;



