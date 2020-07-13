import pandas as pd

md_file = 'datasource/Metadata Library.xlsx'
md_df = pd.read_excel(md_file, header=0, index_col=False, keep_default_na=True)
description_df = md_df[['Test Case Description']]
descript_feature_df = md_df[['Severity', 'Priority', 'Functionality Module']]


# for 'Severity', 'Priority','Functionality Module' features
def removeSpace(descript_feature_df):
    for x in range(0, len(descript_feature_df.columns)):
        for index in range(x, len(descript_feature_df)):
            descript_feature_df.iat[index, x] = descript_feature_df.iat[index, x].strip()
    return descript_feature_df

removeSpace(descript_feature_df)
pd.get_dummies(descript_feature_df).to_csv('datasource/SPF_Features.csv', index=False)
#print(descript_feature_df)

Number_of_words= pd.DataFrame()
# 'Test Case Description' into features
def prepossessing(description_df):
    for index in range(0, len(description_df)):
        description_df.iat[index, 0] = description_df.iat[index, 0].replace(" ", ",")
        description_df.iat[index, 0] = description_df.iat[index, 0].replace(".", ",")
        description_df.iat[index, 0] = description_df.iat[index, 0].replace(",,", ",")
        description_df.iat[index, 0] = description_df.iat[index, 0].strip()
        #print("index: ", index, " Number of words: ",len(description_df.iat[index, 0].split(",")))
        Number_of_words.at[index, 'Number of words in Test Case Description'] = len(description_df.iat[index, 0].split(","))
    return description_df

prepossessing(description_df)
description_df['Test Case Description'].str.get_dummies(sep=',').add_prefix('Test Case Description_').to_csv(
    'datasource/tsDescription_Features.csv', index=False)

# For validating Description after splitting
Number_of_words['Number of words in Test Case Description'] = Number_of_words.astype(int)
# print(Number_of_words)


# Final Feature file creation
pd.concat([md_df, Number_of_words['Number of words in Test Case Description'], pd.get_dummies(descript_feature_df),
           description_df['Test Case Description'].str.get_dummies(sep=',').add_prefix('Test Case Description_')],
          axis=1).to_csv('datasource/All_Features.csv', index=False)


# NLP FILE FOR INDIVIDUL FEATURES
description_df = md_df[['Test Case Description', 'Test Case ID']]
prepossessing(description_df)
b = pd.DataFrame(description_df['Test Case Description'].str.split(',').tolist(), index=description_df['Test Case ID']).stack()
b = b.reset_index()[[0, 'Test Case ID']] # var1 variable is currently labeled 0
b.columns = ['Test Case Description', 'Test Case ID'] # renaming var1

b.to_csv('datasource/Test Case Description_nlp.csv', index=False)

#'Severity', 'Priority', 'Functionality Module'
description_df = md_df[['Severity', 'Test Case ID']]
b = pd.DataFrame(description_df['Severity'].str.split(',').tolist(), index=description_df['Test Case ID']).stack()
b = b.reset_index()[[0, 'Test Case ID']] # var1 variable is currently labeled 0
b.columns = ['Severity', 'Test Case ID'] # renaming var1

b.to_csv('datasource/Severity_nlp.csv', index=False)

#'Severity', 'Priority', 'Functionality Module'
description_df = md_df[['Priority', 'Test Case ID']]
b = pd.DataFrame(description_df['Priority'].str.split(',').tolist(), index=description_df['Test Case ID']).stack()
b = b.reset_index()[[0, 'Test Case ID']] # var1 variable is currently labeled 0
b.columns = ['Priority', 'Test Case ID'] # renaming var1

b.to_csv('datasource/Priority_nlp.csv', index=False)

#'Severity', 'Priority', 'Functionality Module'
description_df = md_df[['Functionality Module', 'Test Case ID']]
b = pd.DataFrame(description_df['Functionality Module'].str.split(',').tolist(), index=description_df['Test Case ID']).stack()
b = b.reset_index()[[0, 'Test Case ID']] # var1 variable is currently labeled 0
b.columns = ['Functionality Module', 'Test Case ID'] # renaming var1

b.to_csv('datasource/Functionality Module_nlp.csv', index=False)
# pd.concat([b['Test Case ID'],b['Functionality Module'].str.get_dummies().add_prefix('Functionality_')], axis=1)\
#     .to_csv('datasource/Functionality Module_getdummies_f.csv', index=False)
#pd.get_dummies(b['Functionality Module']).to_csv('datasource/Functionality Module_getdummies_f.csv', index=False)

