# %% import dependencies

import pandas as pd
from numpy import average

# %% create dictionary of dataframes for each concentration

data = {
    "0.0": pd.read_csv("/Users/owen_hayes/coding/Python/VegetativePropagationLab/data/raw/0.0_Mol_NaCl.csv"),
    "0.08": pd.read_csv("/Users/owen_hayes/coding/Python/VegetativePropagationLab/data/raw/0.08_Mol_NaCl.csv"),
    "0.22": pd.read_csv("/Users/owen_hayes/coding/Python/VegetativePropagationLab/data/raw/0.22_Mol_NaCl.csv"),
    "0.36": pd.read_csv("/Users/owen_hayes/coding/Python/VegetativePropagationLab/data/raw/0.36_Mol_NaCl.csv"),
    "0.5": pd.read_csv("/Users/owen_hayes/coding/Python/VegetativePropagationLab/data/raw/0.50_Mol_NaCl.csv")
}

# %% converted data to dictionary

processed = {}
for k in data:
    processed[k] = {col.split(" ")[1]: data[k][col] for col in data[k].columns}

# %% find averages
averages = [[pd.Series.mean(processed[k][j]) for j in processed[k]] for k in processed]
print([average(x) for x in averages])