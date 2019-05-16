import os,shutil
dict_extension={ 
   'video_exyension':('.mp4'),
   'document_extension':('.jpg'),
   'audio_extension':('.mp3')
}
folderpath=input('copy file path : ')

def file_finder(folder_path,file_extensions):
    files=[]
    for  file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):

             files.append(file)
    return files
#print(file_finder(folderpath,audio_extension))
for extension_type,extension_tuple in dict_extension.items():
    folder_name=extension_type.split('_')[0]+ 'files'
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extension_tuple):
        item_path=os.path.join(folderpath,item)
        item_new_path=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)


    #print('calling file finder ')
    #print(file_finder(folderpath,extension_tuple))

