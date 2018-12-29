import boto3

dynamodb = boto3.resource('dynamodb')

def persist_races(races, table = 'races'):
    with dynamodb.Table(table).batch_writer() as batch:
        for race in races:
            batch.put_item(
                    Item={
                        'date': race['Date'],
                        'event': race['Event'],
                        'venue': race['Venue'],
                        'time': race['Time'],
                        'contact': race['Contact'] 
                        }
                    )
