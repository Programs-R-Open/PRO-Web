import ctypes
import os

if os.name == "nt":

	STD_INPUT_HANDLE = -10
	STD_OUTPUT_HANDLE= -11
	STD_ERROR_HANDLE = -12

	FOREGROUND_BLUE = 0x01 # text color contains blue.
	FOREGROUND_GREEN= 0x02 # text color contains green.
	FOREGROUND_RED  = 0x04 # text color contains red.
	FOREGROUND_INTENSITY = 0x08 # text color is intensified.

	FOREGROUND_WHITE = FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED;


	BACKGROUND_BLUE = 0x10 # background color contains blue.
	BACKGROUND_GREEN= 0x20 # background color contains green.
	BACKGROUND_RED  = 0x40 # background color contains red.
	BACKGROUND_INTENSITY = 0x80 # background color is intensified.

	std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

elif os.name == "posix":

	FOREGROUND_RED = "\x1B[31m";
	FOREGROUND_GREEN = "\x1B[32m";
	FOREGROUND_YELLOW = "\x1B[33m";
	FOREGROUND_BLUE = "\x1B[34m";
	FOREGROUND_MAGENTA = "\x1B[35m";
	FOREGROUND_CYAN = "\x1B[36m";
	FOREGROUND_WHITE = "\x1B[0m";



	BACKGROUND_BLUE = 0x10 # background color contains blue.
	BACKGROUND_GREEN= 0x20 # background color contains green.
	BACKGROUND_RED  = 0x40 # background color contains red.
	BACKGROUND_INTENSITY = 0x80 # background color is intensified.



def set_color(color):
	if os.name == "nt":
		bool = ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color)
	elif os.name == "posix":
		print(color);
	return bool;

def ColorPrint(color, *text):
	set_color(color);
	print(*text);
	set_color(FOREGROUND_WHITE);

def printCol(sep, o, t):
	num = sep - len(o)//8;
	print(o, end="");
	for x in range(num):
		print("\t", end="")
	print(t);



