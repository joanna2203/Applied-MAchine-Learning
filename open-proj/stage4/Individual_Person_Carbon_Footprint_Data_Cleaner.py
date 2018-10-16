# coding: utf-8
# 
import pandas as pd
import numpy as np
individuals_carbon_footprint_df = pd.read_excel(r'data/input_data/Dataset.xlsx', sheet_name='Individuals')
individuals_carbon_footprint_df.head()
individuals_carbon_footprint_df.shape
individuals_carbon_footprint_table = pd.melt(individuals_carbon_footprint_df, id_vars=['Indnum', 'Group', 'Activity', 'Units', 'Consumption', 'Quality_of_Life_Importance__1_10'], value_vars=individuals_carbon_footprint_df.columns.values[6:], var_name='Name of Resource Used', value_name='Amount of Resource Used per Unit')
individuals_carbon_footprint_table.head()
individuals_carbon_footprint_table.shape
individuals_carbon_footprint_table_drop_na = individuals_carbon_footprint_table.dropna(axis = 0)
individuals_carbon_footprint_table_drop_na.head()
individuals_carbon_footprint_table_drop_na.shape
individuals_carbon_footprint_table_replace_na_zero = individuals_carbon_footprint_table
individuals_carbon_footprint_table_replace_na_zero['Amount of Resource Used per Unit'] = np.nan_to_num(individuals_carbon_footprint_table_replace_na_zero['Amount of Resource Used per Unit'])
individuals_carbon_footprint_table_replace_na_zero.head()
individuals_carbon_footprint_table_replace_na_zero.shape
individuals_carbon_footprint_table_drop_na.to_csv(r'data/output_data/Individuals_Carbon_Footprint_NA_Dropped.csv', index=False)
individuals_carbon_footprint_table_replace_na_zero.to_csv(r'data/output_data/Individuals_Carbon_Footprint_NA_Zeroed.csv', index=False)

