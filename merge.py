import subprocess
import sys

def merge(file1, file2):
	path = sys.argv[3]
	f = open(path, "w")
	p1 = subprocess.Popen(["diff", "-u", file1, file2], stdout=f)
	p2 = subprocess.Popen(["patch", file1, path])

