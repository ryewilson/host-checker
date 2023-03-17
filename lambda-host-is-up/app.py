from boto3 import resource
from botocore.exceptions import ClientError
from json import dumps
import os
from datetime import datetime, timezone

tableName = os.environ['host_table']
dynamo = resource('dynamodb').Table(tableName)

def lambda_handler(event, context):
    if event["httpMethod"] == "GET":
        return {
            'statusCode': 200,
            'body': dumps('Got a GET')
        }
    elif event["httpMethod"] == "PUT":

        now = datetime.now(timezone.utc)
        host_id = event["queryStringParameters"]['host']
        

        # query to see if host exists - if so, only update
        try:
            response = dynamo.get_item(Key={'host_id': host_id})
            
            if 'Item' in response:
                update_existing_row(host_id, now)
            else:
                 insert_new_row(host_id, now)
                 
        except ClientError as err:
            print(f"Could not query host {host_id} in table {dynamo.name}. Heres why: {err.response['Error']['Code']}: {err.response['Error']['Message']}")
            raise
        
        return {
            'statusCode': 200,
            'body' : dumps(f'Inserted {host_id}')
        }
        
def update_existing_row(host, now):
    response = dynamo.update_item(
        Key={'host_id': host},
        UpdateExpression="set last_updated = :s",
        ExpressionAttributeValues={
            ':s': now.isoformat() },
        ReturnValues="UPDATED_NEW")
    
def insert_new_row(host_id, now):
    new_host = { 
        'host_id': host_id, 
        'last_updated': now.isoformat(),
    }
    dynamo.put_item(Item=new_host)

