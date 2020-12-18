
# Backward Elimination 


### importing Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### Load dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

### Encode the categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
le = LabelEncoder()
X[:,3] = le.fit_transform(X[:,3])
# applying Onehot encoding to create dummy var.
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([("Country", OneHotEncoder(), [3])], remainder = 'passthrough')
X = ct.fit_transform(X)


# Remove dummy var trap
X = X[:,1:]
print(X)


### Backward Elimination
#### we will remove the feature, if P>0.5(significant value) means these are less significant.  
import statsmodels.api as sm
# (bydefault it's not take constant(thetas 0 ,we have to put theta_0 * X0 = 1
# that's why we are creating col. of 1's and trying to put in the starting of X)
X = np.append(arr  = np.ones((50,1)).astype(int),values = X, axis = 1)# we are adding 1 extra col. in the starting  of X
print(X)
# np.append(values = X, np.ones((50,1)), axis = 1) # it will add col. at the ending of the X dataset


X_opt =X[:, [0,1,2,3,4,5]].astype(float)  # select all col. from X, for optimal matrix of of feature  that is x_opt
regressor_OLS = sm.OLS(y,X_opt).fit() # fitting OLS 
regressor_OLS.summary()

X_opt =X[:, [0,1,3,4,5]].astype(float)   # removing X2(dummmy var) cause p>SL(significant level =0.5)thats why remove predictor of X2
regressor_OLS = sm.OLS(y,X_opt).fit()  # fit          #    p>SL (0.990 > 0.05)
regressor_OLS.summary()

X_opt =X[:, [0,3,4,5]].astype(float)   # remove X1(dummy var) cause P>SL(0.953 > 0.05)
regressor_OLS = sm.OLS(y,X_opt).fit()
regressor_OLS.summary()

X_opt =X[:, [0,3,5]].astype(float)   #     removing X4(administration) cause P>SL (0.608 > 0.05)
regressor_OLS = sm.OLS(y,X_opt).fit()
regressor_OLS.summary()

X_opt =X[:, [0,3]].astype(float)   # removing X5 (marketing spend) case P>SL(0.060 > 0.05)
regressor_OLS = sm.OLS(y,X_opt).fit()
regressor_OLS.summary()





