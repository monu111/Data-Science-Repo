import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# importing dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values


# taking care of missing data 

from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
print(X)


# categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le_X = LabelEncoder()                 # it will give 0,1,2 (for france,spain,germany)
X[:,0] = le_X.fit_transform(X[:,0])   # firstly fit the labelencoder then transform orginal arrrarX[:,0]
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('state', OneHotEncoder(), [0])], remainder = "passthrough")  # to create dummy varible,using this we will create new 3 column for france, spain ,germany
X = ct.fit_transform(X)

le_y = LabelEncoder()
y = le_y.fit_transform(Y)    # there is no need of  dummy var. for Y,cause there are 2 types of var. yes(1),no(0),




#### splitting data into training and testing data set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2,random_state = 0)


# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)  # fit scaler then transfrom 
X_test = sc_X.transform(X_test)  # here we don't need fit cause we already applied to X_train


# feature scaling using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler
mmc = MinMaxScaler()
X_train = mmc.fit_transform(X_train)
X_test = mmc.transform(X_test)



