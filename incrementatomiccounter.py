                                                      # increment of an atomic counter

# boto3, an AWS SDK package
# JSON, a text format package that is language independent
# decimal, a precision Handling package
import boto3                                   
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

# updation of items into the table
response = table.update_item(                                                             
    Key={
        'year': year,
        'title': title
    },
    UpdateExpression="set info.rating = info.rating + :val",
    ExpressionAttributeValues={
        ':val': decimal.Decimal(1)
    },
    ReturnValues="UPDATED_NEW"
)

print("UpdateItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))