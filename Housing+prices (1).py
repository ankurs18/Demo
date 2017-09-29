
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().magic('matplotlib inline')

df = pd.read_csv('train.csv')
df.info()
test_df = pd.read_csv('test.csv')

# In[2]:


df[(df['GrLivArea']>4000)& (df['SalePrice']<300000)]


# In[3]:


#sns.swarmplot(x='GrLivArea', y = 'SalePrice', data = df)
#plt.scatter(x='GrLivArea', y = 'SalePrice', data = df)
def clean(df):
    df.drop(df[(df['GrLivArea']>4000)& (df['SalePrice']<300000)].index, axis =0, inplace=True)
    
    
    # In[75]:
    
    
    #df.plot(x = 'SalePrice',kind = 'scatter')
    #sns.swarmplot(df['SalePrice'])
    #sns.countplot(df['SalePrice'])
    #df['PoolArea'].plot(kind = 'hist')
    df.drop('PoolArea', axis = 1, inplace=True)
    
    
    # In[76]:
    
    
    #removing the misleading value of area 1
    df.loc[(df['MasVnrType']=='None') & (df['MasVnrArea']==1),'MasVnrArea']=0
    
    
    # In[ ]:
    
    
    
    
    
    # In[77]:
    
    
    #where area and type both are null, setting them to 0 and none respectively
    print(df.loc[(df['MasVnrType'].isnull()) & (df['MasVnrArea'].isnull()),('MasVnrArea','MasVnrType')])
    df.loc[(df['MasVnrType'].isnull()) & (df['MasVnrArea'].isnull()),('MasVnrArea','MasVnrType')]=0,'None'
    df.loc[(df['MasVnrType'].isnull()) & (df['MasVnrArea'].isnull()),('MasVnrArea','MasVnrType')]
    
    
    # In[ ]:
    
    
    
    
    
    # In[78]:
    
    
    #when area is 0 bt Type is not none, setting type to the mean of area
    df.loc[(df['MasVnrType']!='None') & (df['MasVnrArea']==0),('MasVnrArea')]=df[df['MasVnrArea']!=0]['MasVnrArea'].mean()
    
    
    # In[79]:
    
    
    #when area is not 0 bt Type is none, setting type to the mode of types
    print(df.loc[(df['MasVnrType']=='None') & (df['MasVnrArea']!=0),('MasVnrType','MasVnrArea')])
    df.loc[(df['MasVnrType']=='None') & (df['MasVnrArea']!=0),('MasVnrType')]=df[df['MasVnrType']!='None']['MasVnrType'].mode().iloc[0]
    df.loc[(df['MasVnrType']=='None') & (df['MasVnrArea']!=0),('MasVnrType','MasVnrArea')]
    
    
    # In[80]:
    
    
    print(df[df['MasVnrType']=='None'].count()['Id'])
    print(df[df['MasVnrType'].isnull()].count()['Id'])
    print(df[df['MasVnrArea']==0].count()['Id'])
    print(df[df['MasVnrArea'].isnull()].count()['Id'])
    
    
    # In[81]:
    
    
    #where type is null bt area is greater than 0 setting it to mode of types
    print(df.loc[(df['MasVnrType'].isnull()) & (df['MasVnrArea']!=0),'MasVnrType'])
    df.loc[(df['MasVnrType'].isnull()) & (df['MasVnrArea']!=0),'MasVnrType']=df[df['MasVnrType']!='None']['MasVnrType'].mode()
    df.loc[(df['MasVnrType'].isnull()) & (df['MasVnrArea']!=0),'MasVnrType']
    
    
    # In[82]:
    
    
    print(df['Alley'].unique())
    df['Alley']=df['Alley'].fillna('NA')
    df['Alley'].unique()
    
    
    # In[83]:
    
    
    print(df['LotFrontage'].unique())
    df['LotFrontage']=df['LotFrontage'].fillna(0)
    df['LotFrontage'].unique()
    
    
    # In[84]:
    
    
    print(df['Alley'].unique())
    df['Alley']=df['Alley'].fillna('NA')
    df['Alley'].unique()
    
    
    # In[85]:
    
    
    print(df['BsmtQual'].unique())
    df['BsmtQual']=df['BsmtQual'].fillna('NA')
    df['BsmtQual'].unique()
    
    
    # In[86]:
    
    
    print(df['BsmtCond'].unique())
    df['BsmtCond']=df['BsmtCond'].fillna('NA')
    df['BsmtCond'].unique()
    
    
    # In[87]:
    
    
    print(df['BsmtExposure'].unique())
    df['BsmtExposure']=df['BsmtExposure'].fillna('NA')
    df['BsmtExposure'].unique()
    
    
    # In[88]:
    
    
    print(df['BsmtFinType1'].unique())
    df['BsmtFinType1']=df['BsmtFinType1'].fillna('NA')
    df['BsmtFinType1'].unique()
    
    
    # In[89]:
    
    
    print(df['BsmtFinType2'].unique())
    df['BsmtFinType2']=df['BsmtFinType2'].fillna('NA')
    df['BsmtFinType2'].unique()
    
    
    # In[90]:
    
    
    df['Electrical'].mode().iloc[0]
    df['Electrical']=df['Electrical'].fillna(df['Electrical'].mode().iloc[0])
    
    
    # In[91]:
    
    
    print(df['FireplaceQu'].unique())
    df['FireplaceQu']=df['FireplaceQu'].fillna('NA')
    df['FireplaceQu'].unique()
    
    
    # In[92]:
    
    
    print(df['GarageType'].unique())
    df['GarageType']=df['GarageType'].fillna('NA')
    df['GarageType'].unique()
    
    
    # In[93]:
    
    
    #where GarageYrBlt is missing, set it as YearRemodAdd
    print(df['GarageYrBlt'].unique())
    #df['GarageYrBlt']=df['GarageYrBlt'].fillna(df['YearRemodAdd'])
    df.loc[(df['GarageYrBlt'].isnull()) & (df['GarageType']!='NA'),'GarageYrBlt']=df['YearRemodAdd']
    df.loc[(df['GarageYrBlt'].isnull()) & (df['GarageType']=='NA'),'GarageYrBlt']=0
    #df['GarageYrBlt'].unique()
    df[['YearBuilt','GarageYrBlt','YearRemodAdd']]
    df['GarageYrBlt'].unique()
    
    
    # In[94]:
    
    
    print(df['GarageFinish'].unique())
    df['GarageFinish']=df['GarageFinish'].fillna('NA')
    df['GarageFinish'].unique()
    
    
    # In[95]:
    
    
    print(df['GarageQual'].unique())
    df['GarageQual']=df['GarageQual'].fillna('NA')
    df['GarageQual'].unique()
    
    
    # In[96]:
    
    
    print(df['GarageCond'].unique())
    df['GarageCond']=df['GarageCond'].fillna('NA')
    df['GarageCond'].unique()
    
    
    # In[97]:
    
    
    
    print(df['PoolQC'].unique())
    df['PoolQC']=df['PoolQC'].fillna('NA')
    df['PoolQC'].unique()
    
    
    # In[98]:
    
    
    print(df['Fence'].unique())
    df['Fence']=df['Fence'].fillna('NA')
    df['Fence'].unique()
    
    
    # In[99]:
    
    
    print(df['MiscFeature'].unique())
    df['MiscFeature']=df['MiscFeature'].fillna('NA')
    df['MiscFeature'].unique()
    
    
    # In[100]:
    
    
    
    df['CentralAir_0']=df.apply(lambda x: 1 if x['CentralAir']=='Yes' else 0, axis =1)
    df.drop('CentralAir', axis =1 , inplace=True)
    
    
    # In[101]:
    
    
    df['Garage'] = df.apply(lambda x: np.log(x['GarageCars']*x['GarageArea']+1), axis=1)
    df.head()[['Garage','GarageCars','GarageArea']]
    
    
    # In[102]:
    
    
    df['isRemodAdd']=df.apply(lambda x: x['YearRemodAdd']>x['YearBuilt'], axis =1)
    #sns.lmplot(x='YearBuilt',y='SalePrice',data=df, hue = 'isRemodAdd',scatter_kws={'alpha':0.25})
    df['yrsOld'] = df.apply(lambda x: x['YrSold']-x['YearBuilt'], axis =1)
    #sns.lmplot(x='yrsOld',y='SalePrice',data=df, hue = 'isRemodAdd',scatter_kws={'alpha':0.25})
    df['RemodAddNumYrs'] = df.apply(lambda x: x['YrSold']-x['YearRemodAdd'], axis =1)
    print(df['BsmtFinType1'].head())
    df['numOfBsmt']= df.apply(lambda x: 1 if x['BsmtFinType1']!='NA' and x['BsmtFinType2']=='NA' else 2 if x['BsmtFinType1']!='NA' and x['BsmtFinType2']!='NA' else 0, axis = 1)
    df['TotalFinBsmtSF']=df.apply(lambda x: x['BsmtFinSF2']+x['BsmtFinSF1'], axis =1)
    df['TotalBathsAbvGrnd']=df.apply(lambda x: x['FullBath']+(x['HalfBath']/2), axis =1)
    df['TotalBathsBsmt']=df.apply(lambda x: x['BsmtFullBath']+(x['BsmtHalfBath']/2), axis =1)
    df['GarageYrsOld']=df.apply(lambda x: x['YrSold']-x['GarageYrBlt'], axis =1)
    df['TotalPorchArea']=df.apply(lambda x: x['WoodDeckSF']+x['OpenPorchSF']+x['EnclosedPorch']+x['3SsnPorch']+x['ScreenPorch'], axis =1)
    'Gd', 'TA', 'Ex', 'Fa'
    z = {'Ex': 5, 'Gd': 4, 'TA': 3, 'Fa':2, 'Po':1, 'NA': 0}
    z2 = {'Gd': 3, 'Av':2, 'Mn':1, 'NA': -1, 'No':0}
    z.keys()
    df['HeatingQuality']= df['HeatingQC'].map(z)
    
    df['ExterQuality'] = df['ExterQual'].map(z)
    
    df['KitchenQuality'] = df['KitchenQual'].map(z)
    #df['FireplaceQuality'] = df['FireplaceQu'].map(z)
    
    #df['GarageQuality'] = df['GarageQual'].map(z)
    
    #df['GarageCondition'] = df['GarageCond'].map(z)
    df['PoolQuality'] = df['PoolQC'].map(z)
    df['BsmtCondition'] = df['BsmtCond'].map(z)
    #df['GarageCondition'] = df['GarageCond'].map(z)
    df['BsmtExposureMapped'] = df['BsmtExposure'].map(z2)
    #df['BsmtExposure'].unique()
    #df['ExterCondition'] = df['ExterCond'].map(z)
    #df.drop('OverallQualcond', axis = 1, inplace=True)
    #df['OverallQualcond']=df.apply(lambda x: (x['OverallQual']+x['OverallCond'])/2, axis =1)
    #df['NumOfFloors']=df.apply(lambda x: 1 if x['2ndFlrSF']==0 else 2, axis =1)
    #df[(df['BsmtFinType1']=='NA') &((df['BsmtFinType2']!='NA'))]
    #df[df['numOfBsmt']!=2][['numOfBsmt','BsmtFinType1','BsmtFinType2']]
    #plt.scatter()
    
    
    # In[103]:
    
    
    df['GarageCondition'] = df['GarageCond'].map(z)
    df.drop(['GarageCond'],axis = 1, inplace=True)
    
    
    # In[104]:
    
    
    df.drop(['BsmtExposure'],axis = 1, inplace=True)
    #df.drop(['KitchenQual','HeatingQC','ExterQual'],axis = 1, inplace=True)
    #df.drop(['FireplaceQu','GarageQual'],axis = 1, inplace=True)
    #df.drop(['GarageCond'],axis = 1, inplace=True)
    #df.drop(['PoolQC'],axis = 1, inplace=True)
    #df.drop(['ExterCond'],axis = 1, inplace=True)
    #df.drop(['ExterCond'],axis = 1, inplace=True)
    #df.drop(['BsmtCondition'],axis = 1, inplace=True)
    df.drop(['MiscVal'],axis = 1, inplace=True)
    return df

