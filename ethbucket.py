#A driver program to call push, pull, merge
#Push: Get the user input for file path append the file name with timestamp
#      upload onto storj.  Update the current view and user view in smart contract
#Pull: Get the cur view from the ledger.  Compare with the file IDs and file names that are currently
#      present in the workspace.  If any of them are open for edit then need to call merge before 
#      replacing them.
#merge: Find the diff between the two files and apply the patch on the file
#init: This file needs to store the list of files that are currently open for edit.  Both file names and IDs
#edit: mark a file as open for edit in config file
#log: Get a list of all fileIDs per user in the order of commits from the ledger
#checkout: Switch to a specific version of the file.  Needs fileId and bucketId

from shutil import copyfile
import ConfigParser
import datetime
import os
import sys

class ethBucket:

	filePath = None
	bucketName = None
	bucketID = None
	config = None
	curFileIDtoName = {}
	
	#Initialize ConfigParser
	def initParser(self):
		ethBucket.config = ConfigParser.RawConfigParser()
		ethBucket.config.read('ethBucket.cfg')
		
	#Input: bucketID, fileID, filePath
	def checkout(self):
		bucketID = sys.argv[2]
		fileID = sys.argv[3]
		ethBucket.filePath = sys.argv[4]
		utils().download(bucketID, fileID, ethBucket.filePath)
		

	#Input: filePath
	def edit(self): 
		self.initParser()
		ethBucket.filePath = sys.argv[2]
		utils().all_perms(ethBucket.filePath)
		path, file = os.path.split(ethBucket.filePath)	
		ethBucket.config.set("Files open for edit", file, "true"); 		
		with open('ethBucket.cfg', 'wb') as configfile:
    			ethBucket.config.write(configfile)


	#Input: bucketName, curPath
	def pull(self):
		#Get the list of files that are present in the active workspace
		CurFileIDs = []
		ethBucket.bucketName = sys.argv[2]
		ethBucket.filePath = sys.argv[3]
		#Get the bucket ID from init file
		self.initParser()
		ethBucket.bucketID = ethBucket.config.get('Bucket', ethBucket.bucketName); 		
		
		#If the file is not open for edit, then just download and replace
		
		for f in CurFileIDs:
			#convert from fileID to fileName, check if this file is open for edit
			newFileName = ethBucket.config.get('ID to Name',f);
			curFile = ethBucket.config.get("Files open for edit", newFileName); 		
			if (curFile != true):
				os.remove(curPath + "/" + newFileName)
				utils().download(ethBucket.bucketID, f, ethBucket.filePath + "/" + newFileName)
			else:
				utils().download(ethBucket.bucketID, f, ethBucket.filePath + "/" + tempEthBucketFile)
				utils().merge(ethBucket.filePath + "/" + newFileName, ethBucket.filePath + "/" + tempEthBucketFile)
				os.remove(ethBucket.filePath + "/" + tempEthBucketFile)

	
	#Input: bucketName, filePath
	def push(self):
		self.initParser()
		#Get the file path from the user
		ethBucket.bucketName = sys.argv[2]
		ethBucket.filePath = sys.argv[3]
		#Get the bucket ID from init file
		ethBucket.bucketID = ethBucket.config.get('Bucket', ethBucket.bucketName); 		
		#Append timeStamp to the fileName
		path, file = os.path.split(ethBucket.filePath)	
		dst = path + "/" + file + "." + datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
		copyfile(ethBucket.filePath,dst)
		#Upload file to STORJ and delete temporary file
		fileID = utils().upload(ethBucket.bucketID, dst)
		os.remove(dst)
		#TODO:Update curView(modify) and userView(appendToList) in the ledger with fileID
		ethBucket.config.set('ID to Name', fileID, file)
		with open('ethBucket.cfg', 'wb') as configfile:
    			ethBucket.config.write(configfile)
			
		

	#Input : bucketName.  This can be changed to get the current working directory later.
	def init(self):
		self.initParser()
		ethBucket.config.add_section('Bucket')
		ethBucket.bucketName = sys.argv[2]
		ethBucket.bucketID = utils().addBucket(ethBucket.bucketName)	
		ethBucket.config.set('Bucket', ethBucket.bucketName, ethBucket.bucketID)
		ethBucket.config.add_section(ethBucket.bucketName)
		ethBucket.config.add_section("ID to Name")
		ethBucket.config.add_section("Files open for edit")
		
		with open('ethBucket.cfg', 'wb') as configfile:
    			ethBucket.config.write(configfile)


	def invoke_func(self, funcName):
		if (funcName == 'push'):
			ethBucket().push()
		elif (funcName == 'init'):
			ethBucket().init()
		elif (funcName == 'pull'):
			ethBucket().pull()
		elif (funcName == 'edit'):
			ethBucket().edit()
		elif (funcName == 'log'):
			ethBucket().log()
		elif (funcName == 'checkout'):
			ethBucket().checkout()
def main():
	if (len(sys.argv) > 1):
		eth = ethBucket() 
		eth.invoke_func(sys.argv[1])
	else:
		print "Options"
		print "	push bucketName filePath"
		print "	init bucketName"
		print "	pull bucketName curPath"
		print "	edit filePath"
		print "	log"
		print "	checkout bucketID fileID filePath/fileName"

if __name__ == "__main__": main()

			
	

	
		
