class BedrockService:
      ...
      def __init__(self):
            pass
      
      def upload_document(file):
            s3_entrypoint = S3FilesEntrypoint() # ERROR: can't change the bucket because of the global coupling
