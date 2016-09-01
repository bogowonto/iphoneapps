import os

file_path = "/Users/yusri/Bogowonto/Workspace/Projects/github/iphoneapps/"

os.chdir(file_path)
os.mkdir("testfolder", 0o775)

print(os.path)

os.chmod("testfolder", 0o755)

os.rename("testfolder", "updated-testfolder")

print("test print)
