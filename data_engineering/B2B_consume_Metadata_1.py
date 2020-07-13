import os
import time

import openpyxl
import pandas as pd
import numpy as np

md_file = '../B2B/OOB_Test-Cases_L - Copy.xlsx'
md_df = pd.read_excel(md_file, header=0, index_col=False)


# For filling values with previous values
for col in range(len(md_df.columns)):
    for row in range(len(md_df.index)):
        if row > 0:
            if str(md_df.iat[row, col]).lower() == 'nan' or str(md_df.iat[row, col]).upper() == 'NAN' or md_df.iat[row, col] == "0" or md_df.iat[row, col] == 'NaN' or \
                    md_df.iat[row, col] == ' ':
                md_df.iat[row, col] = md_df.iat[row - 1, col]

        if len(str(md_df.iat[row, col])) == 3 and str(md_df.iat[row, col]).lower() == 'nan':
            md_df.iat[row, col] = 0
        if len(str(md_df.iat[row, col])) == 1 and str(md_df.iat[row, col]).lower() == ' ':
            md_df.iat[row, col] = 0


md_df.fillna(0, inplace=True)

md_df['Test Case id']=md_df['Test Case id'].astype(str)+'_'+md_df['Step Name']
md_df = md_df.drop('Step Name', axis=1)

md_df.to_csv('../B2B/test.csv', index=False)
df = pd.read_csv('../B2B/test.csv', dtype=object)
df = df.drop('Test Case id', axis=1)
print(df)


# for 'Severity', 'Priority','Functionality Module' features
def removeSpace(descript_feature_df):
    for x in range(0, len(descript_feature_df.columns)):
        for index in range(x, len(descript_feature_df)):
            descript_feature_df.iat[index, x] = descript_feature_df.iat[index, x].strip()
            print(" row value : "+descript_feature_df.iat[index, x])
    return descript_feature_df

removeSpace(df)
df = df.replace(r'[-()=<%]', '', regex=True)



Number_of_words= pd.DataFrame()
# 'Test Case Description' into features
def prepossessing(description_df):
    for index in range(0,len(description_df)):
        for row in range(0,  len(description_df.columns)):
            description_df.iat[index, row] = description_df.iat[index, row].replace(" ", ",")
            description_df.iat[index, row] = description_df.iat[index, row].replace(".", ",")
            description_df.iat[index, row] = description_df.iat[index, row].replace(",,", ",")
            description_df.iat[index, row] = description_df.iat[index, row].replace("0,0", "0")
            description_df.iat[index, row] = description_df.iat[index, row].strip()
    return description_df



prepossessing(df)

df.to_csv('../B2B/features.csv', index=False)

pd.get_dummies(df).to_csv('../B2B/all_Features1.csv', index=False)

finaldf= pd.DataFrame()
listf = []
for column in df:
    # print(df[column].name)
    df[column]= df[column].str.get_dummies(sep=',').add_prefix(df[column].name+'_').to_csv('../B2B/all_Features'+df[column].name+'_A.csv', index=False)
    dfname= df[column].name+'_df'
    time.sleep(1)
    dfname= pd.read_csv('../B2B/all_Features'+df[column].name+'_A.csv', header=0, index_col=False)
    listf.append(dfname)

    finaldf = pd.concat(listf,axis=1)
    os.remove('../B2B/all_Features'+df[column].name+'_A.csv')


finaldf.to_csv('../B2B/fnl.csv', index=False)


# Final Feature file creation
pd.concat([md_df, finaldf], axis=1).to_csv('../B2B/All_FeaturesF.csv', index=False)
