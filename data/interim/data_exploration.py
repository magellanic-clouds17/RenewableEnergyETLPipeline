import pandas as pd
import matplotlib.pyplot as plt

    """
    !!! non_renewables and renewables_total data frames have the same values in the Contribution (TWh) column !!!
    !!! this must be an error in the data !!!
    !!! both data frames are therefore excluded from the analysis !!!
    """

# load csv files

continent_consumption = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\Continent_Consumption_TWH.csv')
country_consumption = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\Country_Consumption_TWH.csv')
#non_renewables = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\nonRenewablesTotalPowerGeneration.csv')
renewables_97_17 = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\renewablePowerGeneration97-17.csv')
#renewables_total = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\renewablesTotalPowerGeneration.csv')
top20_generation = pd.read_csv(r'C:\Users\Latitude\Desktop\Kaggle\global_energy_consumption_and_renewable_generation\portfolio_project_retoflow\data\raw\top20CountriesPowerGeneration.csv')

## info about the dataframes print the name of the data frame before showing the info

print('continent_consumption')
continent_consumption.info(verbose=True)
print('country_consumption')
country_consumption.info(verbose=True)
#print('non_renewables')
#non_renewables.info(verbose=True)
print('renewables_97_17')
renewables_97_17.info(verbose=True)
#print('renewables_total')
#renewables_total.info(verbose=True)
print('top20_generation')
top20_generation.info(verbose=True)

## describe the dataframes print Desciption + the name of the data frame before showing the description

print('Description continent_consumption')
continent_consumption.describe(include='all')
print('Description country_consumption')
country_consumption.describe(include='all')
#print('Description non_renewables')
#non_renewables.describe(include='all')
print('Description renewables_97_17')
renewables_97_17.describe(include='all')
#print('Description renewables_total')
#renewables_total.describe(include='all')
print('Description top20_generation')
top20_generation.describe(include='all')

## visualize the columns of each data frame as a line in a seperate line plot for each data frame

# continent_consumption add title "Continent Consumption" to the above plot
continent_consumption.plot.line(x='Year', y=['World', 'OECD', 'BRICS', 'Europe', 'North America', 'Latin America','Asia', 'Middle-East', 'Africa','Pacific','CIS']).set_title('Continent Consumption')
plt.show()

# country_consumption add title "Country Consumption"
country_consumption.plot.line(x='Year', y=['China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Canada', 'Brazil', 'France', 'South Korea', 'United Kingdom', 'Italy', 'Mexico', 'Spain', 'Indonesia', 'Iran', 'Saudi Arabia', 'Australia', 'South Africa', 'Turkey']).set_title('Country Consumption')    
plt.show()

# non_renewables add title "Non-Renewables"
#non_renewables.plot.bar(x='Mode of Generation', y='Contribution (TWh)').set_title('Non-Renewables')
#plt.show()

# renewables_97_17 add title "Renewables 1997-2017"
renewables_97_17.plot.line(x='Year', y=['Hydro(TWh)', 'Biofuel(TWh)', 'Solar PV (TWh)', 'Geothermal (TWh)']).set_title('Renewables 1997-2017')
plt.show()

# renewables_total add title "Renewables Total"
#renewables_total.plot.bar(x='Mode of Generation', y='Contribution (TWh)').set_title('Renewables Total')
#plt.show()

# top20_generation add title "Top 20 Generation"
top20_generation.plot.bar(x='Country', y=['Hydro(TWh)', 'Biofuel(TWh)', 'Solar PV (TWh)', 'Geothermal (TWh)', 'Total (TWh)']).set_title('Top 20 Generation')
plt.show()


