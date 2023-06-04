#------12.1------
#
# root/
# |
# -----app/
# |    |
# |    -----program.py
# |    |
# |    -----data.txt
# |
# -----photos/
#      |
#      -----cats/
#      |    |
#      |    -----lion.jpg
#      |    |
#      |    -----siamese.png
#      |
#      -----dogs/
#           |
#           -----dachshound.jpg
#           |
#           -----jack_russel.git

#------12.2------
#
import pathlib


#macOS
path = pathlib.Path("/Users/David/Documents/hello.txt")
#windows
#error:
#path = pathlib.Path("C:\Users\David\Documents\hello.txt")
#SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
#correct:
path = pathlib.Path("C:/Users/David/Documents/hello.txt")
path = pathlib.Path(r"C:\Users\David\Documents\hello.txt")
path # WindowsPath('C:/Users/David/Documents/hello.txt')

home = pathlib.Path.home()
home # WindowsPath('C:/Users/pauli')
pathlib.Path.cwd() # WindowsPath('C:/Users/pauli/OneDrive/Dokumenty/Paulina/realpython/Python_Basics/chapters/chapt_12_file_input_and_output')

home / "Desktop" / "hello.txt" # WindowsPath('C:/Users/pauli/Desktop/hello.txt')


path = pathlib.Path("Photos/image/jpg")
path  # WindowsPath('Photos/image/jpg')
path.is_absolute()  # False
home = pathlib.Path.home()
home / pathlib.Path("Photos/image/jpg") # WindowsPath('C:/Users/pauli/Photos/image/jpg')

path = pathlib.Path.home() / "hello.txt"
path  # WindowsPath('C:/Users/pauli/hello.txt')
list(path.parents)  # [WindowsPath('C:/Users/pauli'), WindowsPath('C:/Users'), WindowsPath('C:/')]

for directory in path.parents:
    print(directory)
    
# C:\Users\pauli
# C:\Users
# C:\

path.parent  # WindowsPath('C:/Users/pauli')
path.anchor  # 'C:\\'
type(path.anchor)  # <class 'str'>
path = pathlib.Path("hello.txt")
path.is_absolute() #  False
path.anchor  # ''

home = pathlib.Path.home()
home  # WindowsPath('C:/Users/pauli')
home.name  # 'pauli'
path = home / "hello.txt"
path.name  # 'hello.txt'
path.stem  # 'hello'
path.suffix  # '.txt'

path = pathlib.Path.home() / "hello.txt"
path.exists() # False

path_to_file_exist = pathlib.Path.cwd() / "hello.txt"
path_to_file_exist.exists()  # True

path_to_file_exist.is_file()  # True
path_to_file_exist.is_dir()  # False
home  # WindowsPath('C:/Users/pauli')
home.is_dir() # True

######
#1.
file_path = pathlib.Path.home() / "my_folder" / "my_file.txt"
#2.
file_path.exists()  # False
#3.
file_path.name  # 'my_file.txt'
#4.
file_path.parent  # WindowsPath('C:/Users/pauli/my_folder')
file_path.parents[0]  # WindowsPath('C:/Users/pauli/my_folder')
######

#------12.2------
#
from pathlib import Path

new_dir = Path.cwd() / "new_directory"
#new_dir.mkdir()

new_dir.exists()  # True
new_dir.is_dir()  # True
#error:
#new_dir.mkdir()  # FileExistsError
new_dir.mkdir(exist_ok=True)

if not new_dir.exists():
     new_dir.mkdir()


nested_dir = new_dir / "folder_a" / "folder_b"
#error:
#nested_dir.mkdir()
#Traceback (most recent call last):
#FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki:
#nested_dir.mkdir(parents=True)

#path.mkdir(parents=True, exist_ok=True)

file_path = new_dir / "file1.txt"

file_path.exists()  # False
file_path.touch()
file_path.exists()  # True
file_path.is_file()  # True
file_path.touch()

file_path = new_dir / "folder_c" / "file2.txt"
#error:
#file_path.touch()  # FileNotFoundError

file_path  # WindowsPath('C:/User/<name>/new_directory/folder_c/file2.txt')
file_path.parent  # WindowsPath('C:/Users/<name>/new_directory/folder_c')

if not file_path.parent.exists():
    file_path.parent.mkdir()
file_path.touch()


for path in new_dir.iterdir():
    print(path)

#C:\Users\<nazwa>\new_directory\file1.txt
#C:\Users\<nazwa>\new_directory\folder_a
#C:\Users\<nazwa>\new_directory\folder_c

