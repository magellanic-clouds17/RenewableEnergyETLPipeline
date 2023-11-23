import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 as sql
import sqlalchemy as sa

# Load CSV files into DataFrames
continent_consumption = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\Continent_Consumption_TWH.csv')
country_consumption = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\Country_Consumption_TWH.csv')
renewables_97_17 = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\renewablePowerGeneration97-17.csv')
top20_generation = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\top20CountriesPowerGeneration.csv')

# Merge country_consumption and top20_generation for the year 2020
# Filter for the year 2020 in country_consumption
consumption_2020 = country_consumption[country_consumption['Year'] == 2020]

# Transpose consumption_2020 to make countries as rows
consumption_2020_transposed = consumption_2020.drop('Year', axis=1).transpose()
consumption_2020_transposed.columns = ['Total_Consumption_TWh']

# Reset index to make 'Country' a column
consumption_2020_transposed.reset_index(inplace=True)
consumption_2020_transposed.rename(columns={'index': 'Country'}, inplace=True)

# Merge the two DataFrames on 'Country'
merged_data = pd.merge(top20_generation, consumption_2020_transposed, on='Country', how='inner')
merged_data.rename(columns={'Total (TWh)': 'Total_Renewable_Generation_TWh'}, inplace=True)

# Visualization of energy generation and consumption
plt.figure(figsize=(12, 6))
merged_data.plot(x='Country', y=['Total_Renewable_Generation_TWh', 'Total_Consumption_TWh'], kind='bar')
plt.ylabel('Energy (TWh)')
plt.title('Comparison of Renewable Energy Generation and Consumption in 2020')
plt.show()

# Removing China from the dataset
merged_data_without_china = merged_data[merged_data['Country'] != 'China']

# Visualization without China
plt.figure(figsize=(12, 6))
merged_data_without_china.plot(x='Country', y=['Total_Renewable_Generation_TWh', 'Total_Consumption_TWh'], kind='bar')
plt.ylabel('Energy (TWh)')
plt.title('Comparison of Renewable Energy Generation and Consumption in 2020 (without China)')
plt.show()

# Save the DataFrames as CSV files
merged_data.to_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\processed\comp_energy_consumption_generation.csv', index=False)
merged_data_without_china.to_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\processed\comp_energy_consumption_generation_without_china.csv', index=False)

# Connect to SQLite database and create tables from DataFrames
conn = sql.connect('energy.db')
engine = sa.create_engine('sqlite:///energy.db')

# Using only the sqlalchemy engine to create tables to avoid redundancy
continent_consumption.to_sql('continent_consumption', engine, if_exists='replace', index=False)
country_consumption.to_sql('country_consumption', engine, if_exists='replace', index=False)
renewables_97_17.to_sql('renewables_97_17', engine, if_exists='replace', index=False)
top20_generation.to_sql('top20_generation', engine, if_exists='replace', index=False)
merged_data.to_sql('comp_energy_consumption_generation', engine, if_exists='replace', index=False)
merged_data_without_china.to_sql('comp_energy_consumption_generation_without_china', engine, if_exists='replace', index=False)
