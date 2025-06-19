class BedrockService:
      def __init__(self):
            self.region_sqs = os.getenv("REGION_SQS") # These are not the bedrock arguments
            self.bucket_s3 = os.getenv("CALLS_BUCKET")
            self.env = os.getenv("ENV")
            self.bucket_malware_s3 = f"{self.bucket_s3}-malware"
      
      def upload_document():
            s3 = S3FilesEntrypoint(region_sqs=self.region_sqs, calls_bucket=self.bucket_s3, env=self.env, bucket_malware_s3=self.bucket_malware_s) # Too many arguments
            s3.upload_files_to_s3(file, file.filename, ...)