# In[105]:

df= clean(df)
train_df = clean(train_df)
SalePrice = df[['Id','SalePrice']]
SalePrice[['Id','SalePrice']].iloc[0]
df.columns


# In[ ]:





# In[106]:


#column_types = list()
#for x in df.columns:
#    column_types.append((x,type(df[x].iloc[0])))
column_types=[(x,type(df[x].iloc[0])) for x in df.columns]
cat_columns = [x for (x,coltype) in column_types if coltype==str]
numerical_columns = df.columns.difference(cat_columns)
date_columns = ['YearRemodAdd', 'YrSold' , 'YearBuilt', 'MoSold', 'GarageYrBlt']
len(df.columns) - (len(cat_columns)+len(numerical_columns))
numerical_columns = numerical_columns.difference(['MSSubClass'])
cat_columns = cat_columns.append('MSSubClass')
numerical_columns.difference(date_columns)
print(['Id','SalePrice'].append(date_columns))
cols_normalize = numerical_columns.difference(date_columns)
cols_normalize


# In[ ]:





# In[107]:


from sklearn.preprocessing import StandardScaler
scaler  = StandardScaler()
scaler.fit(df[cols_normalize].drop(['Id','SalePrice'], axis =1))
dff_n = df.copy()
#dff_n[cols_normalize.difference(['Id','SalePrice'])] = pd.DataFrame(scaler.transform(df[cols_normalize].drop(['Id','SalePrice'], axis =1)), columns= cols_normalize.difference(['Id','SalePrice']))
dff_n[cols_normalize.difference(['Id','SalePrice'])] = scaler.transform(df[cols_normalize].drop(['Id','SalePrice'], axis =1))
#dff_n[cols_normalize.difference(['Id','SalePrice'])] =scaler.transform(df[cols_normalize].drop(['Id','SalePrice'], axis =1))
#dff_n = pd.concat(dff_n.append(SalePrice)
#dff_n[['Id','SalePrice']].merge(SalePrice)
dff_n[['Id','SalePrice']] = SalePrice
dff_n.head()



