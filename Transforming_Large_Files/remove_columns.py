import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

raw = pd.read_csv('/Users/you/Downloads/file.csv', encoding='utf-8', header=0, iterator=True, chunksize=10000)

# Print list of column names
chunk_1 = raw.get_chunk(10)
print(list(chunk_1.columns.values))

# addy_2 = []
df_empty = pd.DataFrame()
for chunk in raw:
    df_empty = pd.concat([df_empty,chunk])


df = df_empty.drop(columns=['Application Number','Funding year '])
# Drop the index column read_csv automatically creates.
df = df.drop(columns=df.columns[0])

df.to_csv(r'/Users/you/Desktop/small_file.csv', encoding='utf-8')
