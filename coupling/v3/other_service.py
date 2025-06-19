
class OtherService:
    '''Service that wants to use bedrock document uploading with a different bucket'''
    ...
    def __init__(self):
        pass
      
    def use_bedrock(bucket_name):
        BedrockService() # ERROR: can't change the bucket