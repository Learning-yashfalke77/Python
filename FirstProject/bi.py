import statistics
from numpy import quantile

data = [13, 15, 16, 16, 19, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

print("Mean :", statistics.mean(data))
print("Median :", statistics.median(data))
print("Mode :", statistics.mode(data))
print("Variance :", statistics.variance(data))
print("Standard Deviation :", statistics.stdev(data))
print("Midrange :", (max(data) + min(data)) / 2)
q1, q2, q3 = quantile(data, [0.25, 0.5, 0.75])
print("5-number summary :", [min(data), q1, statistics.median(data), q3, max(data)])
