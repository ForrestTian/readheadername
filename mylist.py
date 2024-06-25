# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:04:09 2024
For GISLab04 Function
@author: Forrest Tian
"""

import csv

def listheadernames(csvfilepath):
    with open(csvfilepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        header = next(reader)
        return list(header), reader.line_num
    
    
#
if __name__ == "__main__":
    streetscsv = r"streets.csv"
    # invoke the function
    header, line_num = listheadernames(streetscsv)
    print(f"line:{line_num}")
    print(header)