
import pandas as pd
readCSV = pd.read_csv("clean5.csv", low_memory=False)

array_attributes = ['amenities']

def get_arr(l):
    l = l.str.replace('[', '');
    l = l.str.replace(']', '');
    l = l.str.replace('{', '');
    l = l.str.replace('}', '');
    l = l.str.replace("'", '');
    l = l.str.replace('"', '');
    return l;
listings_arr_fixed = readCSV[array_attributes].apply(lambda col: get_arr(col));

# Next, we get encoded one-hot-dummies for each value in them, prefixed by the column name.
array_dummy_arrs = [];
for col in listings_arr_fixed.columns:
    dummy_arrs = listings_arr_fixed[col].str.get_dummies(sep=',');
    dummy_arrs = dummy_arrs.add_prefix(col + '_');
    array_dummy_arrs.append(dummy_arrs);
    
listings_arr_fixed = pd.concat(array_dummy_arrs, axis=1);
readCSV = pd.concat([listings_arr_fixed], axis=1);
readCSV.to_csv("clean5.csv", index=False)
