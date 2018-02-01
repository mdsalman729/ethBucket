import subprocess
import sys

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

	def merge(self,file1, file2):
		f = open(file2, "w")
		path, fileName = os.path.split(file2)	
		p1 = subprocess.Popen(["diff", "-u", file1, file2], stdout=f)
		p2 = subprocess.Popen(["patch", file1, fileName])

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

