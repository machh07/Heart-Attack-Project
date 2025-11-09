#Programming in Science (420-SN1-RE)
#Presented to: Mr. Tiago Bortoletto Vaz
#Coded by: Marie-Ange Chhuon, Neshama Gozlan, Carlyn Matar

#Import modules
import pandas as pd
import seaborn as sns

#Import dataset
df = pd.read_csv("Medicaldataset.csv")

#Preliminary steps
#Initial data inspection
print(df.info())
print(df.describe())
#Handle duplicate entries
print(df.duplicated().value_counts()) #There are no duplicates in this dataset 
#Identify and manage missing values
print(df.isnull()) #There are no missing values in any of the columns in the dataset.

# Univariate non-graphical EDA
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
    print("Proportions:", df[cat].value_counts())   # ask for proportion**
    print("Mode:", df[cat].mode())
    print("Number of unique categories:", df[cat].nunique())
