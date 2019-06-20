# boto3, an AWS SDK package                                                             # Delete an existing Table
import boto3     

# resource request service and region are set
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')               
input1=input("enter table :\t")
table = dynamodb.Table(input1)

# a function to delete a table
table.delete()                         