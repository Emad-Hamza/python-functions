import os

def rename_file():
    files_names_list = os.listdir(r"D:\Projects\python\prank")
    print(files_names_list)
    saved_path = os.getcwd()
    os.chdir(r"D:\Projects\python\prank")

    for file_name in files_names_list:
        print("old name is "+file_name)
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("new name is "+file_name)
    os.chdir(saved_path)

rename_file()
