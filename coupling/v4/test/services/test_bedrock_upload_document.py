def test_bedrock_upload_document_success():

    test_document = {
        "content": io.BytesIO(b"test content"),
        "filename": "test_document.pdf"
    }

    s3_entrypoint = S3FilesEntrypoint(
        region_sqs="eu-central-1",
        bucket_s3="test-bucket", # Independent bucket
        env="test",
        bucket_malware_s3="test-bucket-malware"
    )
    
    bedrock = BedrockService(s3_entrypoint)
    
    upload_response = bedrock.upload_document(
        document=test_document
    )
    
    assert upload_response is not None
    assert 'ResponseMetadata' in upload_response
    assert upload_response['ResponseMetadata']['HTTPStatusCode'] == 200
    