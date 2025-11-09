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