#list(new_dir.iterdir())    


for path in new_dir.glob("*.txt"):
    print(f"Glob: {path}")

#".txt" - wildcard character

paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image1.png"]

for path in paths:
    if not path.exists():
        path.touch()

print("Files in new_directory with wildcard character")

list(new_dir.glob("*.py"))
#[WindowsPath('C:/Users/<name>/new_directory/program1.py'),
# WindowsPath('C:/Users/<name>/new_directory/program2.py')]

list(new_dir.glob("1*"))
#[]

list(new_dir.glob("*1*"))
#[WindowsPath('C:/Users/<nazwa>/new_directory/file1.txt'),
# WindowsPath('C:/Users/<nazwa>/new_directory/program1.py')]

list(new_dir.glob("program?.py"))
# [WindowsPath('C:/Users/<name>/new_directory/program1.py'),
#  WindowsPath('C:/Users/<name>/new_directory/program2.py')]

list(new_dir.glob("?older_?"))
#[WindowsPath('C:/Users/<name>/new_directory/folder_a'),
# WindowsPath('C:/Users/<name>/new_directory/folder_c')]

list(new_dir.glob("*1.??"))
# [WindowsPath('C:/Users/<name>/new_directory/program1.py')]

list(new_dir.glob("program[13].py"))
# [WindowsPath('C:/Users/<name>/new_directory/program1.py')]

print("Files in new_directory and in subdirectory")

list(new_dir.glob("**/*.txt"))
# [WindowsPath('C:/Users/<name>/new_directory/file1.txt'),
#  WindowsPath('C:/Users/<name./new_directory/folder_c/file2.txt')]

list(new_dir.glob("**/*.py"))
# [WindowsPath('C:/Users/<name>/new_directory/program1.py'),
#  WindowsPath('C:/Users/<name>/new_directory/program2.py'),
#  WindowsPath('C:/Users/<name>/new_directory/folder_a/program3.py')]

# rglob() == "**/"

list(new_dir.rglob("*.py"))
# [WindowsPath('C:/Users/<name>/new_directory/program1.py'),
#  WindowsPath('C:/Users/<name>/new_directory/program2.py'),
#  WindowsPath('C:/Users/<name>/new_directory/folder_a/program3.py')]


source = new_dir / "file1.txt"
destination = new_dir / "folder_a" / "file1.txt"
source.replace(destination)
# WindowsPath('C:/Users/<name>/new_directory/folder_a/file1.txt')

#it is careful:
if not destination.exists():
    source.replace(destination)

source = new_dir / "folder_c"
destination = new_dir / "folder_d"
#source.replace(destination)  # rename or moving

file_path = new_dir / "program1.py"
file_path.exists()  # True
file_path.unlink()
file_path.exists()  # False
list(new_dir.iterdir())
# [WindowsPath('C:/Users/<name>/new_directory/folder_a'),
#  WindowsPath('C:/Users/<name>/new_directory/folder_d'),
#  WindowsPath('C:/Users/<naem>/new_directory/program2.py')]
file_path.exists()  # False
#delete:
#file_path.unlink()  # FileNotFoundError
file_path.unlink(missing_ok=True)

folder_d = new_dir / "folder_d"
folder_d.exists()  # True
# folder_d.rmdir()  # OSError: [WinError 145] Katalog nie jest pusty
 
#for path in folder_d.iterdir():
#    path.unlink()
#folder_d.rmdir()    
folder_d.exists()  # False

#import shutil
#folder_a = new_dir / "folder_a"
#shutil.rmtree(folder_a)
#list(new_dir.rglob("image*.*"))
# []

######
#1
new_dir_e1 = pathlib.Path.cwd() / "my_folder"
if not new_dir_e1.exists():
    new_dir_e1.mkdir()
#2
paths = [
    new_dir_e1 / "file1.txt",
    new_dir_e1 / "file2.txt",
    new_dir_e1 / "image1.png"]

for path in paths:
    if not path.exists():
        path.touch()

#3
source = paths[2]
destination = new_dir_e1 / "images" / "image1.png"
if not destination.parent.exists():
    destination.parent.mkdir()
if not destination.exists():
    source.replace(destination)   

#4
destination.unlink()

#5
file_dir_to_remove = list(new_dir_e1.iterdir())
for path in file_dir_to_remove:
    if path.exists():
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            path.rmdir()
            
new_dir_e1.rmdir()


# Exercise 5
#import shutil

#shutil.rmtree(new_dir)
######
    
