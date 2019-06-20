                                                        # conditional update

# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3  

# this looks after validation error (throws a statement if the entity already exists) 
from botocore.exceptions import ClientError     

import json                                        
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

# resource request service and region are set
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')                   

table = dynamodb.Table('movies')

title = "The Big New Movie"
year = 2015

# Conditional update (will fail)
print("Attempting conditional update...")

# try block
try:
    response = table.update_item(
        Key={                                                                     
            'year': year,
            'title': title
        },
        UpdateExpression="remove info.actors[0]",
        ConditionExpression="size(info.actors) > :num",
        ExpressionAttributeValues={
            ':num': 3
        },
        ReturnValues="UPDATED_NEW"
    )
    
# exception handling
except ClientError as e:                                                         
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print("UpdateItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))