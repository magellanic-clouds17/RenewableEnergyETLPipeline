import pandas as pd
import matplotlib.pyplot as plt

"""
    !!! non_renewables and renewables_total data frames have the same values in the Contribution (TWh) column !!!
    !!! this must be an error in the data !!!
    !!! both data frames are therefore excluded from the analysis !!!
 """

# Load CSV files
continent_consumption = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\Continent_Consumption_TWH.csv')
country_consumption = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\Country_Consumption_TWH.csv')
renewables_97_17 = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\renewablePowerGeneration97-17.csv')
top20_generation = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\top20CountriesPowerGeneration.csv')

## Merge country_consumption and top20_generation on Country column for year 2020 (top20_generation only has data for 2020)
# Filter country_consumption for 2020
consumption_2020 = country_consumption[country_consumption['Year'] == 2020]

# Transpose the DataFrame to make countries as rows
consumption_2020_transposed = consumption_2020.drop('Year', axis=1).transpose()
consumption_2020_transposed.columns = ['Total_Consumption_TWh'] # only keep the Total_Consumption_TWh column

# Reset the index to make 'Country' a column
consumption_2020_transposed.reset_index(inplace=True)
consumption_2020_transposed.rename(columns={'index': 'Country'}, inplace=True)

# Merge the two DataFrames
merged_data = pd.merge(top20_generation, consumption_2020_transposed, on='Country', how='inner')

# change column name from 'Total (TWh)' to 'Total_Renwable_Generation_TWh'
merged_data.rename(columns={'Total (TWh)': 'Total_Renwable_Generation_TWh'}, inplace=True)

## Visualization
merged_data.plot(x='Country', y=['Total_Renwable_Generation_TWh', 'Total_Consumption_TWh'], kind='bar')
plt.ylabel('Energy (TWh)')
plt.title('Comparison of Renewable Energy Generation and Consumption in 2020')
plt.show()

# drop china from merged_data and store it in a new DataFrame named merged_data_without_china
merged_data_without_china = merged_data[merged_data['Country'] != 'China']

# plot merged_data_without_china
merged_data_without_china.plot(x='Country', y=['Total_Renwable_Generation_TWh', 'Total_Consumption_TWh'], kind='bar')
plt.ylabel('Energy (TWh)')
plt.title('Comparison of Renewable Energy Generation and Consumption in 2020 (without China)')
plt.show()
