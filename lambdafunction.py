from twitterAPI import twitterAPI 

consumer_key = '51PkpfAxfIPUMCqcw8bf8iI'
consumer_secret = 'C27gFe3loVbWwyU9XzyEARMn2398xQ5GJQykDzxx8zlrIedHzx'
access_token_key = '2486856455-4jqktHbZYnCK6dUGbbR3KmyL7Qkopuz509CQ3na'
access_token_secret = '7URcWwdqXIjfSLoRclFY3Vf6hRZIhQbIDYe5aMjWX2ohw'

def lambda_handler(event, context):
    r = event.api.GetSearch('search/tweets', {'q':'DesafioDE'})
    for item in r:
        return(item)
