#%%

import os.path

import pandas as pd

package_directory = os.path.dirname(os.path.abspath(__file__))

raw_data = {
    "0.0": pd.read_csv(os.path.join(package_directory, '0.0_Mol_NaCl.csv')),
    "0.08": pd.read_csv(os.path.join(package_directory, '0.08_Mol_NaCl.csv')),
    "0.22": pd.read_csv(os.path.join(package_directory, '0.22_Mol_NaCl.csv')),
    "0.36": pd.read_csv(os.path.join(package_directory, '0.36_Mol_NaCl.csv')),
    "0.5": pd.read_csv(os.path.join(package_directory, '0.50_Mol_NaCl.csv'))
}
