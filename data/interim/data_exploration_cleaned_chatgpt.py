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

# Print DataFrame information and Description
dataframes = {
    "Continent Consumption": continent_consumption,
    "Country Consumption": country_consumption,
    "Renewables 1997-2017": renewables_97_17,
    "Top 20 Generation": top20_generation
}

for name, df in dataframes.items():
    print(f'{name} Info:')
    df.info(verbose=True)
    print(f'\n{name} Description:')
    print(df.describe(include='all'))

# Plotting
def plot_dataframe(df, title, kind, x_col, y_cols):
    df.plot(kind=kind, x=x_col, y=y_cols).set_title(title)
    plt.show()

plot_dataframe(continent_consumption, 'Continent Consumption', 'line', 'Year', ['World', 'OECD', 'BRICS', 'Europe', 'North America', 'Latin America', 'Asia', 'Middle-East', 'Africa', 'Pacific', 'CIS'])
plot_dataframe(country_consumption, 'Country Consumption', 'line', 'Year', ['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Canada', 'Brazil', 'France', 'South Korea', 'United Kingdom', 'Italy', 'Mexico', 'Spain', 'Indonesia', 'Iran', 'Saudi Arabia', 'Australia', 'South Africa', 'Turkey'])
plot_dataframe(renewables_97_17, 'Renewables 1997-2017', 'line', 'Year', ['Hydro(TWh)', 'Biofuel(TWh)', 'Solar PV (TWh)', 'Geothermal (TWh)'])
plot_dataframe(top20_generation, 'Top 20 Generation', 'bar', 'Country', ['Hydro(TWh)', 'Biofuel(TWh)', 'Solar PV (TWh)', 'Geothermal (TWh)', 'Total (TWh)'])
