import os
import random

def rename_file():
    files_names_list = os.listdir(r"D:\Projects\python\alphabet")
    print(files_names_list)
    saved_path = os.getcwd()
    os.chdir(r"D:\Projects\python\alphabet")

    for file_name in files_names_list:
        print("old name is "+file_name)
        file_chars_list = list(os.path.splitext(file_name)[0])+list("0123456789")#adding numbers to the file name string
        random.shuffle(file_chars_list)#shuffle the file name string after adding numbers
        new_name = ''.join(file_chars_list)+".jpg"
        print("new_name is "+new_name)        
        os.rename(file_name, new_name)#first renaming producre
        newer_name = new_name.translate(None, "0123456789")#cleaning the file name string from numbers
        os.rename(new_name, newer_name)#second renaming producre
        print("newer_name is "+newer_name)
        
    os.chdir(saved_path)

rename_file()
