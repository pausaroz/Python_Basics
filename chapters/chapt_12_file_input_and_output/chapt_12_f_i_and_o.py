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
file_path.exists()
False
#3.
file_path.name
'my_file.txt'
#4.
file_path.parent
WindowsPath('C:/Users/pauli/my_folder')
file_path.parents[0]
WindowsPath('C:/Users/pauli/my_folder')
######
