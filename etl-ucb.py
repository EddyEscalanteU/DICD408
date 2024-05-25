# Required Libraries
import pandas as pd
import numpy as np

# Extraction
wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine_data = pd.read_csv(wine_url, header=None)

wine_quality_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_data = pd.read_csv(wine_quality_url, sep=";")

# Initial look at the data
#print(wine_data.head())
#print(wine_quality_data.head())

# Transformation
# Assigning meaningful column names
wine_data.columns = ['class', 'alcohol', 'malic acid', 'ash',
                     'alcalinity of ash', 'magnesium', 'total phenols',
                     'flavonoids', 'nonflavonoid phenols', 'proanthocyanidins',
                     'color intensity', 'hue', 'OD280/OD315 of diluted wines',
                     'proline']

# Converting Class column into categorical datatype
wine_data['class'] = wine_data['class'].astype('category')

# Checking for any missing values in both datasets
print(wine_data.isnull().sum())
print(wine_quality_data.isnull().sum())

# Normalizing 'alcohol' column in the wine_data using Min-Max normalization
wine_data['alcohol'] = (wine_data['alcohol'] - wine_data['alcohol'].min()) / (wine_data['alcohol'].max() - wine_data['alcohol'].min())

wine_data['alcohol'] = wine_data['alcohol'] * 10

# Loading
# Saving the transformed data as a csv file
wine_data.to_csv('wine_dataset.csv', index = False)
wine_quality_data.to_csv('wine_quality_dataset.csv', index = False) 



# Live Share VS Code
# https://prod.liveshare.vsengsaas.visualstudio.com/join?2164B09DADFF4C0820305BF4BF8865BCC21C
# https://prod.liveshare.vsengsaas.visualstudio.com/join?5685C665E8F5745FAC49D461DEAD76679157