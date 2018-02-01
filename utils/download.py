import subprocess
import sys
from permissions import read_perms

def download(bucketID, fileID, path):
	p1 = subprocess.Popen(["Storj", "download-file", bucketID, fileID, path], stdout=subprocess.PIPE)
	output = p1.communicate()[0]
	print output
	read_perms(path)

