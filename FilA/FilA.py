import os
import shutil
from posixpath import splitext

def organize():
    files,path = scan()
    doc_path = os.path.join(path,'Docs')
    img_path = os.path.join(path,'Images')
    vid_path = os.path.join(path,'Videos')
    aud_path = os.path.join(path,'Audios')
    app_path = os.path.join(path,'Softwares')
    zip_path = os.path.join(path,'Zipped')
    
    check_doc = os.path.isdir(doc_path)
    check_img = os.path.isdir(img_path)
    check_vid = os.path.isdir(vid_path)
    check_aud = os.path.isdir(aud_path)
    check_app = os.path.isdir(app_path)
    check_zip = os.path.isdir(zip_path)

    if check_doc == False:
        os.mkdir(doc_path) 
    if check_img == False:
        os.mkdir(img_path)
    if check_vid == False:
        os.mkdir(vid_path)
    if check_aud == False:
        os.mkdir(aud_path)
    if check_app == False:
        os.mkdir(app_path)
    if check_zip == False:
        os.mkdir(zip_path)

    for type in files:
        x = splitext(type)[1].lower()
        if x != '':
            if x in doc_exts:
                shutil.move(os.path.join(path,type),doc_path)
            if x in img_exts:
                shutil.move(os.path.join(path,type),img_path)
            if x in aud_exts:
                shutil.move(os.path.join(path,type),aud_path)
            if x in vid_exts:
                shutil.move(os.path.join(path,type),vid_path)
            if x in app_exts:
                shutil.move(os.path.join(path,type),app_path)
            if x in zip_exts:
                shutil.move(os.path.join(path,type),zip_path)

    print('Opertion Completed')



def scan():
    files_list = []
    path = input('Enter the path : ')
    print('Scanning...')
    files_list = os.listdir(path)
    print('Scanning Done!')
    return files_list,path

doc_exts = ['.pdf','.docx','.doc','.pptx','.ppt','.xlsx','.xls']
img_exts = ['.jpg','.jpeg','.png','.jfif','.gif','.webp']
vid_exts = ['.mp4','.mpeg4','.3gp','.wmv','.mkv','.webm','.mov']
aud_exts = ['.mp3','.wav','.aac','.flac']
app_exts = ['.exe','.msi','.apk','.jar']
zip_exts = ['.zip','.rar']

organize()