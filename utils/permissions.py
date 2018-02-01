import subprocess
import sys

def all_perms(path):
	p1 = subprocess.Popen(["chmod", "777", path], stdout=subprocess.PIPE)
	output = p1.communicate()[0]
	print output
def read_perms(path):
	p1 = subprocess.Popen(["chmod", "444", path], stdout=subprocess.PIPE)
	output = p1.communicate()[0]
	print output

