import boto3
from pydantic_settings import SettingsConfigDict
from pydantic_settings_aws import SecretsManagerBaseSettings


client = boto3.client("secretsmanager", region_name="eu-central-1")


class AWSSecretsSettings(SecretsManagerBaseSettings):
    model_config = SettingsConfigDict(
        secrets_name="/zappapi/AGENT_ID",
        secrets_client=client
    )

    AGENT_ID: str


print(AWSSecretsSettings().model_dump())