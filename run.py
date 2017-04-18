import admin
import monitor
import os

def main():
	abs_path = os.path.abspath("monitor.py")
	command = "python " + str(abspath)
	admin.command(command)	

if __name__ == '__main__':
	main()