class BedrockService:
      def __init__(self):
            s3_entrypoint = S3FilesEntrypoint(region_sqs=os.getenv("REGION_SQS"), calls_bucket=os.getenv("CALLS_BUCKET"), env=os.getenv("ENV"), os.getenv("MALWARE_BUCKET"))

      def upload_document(document):
            s3 = s3_entrypoint(document)
            s3.upload_files_to_s3(file, file.filename, ...)
