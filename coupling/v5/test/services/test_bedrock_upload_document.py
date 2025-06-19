def test_bedrock_upload_document_success():
    # Create a test document object
    test_document = {
        "content": io.BytesIO(b"test content"),
        "filename": "test_document.pdf"
    }
    
    # Setup your service
    s3_entrypoint = S3FilesEntrypoint(
        region_sqs="eu-central-1",
        bucket_s3="test-bucket",
        env="test",
        bucket_malware_s3="test-bucket-malware"
    )
    
    bedrock = BedrockService(s3_entrypoint)
    
    # Call the method and get the response
    upload_response = bedrock.upload_document(
        document=test_document
    )
    
    # Assert on the response properties
    assert upload_response is not None
    assert 'ResponseMetadata' in upload_response
    assert upload_response['ResponseMetadata']['HTTPStatusCode'] == 200
    