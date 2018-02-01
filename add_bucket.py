import subprocess
import sys


def addBucket(bucketName):
	p2 = subprocess.Popen(["./storj", "add-bucket", bucketName], stdout=subprocess.PIPE)
	output = p2.communicate()[0]
	print output
	bucketInfo = output.split(":")
	bucketID1 = bucketInfo[1]
	bucketID2 = bucketID1.split(" ")
	bucketID = bucketID2[1]
	return bucketID



