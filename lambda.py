import json
import boto3
from datetime import datetime

time = datetime.now().isoformat()
s3 = boto3.resource('s3')

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    record = event['Records'][0]
    source_file_bucket = record['s3']['bucket']['name']
    source_file_name = record['s3']['object']['key']
    print('source_file_bucket: ', source_file_bucket)
    print('source_file_name: ', source_file_name)
    # source_file_path = 's3://' + source_file_bucket + '/' + source_file_name

    # s3.Bucket(source_file_bucket).download_file(source_file_name, 'test.csv')
    # print(download_path)
    s3_client.download_file(source_file_bucket, source_file_name, '/tmp/{}.csv'.format(time))

    with open('/tmp/{}.csv'.format(time), 'r') as f:
        with open('/tmp/correct_{}.csv'.format(time), 'w') as w:
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
                    line = line.replace('"{', '{').replace('}"', '}')
                w.write(line)

    df = pd.read_csv('/tmp/correct_{}.csv'.format(time), sep='|')
    df['Lightning_Time'] = pd.to_datetime(df['Lightning_Time'], format='%m/%d/%Y %H:%M:%S %p')
    df['major'] = df['Stroke_Solution'].apply(
        lambda x: 0.0 if not x.startswith('{"ee":{"maj"') else json.loads(x)['ee']['maj'])
    df['minor'] = df['Stroke_Solution'].apply(
        lambda x: 0.0 if not x.startswith('{"ee":{"maj"') else json.loads(x)['ee']['min'])
    df['bearing'] = df['Stroke_Solution'].apply(
        lambda x: 0.0 if not x.startswith('{"ee":{"maj"') else json.loads(x)['ee']['b'])
    df['stations'] = df['Offsets'].apply(
        lambda x: '|'.join([i.split('=')[0] for i in x.replace('"', '').strip(',').split(',')]))
    df['numberstation'] = df['Offsets'].apply(
        lambda x: len(x.replace('"', '').strip(',').split(',')) if len(x) > 4 else 0)

    df.to_parquet('/tmp/parquet_{}'', compression='
    gzip
    ')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
