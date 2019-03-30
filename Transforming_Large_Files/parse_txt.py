import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Optionally separate the dataframes from the raw datasource.
# raw_0 = pd.read_csv('/Users/you/Downloads/sample.txt', names=["ADDRESS1", "ADDRESS2", "CITY", "STATE"], usecols=[0,1], encoding='utf-8', sep='\t', header=0, iterator=True, chunksize=100)
raw = pd.read_csv('/Users/you/Repos/Scripts/Source_files/sample.txt', names=["ADDRESS1", "ADDRESS2", "CITY", "STATE"], encoding='utf-8', sep='\t', header=0, iterator=True, chunksize=100)
addy_2 = []

df_empty = pd.DataFrame()
for chunk in raw:
    for index, row in chunk.iterrows():
        addy_2.append(str(row["ADDRESS2"]).decode('unicode_escape').encode('ascii', 'ignore'))
        # print(str(row["ADDRESS2"]).decode('unicode_escape').encode('ascii', 'ignore'))
        # print(row["ADDRESS2"])
        # print(index)
    # print(chunk)
    df_empty = pd.concat([df_empty,chunk])

address_2 = pd.Series(addy_2)
col_one = df_empty["ADDRESS1"]
df = df_empty.drop(columns=['ADDRESS1','ADDRESS2'])
comb = pd.concat([address_2, df_empty], axis=1, join_axes=[address_2.index])
result = pd.concat([col_one, comb], axis=1, join_axes=[comb.index])
result.to_csv(r'/Users/you/Desktop/small_file.csv', encoding='utf-8')
