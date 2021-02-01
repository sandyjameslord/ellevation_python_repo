"""
Author: Sandy Lord
Date: January 31, 2021
Purpose: To process 2000+ files as rapidly as possible for the Ellevation Data Challenge:
Standardized Test Score File Processing.
"""

#import the processing file
import process_one_file_2000 as process_data

# import Process from multiprocessing to spread computing across many cores
from multiprocessing import Process

# import timeit to examine performance
import timeit


def process_2000_files():
    """For the purposes of this processing, I am assuming that all 2000 csvs of sample-mcas-data are in a
    local folder called data. To simulate processing 2000 files, I am initializing a variable and using
    modulus to take in 10 files ending in (0..9) 200 times each and creating 2000 csv files that are
    1x to 3x times larger, depending on the number of tests taken."""
    i = 0
    while i < 2000:
        # initialize a Process for each processing event. This allows each process to run simultaneously, decreasing
        # processing time greatly. The target is the process_one_client function, which takes two args, the name of
        # the client input file, and an index for naming the created files.
        p = Process(
            target=process_data.process_one_client,
            args=(f"./data/sample-mcas__{(i % 10 % 10 % 10)}.csv", i)
        )
        p.start()
        i += 1

# print("time it takes to process 50 files (seconds): ", timeit.timeit(process_2000_files, number=1))
