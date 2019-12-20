import pandas as pd 
import numpy as np 
# import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats.stats import pearsonr

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

all_data = pd.concat((train.loc[:,"MSSubClass":"SaleCondition"],
                     test.loc[:, "MSSubClass":"SaleCondition"]))

prices = pd.DataFrame({'price':train['SalePrice'], 'log(price+1)':np.log1p(train['SalePrice'])})
prices.hist()
plt.show()