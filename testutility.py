import pandas as pd
import yaml
    
def array_clean(array):
    new_array = [(''.join(y for y in x if y.isalnum() or y==' ')).strip().lower() for x in array]
    return new_array

def config_file(path):
    with open(path,'r') as file:
        att = yaml.safe_load(file)
    return att

def column_validation(df,expected):
    new_column_names = array_clean(df.columns)
    expected_column_names = array_clean(expected)
    trigger = True
    unexpected_columns = [x for x in new_column_names if x not in expected_column_names]
    if len(unexpected_columns) >0:
        print('Columns Not Present in Schema',unexpected_columns)
        trigger = False
    missing_columns = [x for x in expected_column_names if x not in new_column_names]
    if len(missing_columns) >0:
        print('Missing Columns',missing_columns)
        trigger = False
    if trigger:
        df.columns = new_column_names
        print('Sucessfully validated column Names')
        return 1
    else:
        return 0
    
def drop_columns(df,col_names):
    df = df.drop(array_clean(col_names),axis=1)
    return df
