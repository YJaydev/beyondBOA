import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder


md_file = 'Metadata Library.xlsx'
md_df = pd.read_excel(md_file, header=0, index_col=False, keep_default_na=True )




description_df = md_df[['Test Case Description', 'Test Case ID']]

#print(description_df)

# cleaned = description_df["Test Case Description"].str.split(",", n = 1, expand = True)
# print(cleaned)



#col = list(description_df)
#col_join = " ".join(col)
#col_split = col_join.split(" ")

#print(md_df[['Test Case Description']])
#print(description_df.head())
#print(description_df.values.tolist())
def prepossessing(description_df):
  for index in range(0,len(description_df)):
      #print(description_df.iat[index,0])
      description_df.iat[index,0] = description_df.iat[index,0].replace(" ",",")
      description_df.iat[index, 0] = description_df.iat[index, 0].replace(".", ",")
      description_df.iat[index, 0] = description_df.iat[index, 0].replace(",,", ",")
      #print(description_df.iat[index,0])
      #print(index)
  return description_df
prepossessing(description_df)


#description_df.set_index("Test Case ID", inplace = True)

#description_df['Test Case Description'].str.split(expand=True).to_csv('af_test_encode1.csv', index=False)

b = pd.DataFrame(description_df['Test Case Description'].str.split(',').tolist(), index=description_df['Test Case ID']).stack()
b = b.reset_index()[[0, 'Test Case ID']] # var1 variable is currently labeled 0
b.columns = ['Test Case Description', 'Test Case ID'] # renaming var1

b.to_csv('af_test_nlp1.csv', index=False)

pd.get_dummies(b).to_csv('af_test_encode1.csv', index=False)

# test_txt = 'View timesheet of employee from list or view specific employees timesheet by searching and verify if it can be approved and rejected successfully'





# cleaned = pd.DataFrame()
# def presplitting(description_df):
#   for index in range(0,len(description_df)):
#       for split_val in range(0,len(description_df.iat[index, 0].split(","))):
#           cleaned = description_df["Test Case Description"].str.split(",", n=1, expand=True).stack()
#           print("inside value: ",split_val)
#       print("out side value : ",index)
#   return cleaned
# presplitting(description_df)







#description_df.set_index("Test Case ID", inplace = True)
#cleaned = description_df["Test Case Description"].str.split(",", n = 1, expand = True).stack()

#print(cleaned)
#
# cleaned.to_csv('bf_test_encode.csv', index=False)
# pd.get_dummies(cleaned).groupby(level=0).sum().to_csv('af_test_encode1.csv', index=False)




#pd.get_dummies(description_df)
#print(description_df)
#description_df.to_csv('af_test.csv', sep='\t', index=False, encoding='utf-8')
#pd.get_dummies(description_df).to_csv('af_test.csv', sep='\t', encoding='utf-8')


# description_df.apply(LabelEncoder().fit_transform)
#description_df = OneHotEncoder().fit_transform(description_df)
# onehotencoder = OneHotEncoder(categorical_features=[0])
#
# description_df = onehotencoder.fit_transform(description_df).toarray()
#OneHotEncoder().fit_transform(df)
# print(description_df)
# description_df.to_csv('af_test_encode.csv', index=False)
# pd.get_dummies(description_df)
#
# print(description_df)
