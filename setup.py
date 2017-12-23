from cx_Freeze import setup, Executable

setup(name = "cryptodwarf" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("cryptodwarf/cli.py")])
