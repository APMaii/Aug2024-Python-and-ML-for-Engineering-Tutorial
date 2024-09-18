#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:34:51 2024

@author: apm


command + space --> Terminal

windows---> win+R
wt


globally--> all over system
but env is isolated


python --version

and ....




pwd
Print Working Directory
Shows the current directory path.



ls
List
Lists files and directories in the current directory.
bash
Copy code
ls        # Basic listing
ls -l     # Detailed listing
ls -a     # Include hidden files



cd
Change Directory
Changes the current directory.
bash
Copy code
cd /path/to/directory   # Navigate to specified directory
cd ..                   # Move up one directory
cd ~                    # Move to the home directory



rm
Remove
Deletes files or directories. Use with caution.
bash
Copy code
rm file_name               # Remove a fil





cp
Copy
Copies files or directories.
bash
Copy code
cp source_file destination_file    # Copy file
cp -r source_directory destination_directory   # Copy directory




mv
Move
Moves or renames files and directories.
bash
Copy code
mv old_name new_name         # Rename a file or directory
mv file_name /new/path/      # Move file to a new directory



touch
Create Empty File
Creates a new empty file or updates the timestamp of an existing file.
bash
Copy code
touch new_file


find
Find Files
Searches for files and directories.
bash
Copy code
find /path/to/search -name 'filename'



kill
Terminate Process
Sends signals to processes, usually to terminate them.
bash
Copy code
kill PID           # Terminate process with ID PID
kill -9 PID        # Forcefully terminate process


wget
Download Files
Downloads files from the web.
bash
Copy code
wget http://example.com/file


history
Command History
Displays the command history.
bash
Copy code
history






-------
conda env list

conda info --envs




conda create --name myenv python=3.8

Here, myenv is the name of the environment, and python=3.8 specifies 
the version of Python you want to install in that environment. You can also 
include other packages by listing them after the python version, e.g., numpy pandas.





conda activate myenv


conda deactivate


conda install package_name

conda install requests

pip install 







conda activate myenv
python my_script.py




conda list

conda deativate


conda remove --name myenv --all




"""