# In[ ]:





# In[ ]:





# In[108]:


#dff=pd.get_dummies(dff_n.drop(['BsmtCond'],axis=1))
dff=pd.get_dummies(dff_n.drop(['numOfBsmt','BsmtUnfSF', 'HalfBath', 'FullBath', 'BsmtFullBath', 'BsmtHalfBath'],axis=1))
#dff['MSSubClass']=pd.get_dummies(dff['MSSubClass'])
#dff=dff.copy()


# In[109]:


dff = dff.merge(pd.get_dummies(dff['MSSubClass'], prefix='MSSubClass'), on = df.index.values)
dff.index.values
dff.drop('MSSubClass', axis = 1, inplace=True)


# In[110]:


from sklearn.model_selection import train_test_split
dff_train = dff.drop(['GarageCars','GarageArea', 'Id', 'SalePrice','YearRemodAdd','YearBuilt', 'WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch'], axis =1)
X_train, X_test, y_train, y_test = train_test_split(dff_train, dff['SalePrice'], test_size=0.3, random_state=101)
y_train = np.log1p(y_train)


# In[111]:


from sklearn.ensemble import RandomForestRegressor
from collections import Counter
rf = RandomForestRegressor(random_state=101)
rf.fit(X_train,y_train)
scores =sorted(list(zip(map(lambda x: round(x, 4), rf.feature_importances_),X_train.columns)),reverse=True)
c =Counter([y.partition('_')[0] for (x,y) in scores])
c['Heating']


