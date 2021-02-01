# ellevation_python_repo

This repo has two folders, process_1_file and process_2000_files_with_multiprocessor. 

Please look at the process_1_file/process_one_file.py file. It is my first take on the solution and processes
one file in 9-10 seconds. It is less well documented, so please do not refer to it for docstrings or
good comments.

process_2000_files_with_multiprocessor has two files. process_one_file_2000.py is well documented and provides
the logic for taking in a file and processing it according to Ellevation's canonical template. 
process_2000_files_multi.py is the runner file. It uses multiprocessing to decrease the time it takes to 
process many files.
