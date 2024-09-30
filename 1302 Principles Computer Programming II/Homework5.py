# Using pandas databasing to store create data structures, and presenting them though matplotlib via graphing mechinizems, and using commenting to make code readable and reproducable

import pandas as pd
import matplotlib.pyplot as plt

# This line gets the data from the csv file and places it into a pandas dataframe
data = pd.read_csv('car_data.csv')

# Here the shape of the data is attained and then printed with the .shape function
# The line under this one is solution for 1
print('Shape of dataframe:   ' + str(data.shape))

# Here we attain the data on which car has 6 cylinders giving a boolean expression
# as well as seeing which place of origin is Japan also producing a boolean expression
# The line under this starts the solution for 2
cy = data['cylinders'] == 6
place = data['origin'] == 'japan'

# This for loop goes and finds the index of all places that produced true for Japan
x = 0
places = []
for p in place:
    if p:
        x = x + 1
        places.append(x)
    else:
        x = x + 1

# This for loop goes and finds the index of all cylinders that produced true for 6
x = 0
cyl = []
for c in cy:
    if c:
        x = x + 1
        cyl.append(x)
    else:
        x = x + 1

# This for loop uses another for loop to compare the list of Japan origin cars to 6-cylinder cars
common = []
for p in places:
    for c in cyl:
        if p == c:
            common.append(c)

# This for loop takes the list of common index and finds the name of the car
cars = []
for c in common:
    cars.append(data.loc[c - 1, 'name'])

print('Japanese v6 cars: ', cars)
# The line above finishes teh solution for 2

# Here we get the data for the horsepower
# The line under this starts the solution for 3
horsepower = data['horsepower']

# This for loop sees if there is a value greater than 1 (in context of horsepower it needs to be much greater than 1)
# and then adds the index to a list
x = 0
no_horse_power = []
for hp in horsepower:
    if hp >= 1:
        x = x + 1
    else:
        x = x + 1
        no_horse_power.append(x)

# This for loop takes the list of index without horsepower and finds the name
cars = []
for hp in no_horse_power:
    cars.append(data.loc[hp - 1, 'name'])

print('Cars with missing horsepower data: ', cars)
# The line above ends the solution to 3

# This is where the data for the mpg is isolated
# The line under this starts number 4
mpg = data['mpg']

# This for loop looks through the mpg data and adds it to a list if it is greater than 20
mpg_list = []
x = 0
for m in mpg:
    if m >= 20:
        x = x + 1
        mpg_list.append(x)
    else:
        x = x + 1

# Here the list of 20 and more mpg is counted
x = 0
for num in mpg_list:
    x = x + 1

print('Number of cars having mpg >= 20: ' + str(x))
# The line above this ends the solution for 4

# Here we sort the data from the mpg variable created earlier that contains mpg in greatest to the least order
# the car_name var takes the data set and takes the mpg and sets it to find the highest mpg with the ac_mpg.iloc[0]
# then using the .name it gets the information of the car and then using the .iloc[0] again gives us the cars name value
# The line below starts the solution to 5
print('Most fuel efficient car: ', [data[(mpg == mpg.sort_values(ascending=False).iloc[0])].name.iloc[0]])
# The line above prints / ends the solution to 5

# The line below starts the solution for 6
weight = data['weight']
max_w = weight.sort_values(ascending=False).iloc[0]
min_w = weight.sort_values(ascending=True).iloc[0]
# Max_w is the weight sorted in greatest to least, and then picks the top one as the max
# Min is the weight sorted in least to greatest, and then picks the top one as the min

# This for loop adds all the weight up into the total var
total = 0
for w in weight:
    total = total + w

# The avg var takes the total var and then divides it by the index amount to give and average
avg = total/data.shape[0]
print('minimum weight: ' + str(min_w) + ', maximum weight: ' + str(max_w) + ', average weight: ' + str(round(avg, 2)))
# This ends the solution for 6

# The drop_data var drops all the database sets that do not have a value
# The line below starts the solution for 7
drop_data = data.dropna(axis=0)
print('Shape after removing the missing values: ' + str(drop_data.shape))
# The line above ends the solution for 7

# Here we take the data of weights of the cars, and use the for loop to place the weights to a list
# The line under starts the solution to 8
weight = data['weight']
x = 0
weights = []
for w in weight:
    weights.append(weight.loc[x])
    x = x + 1

# Here we take the data of mpg of the cars, and use the for loop to place the mpg to a list
mpgs = data['mpg']
x = 0
mpg_l = []
for m in mpgs:
    mpg_l.append(mpgs.loc[x])
    x = x + 1

# Here we take the data of displacement of the cars, and use the for loop to place the displacement to a list
dis = data['displacement']
x = 0
disp = []
for d in dis:
    disp.append(dis.loc[x])
    x = x + 1

# here the first subplot is created, and it uses the mpg list as well as the weights list to get the data
plt.subplot(2, 1, 1)
plt.scatter(mpg_l, weights)
plt.ylabel('weight')

# Here the second subplot is created, and it uses the mpg list as well as the displacement list to get the data
plt.subplot(2, 1, 2)
plt.scatter(mpg_l, disp)
plt.ylabel('displacement')
plt.xlabel('mpg')
 
plt.show()
# The line above ends the solution of 8
