import re
import linecache
import pandas as pd
print("pingu")
from pandas import DataFrame
import numpy as np
import csv
import os
import statistics

# 'O:/HLS_Projects/matrix_mult_2019/solution1/.autopilot/db/a.o.3.ll'
#test code
path_name_begin = 'O:/HLS_Projects/BenchMarks_Hls/dfDiv_BM/division'
path_name_begin2 = 'O:/HLS_Projects/apdcm'
path_name_begin3 = 'O:/HLS_Projects/matrix_mult_2000'
path_name_begin4 = 'O:/total_new_apdcm/total_new_solution8'
path_name_end = '/.autopilot/db/float64_div.verbose.bind.rpt'
input_function_name = 'encode'
file_list = []
for root, dirs, files in os.walk(path_name_begin4):
    for file in files:
        if file.endswith(".res"):  # for timing and latency
            name1 = os.path.join(root, file)
            name2 = name1.replace('\\', '/')
            file_list.append(name2)

max_path_length=0
max_out_edges=0
max_in_edges=0
total_nodes=0
for file_name in file_list:
    labels=[]

    ### ------------features from basic block-------------------------------------
    other_op_bb_list = []
    with open(file_name, 'rt') as file:
        for num, line in enumerate(file, 1):
            if 'max path length' in line:
                max_path_length=line.split(" ")[3]
            elif 'max number of outgoing edges=' in line:
                max_out_edges=line.split(" ")[6]
            elif 'max number of incoming edges=' in line:
                max_in_edges=line.split(" ")[6]
            elif 'total number of nodes=' in line:
                total_nodes=line.split(" ")[5]
            elif 'label=' in line:
                label_no=line.split(" ")[1].split('|')[0].split('%')[1]
                labels.append(label_no)
    labels.pop(0)



print("max path length= ", max_path_length, "\n max out going edges= ", max_out_edges, "\n max in coming edges= ", max_in_edges, "\n total num of nodes= ", total_nodes)

print(labels)