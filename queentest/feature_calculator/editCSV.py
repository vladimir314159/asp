import csv
import numpy
import operator
import pandas as pd
import 
#from calculateBestEncoding import queen11, queen4

f = pd.read_csv("data80.csv")

MaxQcol_array = []
MaxQdiagonal_array = []
MaxQrow_array = []
blockednsq_array = []
n_array = []
queens_encoding_array = []

for number in range(4000,4900):
    

keep = ['MaxQcol','MaxQrow','AvgQcol','blocked/n^2','n','class']

f[keep].to_csv("data80.csv", index=False)

