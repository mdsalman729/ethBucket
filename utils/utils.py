import subprocess
import sys
import os

class utils:
	def addBucket(self,bucketName):
		p2 = subprocess.Popen(["Storj", "add-bucket", bucketName], stdout=subprocess.PIPE)
		output = p2.communicate()[0]
		print output
		bucketInfo = output.split(":")
		bucketID1 = bucketInfo[1]
		bucketID2 = bucketID1.split(" ")
		bucketID = bucketID2[1]
		return bucketID

	def download(self,bucketID, fileID, path):
		p1 = subprocess.Popen(["Storj", "download-file", bucketID, fileID, path], stdout=subprocess.PIPE)
		output = p1.communicate()[0]
		print output
		self.read_perms(path)

	def merge(self,file1, file2, file3):
		path, fileName = os.path.split(file3)	
		f = open(file3, "w")
		p1 = subprocess.Popen(["diff", "-u", file1, file2], stdout=f)
		output = p1.communicate()[0]
		p2 = subprocess.Popen(["patch", file1, file3])
		output = p2.communicate()[0]
		

	def all_perms(self,path):
		p1 = subprocess.Popen(["chmod", "777", path], stdout=subprocess.PIPE)
	def read_perms(self, path):
		p1 = subprocess.Popen(["chmod", "444", path], stdout=subprocess.PIPE)

	def upload(self,bucketID, path):
		p1 = subprocess.Popen(["Storj", "upload-file", bucketID, path], stdout=subprocess.PIPE)
		output = p1.communicate()[0]
		print output
		fileInfo = output.split(":")
		fileID1 = fileInfo[1]
		fileID2 = fileID1.split("\n")
		fileID3 = fileID2[0]
		fileID4 = fileID3.split(" ");
		fileID = fileID4[1]
		return fileID

