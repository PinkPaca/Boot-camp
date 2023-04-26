import pandas as pd
import seaborn as sns

iris_df=sns.load_dataset('iris')
print(iris_df.columns)
just_the_species=iris_df['species']
sepal_and_petal_info=iris_df[['sepal_length','sepal_width','petal_length','petal_width']]

small_sepal_length=iris_df[iris_df['sepal_length']<4.2]