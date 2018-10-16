import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
import os
import glob
import re
indv_data_df= pd.read_excel(r'data/input_data/Dataset.xlsx', sheet_name = 'Individuals')
indv_data_df.head()
indv_data_df.shape
carbon_footprint_data_df = pd.read_excel(r'data/input_data/Dataset.xlsx', sheet_name = r'Carbon Footprint', skiprows=1, index_col = 0, na_values=0)
carbon_footprint_data_df
carbon_footprint_data_df.shape
carbon_footprint_data_df_select_data = carbon_footprint_data_df.drop(['Unnamed: 14', 'Notes'], axis = 1)
carbon_footprint_data_df_select_data.shape
carbon_footprint_data_df_select_data_table = pd.melt(carbon_footprint_data_df_select_data, id_vars=['Activity', 'Per'], value_vars=list(carbon_footprint_data_df.columns.values)[2:])
carbon_footprint_data_df_select_data_table.shape
carbon_footprint_data_df_select_data_table_without_na = carbon_footprint_data_df_select_data_table.dropna(axis = 0)
carbon_footprint_data_df_select_data_table_without_na.shape
carbon_footprint_data_df_select_data_table.to_csv(r'data/input_data/Carboon_Footprint_Table.csv')
carbon_footprint_data_df_select_data_table_without_na.to_csv(r'data/output_data/Carboon_Footprint_Table.csv')
indv_data_df.to_csv(r'data/input_data/Individual_Data.csv')
indv_data_df.to_csv(r'data/output_data/Individual_Data.csv')

