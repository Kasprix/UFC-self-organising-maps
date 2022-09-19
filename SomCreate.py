from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn import preprocessing
from operator import itemgetter

labels = pd.read_csv(
    r'C:\Users\reece\Google Drive\University\Diss\Python Programs\Dissertation\FilteredPandasFighterListWithNamesFINAL.csv', delimiter=',', usecols=[0])

data = pd.read_csv(
    r'C:\Users\reece\Google Drive\University\Diss\Python Programs\Dissertation\FilteredPandasFighterListWithNamesFINAL.csv', delimiter=',', usecols=[2, 3, 4, 5, 6, 7, 8, 9])

x = data.values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
normalisedValues = pd.DataFrame(x_scaled)

numpyX = pd.DataFrame(normalisedValues).to_numpy()

# print(numpyX)


som = MiniSom(13, 13, 8, sigma=3, learning_rate=.5,
              neighborhood_function='gaussian', random_seed=10)
som.train(numpyX, 500, verbose=True)

#print("SOM fitted!")

data['X'] = ' '
data['Y'] = ' '
# print(data)

counter = 0

for item in numpyX:
    # print(som.winner(item))
    text = str(som.winner(item))
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.split(",")
    data.at[counter, 'X'] = text[0]
    data.at[counter, 'Y'] = text[1]
    print(text)
    counter = counter + 1

frames = pd.DataFrame(labels.join(data))

frames.to_csv(r'C:\Users\reece\Google Drive\University\Diss\Python Programs\Dissertation\Results\NeighbourhoodIterations\13x13\500.csv',
              encoding='utf-8', index=False)

# print(labels.join(data))

fig = plt.figure()
plt.pcolor(som.distance_map().T, cmap='magma')
cbar = plt.colorbar()
cbar.set_label('Intensity of fighters within a Coordinate',
               rotation=270, labelpad=14)
fig.suptitle(
    'Heatmap Showing a Self Organasing Map With a \n13x13 Neighbourhood Trained for 500 Iterations', fontsize=15)
plt.xlabel('X Coordinates', fontsize=18)
plt.ylabel('Y Coordinates', fontsize=18)
fig.savefig(r'C:\Users\reece\Google Drive\University\Diss\Python Programs\Dissertation\Results\NeighbourhoodIterations\13x13\500.png')
plt.show()
# print(numpyX)