# In[ ]:





# In[112]:


from sklearn.metrics import mean_squared_log_error
from math import sqrt
pred = rf.predict(X_test)
pred = np.expm1(pred)
rmse = sqrt(mean_squared_log_error(y_test, pred))
rmse


# In[118]:


from xgboost.sklearn import XGBRegressor

xgb = XGBRegressor()
bst = xgb.fit(X_train,y_train)
preds = xgb.predict(X_test)
preds = np.expm1(preds)
rmse = sqrt(mean_squared_log_error(y_test, preds))
rmse


# In[ ]:





# In[119]:


submission = pd.DataFrame({
        "Id": X_test["Id"],
        "Label": pred
    })


# In[ ]:


import operator
def getscores(scores):
    score = dict()
    for row in scores:
        name = row[1]
        name = name.partition('_')[0]
        if name in score.keys():
            score[name]=score[name]+row[0]
        else:
            score[name]=row[0]
    
    for k, v in score.items():
        score[k]=score[k]/c[k]
    sorted_x = sorted(score.items(), key=operator.itemgetter(1),reverse=True)
    return sorted_x
x = getscores(scores)            
print(type(x))


# In[ ]:





# In[ ]:





# In[116]:


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
selectkbest = SelectKBest(score_func=f_regression, k='all')
fit = selectkbest.fit(X_train, y_train)
scores_kbest =sorted(list(zip(map(lambda x: round(x, 4), fit.scores_),X_train.columns)),reverse=True)
scores_kbest_n = getscores(scores_kbest)
scores_kbest_n


# In[117]:


from sklearn.preprocessing import Normalizer
normalizer  = Normalizer().fit(df[cols_normalize])
dff_n = df.copy()
dff_n[cols_normalize.difference(['Id','SalePrice'])] = pd.DataFrame(normalizer.transform(df[cols_normalize].drop(['Id','SalePrice'], axis =1)), columns= cols_normalize.difference(['Id','SalePrice']))
#dff_n = pd.concat(dff_n.append(SalePrice)
#dff_n[['Id','SalePrice']].merge(SalePrice)
dff_n[['Id','SalePrice']] = SalePrice
dff_n.head()


# In[ ]:




