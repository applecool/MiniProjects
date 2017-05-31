import os

def crack_code():
    #get all file names in the directory.
    file_list = os.listdir("/Users/ShellZero/MiniProjects/Cipher/prank")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir("/Users/ShellZero/MiniProjects/Cipher/prank")
    for file_name in file_list:
        print("old name", file_name)
        table = file_name.maketrans(dict.fromkeys("0123456789"))
        print("new name", file_name.translate(table))
        os.rename(file_name, file_name.translate(table))

crack_code()
