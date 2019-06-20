                 # Creation of Table in DynamoDB

 # a SDK package for aws in python
import boto3 

# user should go on with below line of code if they have'nt configured through AWS previously (Note)
# client = boto3.client('dynamodb',aws_access_key_id='yyyy', aws_secret_access_key='xxxx', region_name='***')                                                  

# aws service resource and region are set.

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 
name=input("Enter name of the table :\t")

# Creation of table

table = dynamodb.create_table(                                 
    TableName=movies,
    KeySchema=[
        {
            
         # here Attribute 'year' is a partition key and it is of type hash which is derived using hash function
                                                                
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition key                 
                                                                
        },
        {
            
         # here Attribute 'title' is a sort key and it is of type Range
         
            'AttributeName': 'title',                         
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[                                      
        {
            
        
             # N represents the datatype of attribute 'year' should be a number
        
            'AttributeName': 'year',                          
            'AttributeType': 'N'
        },
        {
             # S represents the datatype of attribute 'title' should be a string
        
            'AttributeName': 'title',                        
            'AttributeType': 'S'
        },

    ],
        # throughput parameters
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,                             
        'WriteCapacityUnits': 10
    }
    
)

print("Table status:", table.table_status)