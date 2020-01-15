import pandas as pd
import math

# Mean/Average formula for population and sample data
def mean(data):
    sumus = 0
    for d in data:
        sumus += d

    return sumus / len(data)

# Standard Deviation formula for population data
def pop_std_dev(data):
    m = mean(data)
    sumus = 0
    for d in data:
        sumus += (d - m)**2
    return math.sqrt(sumus/len(data))

# Standard deviation for sample data 
def sample_std_dev(data):
    m = mean(data)
    sumus = 0
    for d in data:
        sumus += (d - m)**2
    return math.sqrt(sumus/(len(data) - 1))

# Variance Formula for Population data
def pop_variance(data):
    m = mean(data)
    sumus = 0
    for d in data:
        sumus += (d - m)**2
    return sumus/len(data)

# Variance Formula for Sample Data
def sample_variance(data):
    m = mean(data)
    sumus = 0
    for d in data:
        sumus += (d - m)**2
    return sumus/(len(data) - 1)

# Linear Regression for two datasets x and y
def linear_reg(x, y):
    x_mean = mean(x)
    y_mean = mean(y)

    first_sum = 0
    sec_sum = 0

    for i in range(len(x)):
        first_sum += (x[i] - x_mean) * (y[i] - y_mean)

    for j in range(len(x)):
        sec_sum += (x[i] - x_mean)**2

    b1 = first_sum / sec_sum
    b0 = y_mean - b1 * x_mean
    
    reg = []
    for k in x:
       reg.append(b0 + b1*k)

    return reg

def main():
    # Extract data
    data = pd.read_csv('./data/big_five_stocks.csv')
    print(data.head())
    open_data = data['open']
    closed_data = data['close']

    # Mean
    open_mean = mean(open_data)
    closed_mean = mean(closed_data)

    # Standard Deviation
    open_pop_std = pop_std_dev(open_data)
    open_sample_std = sample_std_dev(open_data)
    closed_pop_std = pop_std_dev(closed_data)
    closed_sample_std = sample_std_dev(closed_data)

    # Variance
    open_pop_var = pop_variance(open_data)
    open_sample_var = sample_variance(open_data)
    closed_pop_var = pop_variance(closed_data)
    closed_sample_var = sample_variance(closed_data)
    
    # Print data
    print('Mean for open data ' + str(open_mean))
    print('Mean for closed data ' + str(closed_mean))
    print('Population standard deviation for open data ' + str(open_pop_std))
    print('Sample standard deviation for open data ' + str(open_sample_std))
    print('Population standard deviation for closed data ' + str(closed_pop_std))
    print('Sample standard deviation for closed data ' + str(closed_sample_std))
    print('Population variance for open data ' + str(open_pop_var))
    print('Sample variance for open data ' + str(open_sample_var))
    print('Population  variance for closed data ' + str(closed_pop_var))
    print('Sample variance for closed data ' + str(closed_sample_var))

main()
