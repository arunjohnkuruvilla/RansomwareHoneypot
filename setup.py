import sys
import src.generate as generate

def module_check():
	status = True
	try:
		import fpdf
	except ImportError:
		print "FPDF module not installed."
		status = False
	return status

def help_text():
	return
def main():
	if len(sys.argv) < 2:
		print "No command given"
		sys.exit(0);

	if sys.argv[1] == "configure":
		if module_check():
			print "All required modules present."
		else:
			print "Required modules not present."

	# Generate folder structure
	elif sys.argv[1] == "generate":
		file_system = generate.FS()
		file_system.create_dir_tree()
		file_system.generate_pdf()
		file_system.generate_xls()
		file_system.generate_txt()
	else:
		print "Invalid command given"
		print "usage: setup.py [-h] command"
		print "setup.py: error: too few arguments"

if __name__ == '__main__':
	main()
