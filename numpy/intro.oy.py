import pandas as pd
from datetime import datetime
import json

time = datetime.now().isoformat()

print(event)
print('source_file_bucket: ',source_file_bucket)
print('source_file_name: ',source_file_name)
source_file_path = 's3://' + source_file_bucket + '/' + source_file_name

with open('/Users/amandeep.singh1/Desktop/testm1/xaa.csv', 'r') as f:
    with open('/Users/amandeep.singh1/Desktop/testm1/xaa_new1.csv', 'w') as w:
        for data in f:
            count = 0
            line = ""
            for each in data:
                if each in '"' and count == 0:
                    count += 1
                elif each in '"' and count == 1:
                    count -= 1
                if count == 0 and each == ',':
                    each = each.replace(',', '|')
                line = line + each
                line = line.replace('"{','{').replace('}"','}')
            w.write(line)
            print(line)


df = pd.read_csv('/Users/amandeep.singh1/Desktop/testm1/xaa_new1.csv', sep='|')

df['Lightning_Time'] = pd.to_datetime(df['Lightning_Time'], format = '%m/%d/%Y %H:%M:%S %p')
df['major'] = df['Stroke_Solution'].apply(lambda x: 0.0 if not x.startswith('{"ee":{"maj"') else json.loads(x)['ee']['maj'])
df['minor'] = df['Stroke_Solution'].apply(lambda x: 0.0 if not x.startswith('{"ee":{"maj"') else json.loads(x)['ee']['min'])
df['bearing'] = df['Stroke_Solution'].apply(lambda x: 0.0 if not x.startswith('{"ee":{"maj"')  else json.loads(x)['ee']['b'])
df['stations'] = df['Offsets'].apply(lambda x: '|'.join([i.split('=')[0] for i in x.replace('"','').strip(',').split(',')]))
df['numberstation'] = df['Offsets'].apply(lambda x: len(x.replace('"','').strip(',').split(',')) if len(x) > 4 else 0)
#df['Lightning_Time'] = df['Lightning_Time'].apply(lambda x:datetime.strptime(x ,'%m/%d/%Y %H:%M:%S %p').timestamp())
#df['Lightning_Time'] = pd.to_datetime(df['Lightning_Time']

df.to_parquet('/Users/amandeep.singh1/Desktop/testm1/test_parquet1132', compression='gzip')



