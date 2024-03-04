from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Initialize the BlobServiceClient using the connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=tunestorage;AccountKey=xFYgusi2lp26nygotFYbd011vCH7w61g91VqElXq+AJ4U332JvIDW8PeSQRqSf/ZuZfcYT9f1agb+ASt09QieQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Get a reference to a container
container_name = "tune-blob"
container_client = blob_service_client.get_container_client(container_name)

# Specify local file path
local_file_path = "requirements.txt"

# Specify blob (file) name
blob_name = "req.txt"


def upload():
    # Upload the file
    with open(local_file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data)
