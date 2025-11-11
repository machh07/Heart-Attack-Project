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
    
for num in numerical_variables:
    
 sns.displot(df, x= num ,bins=20)
 sns.displot(df, x=num ,hue= "Gender") 
 sns.displot(df, x= num , hue ="Gender" , multiple="stack")
 sns.displot(df, x= num , hue ="Gender" , multiple="dodge") 
 sns.displot(df, x= num , hue = "Result" , stat= "density" , common_norm=False) 
 sns.displot(df, x= num, kind="kde", bw_adjust = 4) 
 sns.displot(df, x=num ,hue= "Gender", kind="ecdf")
            