import subprocess


def upload(bucketID, path):
	p1 = subprocess.Popen(["./storj", "upload-file", bucketID, path], stdout=subprocess.PIPE)
	output = p1.communicate()[0]
	print output
	fileInfo = output.split(":")
	fileID1 = fileInfo[1]
	fileID2 = fileID1.split("\n")
	fileID3 = fileID2[0]
	fileID4 = fileID3.split(" ");
	fileID = fileID4[1]
	return fileID

