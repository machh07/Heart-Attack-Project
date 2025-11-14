#Programming in Science (420-SN1-RE)
#Presented to: Mr. Tiago Bortoletto Vaz
#Coded by: Marie-Ange Chhuon, Neshama Gozlan, Carlyn Matar

#Import modules
import pandas as pd
import seaborn as sns

#Import dataset
df = pd.read_csv("Medicaldataset.csv")

# 2 Preliminary steps
#Initial data inspection
print(df.info())
print(df.describe())
print(df.nunique())
#Handle duplicate entries
print(df.duplicated().value_counts()) #There are no duplicates in this dataset 
#Identify and manage missing values
print(df.isnull()) #There are no missing values in any of the columns in the dataset.



# 3 Univariate non-graphical EDA
#numerical values
numerical_variables =["Age", "Heart rate","Systolic blood pressure" ,"Diastolic blood pressure" , "Blood sugar","CK-MB", "Troponin"]
for num in numerical_variables:
    print("Mean:", df[num].mean())
    print("Median:", df[num].median())
    print("Mode:", df[num].mode())
    print("Variance:", df[num].var())
    print("Skewness:", df[num].skew())
    print("Kurtosis:", df[num].kurt())
    print("Quartiles:", df[num].quantile([0.25, 0.5, 0.75]))
#categorical variables
categorical_variables = ["Gender","Result"]
for cat in categorical_variables:
    print("Frequency counts:", df[cat].value_counts())
    print("Proportions:", df[cat].value_counts(normalize=True)*100)
    print("Mode:", df[cat].mode())
    print("Number of unique categories:", df[cat].nunique())
#4 Univariate graphical EDA 

for num in numerical_variables:
    
 sns.displot(df, x= num ,bins=20)
 sns.displot(df, x=num ,hue= "Gender") 
 sns.displot(df, x= num , hue ="Gender" , multiple="stack")
 sns.displot(df, x= num , hue ="Gender" , multiple="dodge") 
 sns.displot(df, x= num , hue = "Result" , stat= "density" , common_norm=False) 
 sns.displot(df, x= num, kind="kde", bw_adjust = 4) 
 sns.displot(df, x=num ,hue= "Gender", kind="ecdf")
 
 #Multivariate non-graphical EDA
 #A
 print(pd.crosstab(df["Gender"],df["Result"])) #We can observe that males (represented by the number 1) are more susceptible to heart attacks than females (represented by the number 0)
 #Since we only have 2 categorical variables, this is the only outcome possible for a crosstab.
 #B (Normalize with columns)
 print(pd.crosstab(df["Gender"],df["Result"], normalize = "columns"))
 #Once again, we observe a higher proportion of males suffering from heart attacks than females.
 #C
 #With only 2 categorical variables in our dataset, we are unable to generate a three-way frequency table.




#Multivariate graphical EDA
#importing matplotlib module to prevent overlapp of graphs 

import matplotlib.pyplot as plt 

#Filtering our data to erase possible mistakes (unrealistic and impossible heart rate values) to have cleaner graphs
df = df[df['Heart rate'] <= 220]

#6.1.Visualizing statistical relationships 

#a) Using Faceting feature
sns.relplot(df, x='Systolic blood pressure', y='Diastolic blood pressure', col='Result')
plt.show()

#b) Representing 5 variables   
sns.relplot(df, x="Age", y="Troponin", size='CK-MB', hue="Result", col="Gender", kind="scatter" )
plt.show()

#c) kind = line does not show a relation between both for some reason
sns.relplot(df, x="Age", y="Systolic blood pressure", kind="line")
plt.show()


#d) Standard deviation (NOT WORKING!! MERGING 2 PLOTS TOGETHER FIX!!)
sns.barplot(df, x="Result", y="CK-MB", errorbar="sd")
plt.show()

#e) linear regression 
sns.lmplot(df, x='Systolic blood pressure', y='Diastolic blood pressure')
plt.show()

#6.2 Visualizing categorical data
#grouping numerical variables into categorical data
df['grouped_age'] = pd.cut(df['Age'], bins=[14, 30, 50, 80, 108], labels=['Young', 'Adult','Older adults', 'Elderly'])
df['grouped_sbp'] = pd.cut(df['Systolic blood pressure'], 
                           bins=[0, 90, 120, 130, 180, 300],
                           labels=["Low BP", "Normal", "Elevated", " Hypertension","H Crisis"])

#a) 
sns.catplot(df, x='Result', y='Heart rate', jitter=True)
plt.show()

#b)
sns.catplot(df, x='Gender', y='Age', jitter=False) 
plt.show()

#c)
sns.catplot(df, x='Result', y='CK-MB', hue='Gender', kind='swarm')
plt.show()

#d) WHY DOES IT LOOK LIKE THIS ???
sns.catplot(df, x='Result', y='Troponin', hue='Gender', kind='box')
plt.show()

#e)
sns.catplot(df, x='grouped_age', y='Troponin', kind='boxen')
plt.show()

import matplotlib.pyplot as plt 
#f)
sns.catplot(df, x='Age', y='Result', hue='Gender', kind='violin', inner='stick', split=True, bw =.5)
plt.show()

#g) GRAPHS R MERGING TGT, NOT SHOWING
g = sns.catplot(df, x='Age', y='Result', kind='violin', inner=None)
sns.swarmplot(df,x='Age', y='Result', size=3, ax=g.ax, color='orange)
plt.show()

#h)

#i)

#j) in each yes and each no catplot kind count 


#6.3.Visualizing bivariate distributions 
# a) Heatmap adjusted bin width?
sns.displot(df, x="Age", y="Heart rate", cbar=True, binwidth = (3, 3) )
plt.show()

#b) kde
sns.displot(df, x="Age", y='Systolic blood pressure', kind='kde', level=10, thresh=0.1)
plt.show()

#c) 
sns.displot(df, x="Age", y='Systolic blood pressure', kind='kde', col='Gender')
plt.show()



           
