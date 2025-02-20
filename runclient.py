from azure.ai.ml.entities import AzureOpenAIConnection, ApiKeyConfiguration
from azure.ai.ml.entities import UsernamePasswordConfiguration

name = "XXXXXXXXX"

target = "https://XXXXXXXXX.cognitiveservices.azure.com/"

resource_id= "Azure-resource-id"

# Microsoft Entra ID
credentials = None
# Uncomment the following if you need to use API key instead
# api_key= "my-key"
# credentials = ApiKeyConfiguration(key=api_key)

wps_connection = AzureOpenAIConnection(
    name=name,
    azure_endpoint=target,
    credentials=credentials,
    resource_id = resource_id,
    is_shared=False
)
ml_client.connections.create_or_update(wps_connection)