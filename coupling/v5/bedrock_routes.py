from v2.S3Entrypoint import S3FilesEntrypoint
from v5.dependencies import BedrockDep, S3Dep


@router.post("/") # Bedrock upload document
async def upload_document(
    document: UploadFile = File(...),
    s3: S3Dep,
    bedrock: BedrockDep,
    settings: Settings
):
    """
    Uploads a document to S3 and returns the response.
    """
    # Upload the file to S3
    s3_entrypoint = S3FilesEntrypoint(s3=s3, region_sqs=settings.region_sqs, bucket=settings.calls_bucket, env=settings.env, malware_bucket=settings.malware_bucket)
    bedrock = BedrockService(s3=s3, bedrock=bedrock)
    response = bedrock.upload_documents3_entrypoint(s3_entrypoint, document)
    return 