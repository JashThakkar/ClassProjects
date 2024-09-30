# Three funtions that take an observed and predicted set of numbers and then it gives the MSE, RMSE, and MAE

import math


def computeMSE(observed, predicted):
    net = x = 0

    for op in observed and predicted:
        diff = (int(observed[x]) - int(predicted[x]))
        sqr = diff * diff
        net = net + sqr
        x = x + 1

    mse = round(net / len(observed), 2)
    print('MSE = ' + str(round(mse, 2)))


def computeRMSE(observed, predicted):
    net = x = 0

    for op in observed and predicted:
        diff = (int(observed[x]) - int(predicted[x]))
        sqr = diff * diff
        net = net + sqr
        x = x + 1

    mse = round(net / len(observed), 2)
    rt = math.sqrt(mse)
    print('RMSE = ' + str(round(rt, 2)))

def computeMAE(observed, predicted):
    net = x = 0

    for op in observed and predicted:
        diff = (int(observed[x]) - int(predicted[x]))
        if diff < 0:
            diff = diff * -1

        net = net + diff
        x = x + 1

    mae = round(net / len(observed), 2)
    print('MAE = ' + str(round(mae, 2)))

#Driver code

observed = input('observed = ')
predicted = input('predicted = ')
observed = observed.split(sep=',')
predicted = predicted.split(sep=',')

computeMSE(observed, predicted)
computeRMSE(observed, predicted)
computeMAE(observed, predicted)
