from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)
 
upload_file_list = ['1.png']
 
exist_file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(targetDirID)}).GetList()
 
for upload_file in upload_file_list:
	if(not os.path.exists(upload_file)):
		continue
		
	fileName = os.path.basename(upload_file)
	for file1 in exist_file_list:
		if file1['title'] == fileName:
			file1.Delete()
		
	gfile = drive.CreateFile({'parents': [{'id': targetDirID}], 'title': fileName})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file. 



"""from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1AyRu9ixxuG-Bt5KB6cm0HmEkUAf7ZX1N')}).GetList()
print(len(file_list))
for file in file_list:
	print('title: %s, id: %s' % (file['title'], file['id'])) """