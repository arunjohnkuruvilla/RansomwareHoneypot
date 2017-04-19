import sys

def module_check():
	status = True
	try:
		import fpdf
	except ImportError:
		print "FPDF module not installed."
		status = False
	return status

def main():
	if len(sys.argv) < 2:
		print "No command given"
		sys.exit(0);

	if sys.argv[1] == "configure":
		if module_check():
			print "All required modules present."
		else:
			print "Required modules not present."

	elif sys.argv[1] == "generate":
		print "'generate' command selected"
	else:
		print "Invalid command given"
		print "usage: setup.py [-h] command"
		print "setup.py: error: too few arguments"

if __name__ == '__main__':
	main()
