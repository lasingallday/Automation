import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

raw = pd.read_csv('/Users/jif/Repos/Automation/Files/annual-enterprise-survey-2018-financial-year-provisional-csv.csv', encoding='utf-8', header=0, iterator=True, chunksize=10000)

# Print list of column names
chunk_1 = raw.get_chunk(10)
print(list(chunk_1.columns.values))

# addy_2 = []
df_empty = pd.DataFrame()
for chunk in raw:
    df_empty = pd.concat([df_empty,chunk])


df = df_empty.drop(columns=['Value','Industry_code_ANZSIC06'])
df.to_csv(r'/Users/jif/Repos/Automation/Files/annual_enterprise_survey_2018_transformed.csv', encoding='utf-8', index=False)
