# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=None):
    '''
    open csv and parse
    '''
    
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)
            
        if has_headers:
            headers = next(rows)
            
        records=[]
        
        if select:
                indices=[headers.index(col) for col in select]
                headers=select
                
        for row in rows:
            if not row:
                continue
            
            if select:
                row = [row[index] for index in indices]
                
            if types:
                row = [type(val) for type, val in zip(types, row)]       
                
            if has_headers:
                record=dict(zip(headers, row))
            else:
                record=row
                
            records.append(record)
            
    return records
        