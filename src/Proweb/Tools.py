from send2trash import send2trash
import shutil
import json
import os

def mkdir(path):
	if(exists(path)):
		return; 
	try:
		os.mkdir(path);
	except Exception as e:
		print("Error mkdir:" +str(e));


def mkfile(path, text=""):
	try:
		print(text);
		f = open(path, "w");
		f.write(text);
		f.close();
	except Exception as e:
		print("Error: " + e);
		print(dir(e));


def rmdir(path):
	try:
		for root, dirs, files in os.walk(path, topdown=False):
			for name in files:
				send2trash(os.path.join(root, name))
			for name in dirs:
				send2trash(os.path.join(root, name))
		os.rmdir(path);
	except Exception as e:
		print("Error rmdir" + str(e));


def rmfile(path):
	try:
		os.remove(path);
	except Exception as e:
		print("Error rmfile" + str(e));


def rm(path):
	if os.path.isdir(path):
		rmdir(path);
	elif os.path.isfile(path):
		rmfile(path);


def mv(src, dst):
	try:
		shutil.move(src, dst);
	except Exception as e:
		print("Error")


def cp(src, dst):
	try:
		shutil.copytree(src, dst);
	except Exception as e:
		print("Error: " + str(e));


def read(path):
	try:
		f = open(path, "r");
		text = f.read();
		f.close();
		return text;
	except Exception as e:
		print("Error read:" + str(e));


def readJson(path):
	try:
		f = open(path, "r");
		return json.loads(f.read());
	except Exception as e:
		print("Error readJson: " + str(e))


def readLines(path, cb):
	f = open(path, "r");
	while True:
		line = f.readline();
		cb(line);
		if not line:
			break;


def write(path, text):
	try:
		f = open(path, "w");
		f.write(text);
		f.close();
	except Exception as e:
		print("Error write:" + str(e));


def writeJson(path, text):
	try:
		text = json.dumps(text, indent = 4)
		f = open(path, "w");
		f.write(text);
		f.close();
	except Exception as e:
		print("Error readJson: " + str(e))


def exists(path):
	try:
		return os.path.exists(path);
	except Exception as e:
		print("Error exist: " + str(e));