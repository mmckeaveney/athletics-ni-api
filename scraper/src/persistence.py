import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def persist_races(races, table = 'athletics-ni-api-dev'):
    with dynamodb.Table(table).batch_writer() as batch:
        for race in races:
            batch.put_item(
                    Item={
                        'id': race['Event'] + race['Date'],
                        'date': race['Date'],
                        'event': race['Event'],
                        'venue': race['Venue'],
                        'time': race['Time'],
                        'contact': race['Contact'] 
                        }
                    )
