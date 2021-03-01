## 3. Populations and Samples ##

question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

## 4. Sampling Error ##

import pandas as pd
wnba = pd.read_csv('wnba.csv')
print(wnba.head())
print(wnba.tail())
shape = wnba.shape
games_played = wnba['Games Played']
parameter = games_played.max()
sample = games_played.sample(30, random_state=1)
statistic = sample.max()
sampling_error = parameter - statistic

## 5. Simple Random Sampling ##

import pandas as pd
import matplotlib.pyplot as plt

wnba = pd.read_csv('wnba.csv')

pts = wnba['PTS']
mean_pts = pts.mean()

sample_means = []
x_axis = range(1, 101)

for i in range (0, 100):
    sample = pts.sample(10, random_state=i)
    sample_means.append(sample.mean())

print(sample_means)
plt.scatter(x_axis, sample_means)
plt.axhline(mean_pts)
    
    

## 7. Stratified Sampling ##

wnba['points_per_game'] = wnba['PTS']/wnba['Games Played']

strata = []
stratum_C = wnba[wnba['Pos']=='C']
strata.append((stratum_C, 'C'))
stratum_F = wnba[wnba['Pos']=='F']
strata.append((stratum_F, 'F'))
stratum_FC = wnba[wnba['Pos']=='F/C']
strata.append((stratum_FC, 'F/C'))
stratum_G = wnba[wnba['Pos']=='G']
strata.append((stratum_G, 'G'))
stratum_GF = wnba[wnba['Pos']=='G/F']
strata.append((stratum_GF, 'G/F'))

points_per_position = {}

for stratum, position in strata:
    sample = stratum['points_per_game'].sample(10, random_state=0)
    points_per_position[position] = sample.mean()
    
position_most_points = max(points_per_position, key=points_per_position.get)

print(max(points_per_position))
    

    