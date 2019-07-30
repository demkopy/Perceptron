from math import *
import random
import collections as cols

def weightsInit(n):
    w = [random.randint(0, 100) / 100.0 for _ in range(0, n)]
    return w


def weightedSum(inputData, weights):
    sum = 0
    for i in range(0, len(weights)):
        sum += inputData[i] * weights[i]
    return sum


def activFunc(x):
    return 1.0 / (1.0 + exp(-x))


def guess(inputData, weights, bias = 1):
    return activFunc(weightedSum(inputData, weights) + bias)


def train(inputTestData, outputTestData, weights):
    learningRate = 0.01
    iters = 10000
    for iter in range(iters):
        print("{}% DONE".format(round(iter/iters, 2) * 100))
        for i in range(0, len(inputTestData)):
            out = guess(inputTestData[i], weights)
            target = outputTestData[i]

            for j in range(0, len(weights)):
                inp = inputTestData[i][j]
                delta = -(target - out) * out * (1 - out) * inp
                weights[j] -= delta * learningRate


def randPoint():
    return [random.randrange(-30, 30), random.randrange(-30, 30)]


def check(a, b, point):
    if a * point[0] + b < point[1]:
        return 1
    else:
        return 0


a, b = 2, -10
inputTestData = [randPoint() for _ in range(100)]
outputTestData = [check(a, b, point) for point in inputTestData]

weights = weightsInit(len(inputTestData[0]))
train(inputTestData, outputTestData, weights)

results = []
for _ in range(100):
    point = randPoint()
    prediction = guess(point, weights)
    if prediction > 0.5:
        answer = 1
    else:
        answer = 0

    if answer == check(a, b, point):
        results.append(1)
    else:
        results.append(0)

print("Success: " + str(cols.Counter(results)[1]) + "%")
