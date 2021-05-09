def startTag(tag, attr=""):
	a = f"<{tag}";

	if type(attr) == dict:
		attr = attr.items()

	for key, value in attr:
		a += f" {key}='{value}'";
	a += ">";

	return a;


def endTag(tag):
	return f"</{tag}>"


def createTag(tag, attr="", content=""):
	start = startTag(tag, attr);
	end = endTag(tag);

	return start + content + end;


def declTag(decl=""):
	a = f"<!{decl}>";

	return a;

