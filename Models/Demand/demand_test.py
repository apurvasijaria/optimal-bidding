import os
import pandas as pd
import pickle
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt # plotting
import seaborn as sns # plotting

from functools import partial # to reduce df memory consumption by applying to_numeric

import sklearn 
from sklearn.metrics import mean_squared_error
import sys
import graphlab as gl 


test_file = '../../DataSets/Demand_Train_Pred_processed.csv'
test_data = pd.read_csv(test_file)
test_data = test_data.drop('Day',axis=1)
test_data = test_data.drop('demand_act',axis=1)

print test_data.head()

test_data = gl.SFrame(test_data)
model = gl.load_model('demand_module')
preds = model.predict(test_data)
preds = pd.DataFrame(np.asarray(preds), columns=['demand_model'])
# preds['demand_model'] = preds['demand_model'].apply(lambda x: 0 if x<=0 else x)
preds.to_csv('demand_test2.csv',index=False)
print preds.head()

