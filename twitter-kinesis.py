from TwitterAPI import TwitterAPI
import boto3
import json
import twitterCreds

##twittercredentials

consumer_key = 'twitterCreds.51PkpfAxfIPUMCqcw8bf8w8iI'
consumer_secret = 'twitterCreds.C27gFe3loVbWwyU9XzyEARMn2398xQ5GJQykDzxx8zlrIedHzx'
access_token = 'twitterCreds.2486856455-4jqktHbZYnCK6dUGbbR3KmyL7Qkopuz509CQ3na'
access_token_secret = 'twitterCreds.7URcWwdqXIjfSLoRclFY3Vf6hRZIhQbIDYe5aMjWX2ohw'

api = TwitterAPI


kinesis = boto3.client('kinesis')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})

for item in r:
        kinesis.put_record(StreamName="twitter", Data=json.dumps(item), PartitionKey="filter") 

def lambda_handler(event, context):
    r = event.api.GetSearch('search/tweets', {'q':'DesafioDE'})
    for item in r:
        return(item)
