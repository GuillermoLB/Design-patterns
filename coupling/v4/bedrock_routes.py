

@router.post("/") # Bedrock upload document
async def upload_document(
    document: UploadFile = File(...),
):
    """
    Uploads a document to S3 and returns the response.
    """
    # Upload the file to S3
    s3_entrypoint = S3FilesEntrypoint(region_sqs=os.getenv("REGION_SQS"), calls_bucket=os.getenv("CALLS_BUCKET"), env=os.getenv("ENV"), os.getenv("MALWARE_BUCKET"))
    bedrock = BedrockService(s3_entrypoint=s3_entrypoint)
    response = bedrock.upload_document(document)
    return response