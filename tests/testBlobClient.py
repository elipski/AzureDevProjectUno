import os
import traceback
from config import Config
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    #Test getting Application Configuration 
    print("Azure connecition string: " + os.environ.get('AZURE_APP_CONFIG_CONNECTION_STRING'))
    APP_CONFIG_CONNECTION_STRING = os.environ.get('AZURE_APP_CONFIG_CONNECTION_STRING')
    app_config_client = AzureAppConfigurationClient.from_connection_string(APP_CONFIG_CONNECTION_STRING)
    retrieved_config_setting = app_config_client.get_configuration_setting(key='SQL_USER_NAME')
    print("Retrieved Setting: " + retrieved_config_setting.value )

    upload_file_path = r"./example_images/blob-solution.png"
    # Write text to the file
    #print(upload_file_path)
    #file = open(upload_file_path, "r")
    #print(file)
    
    blob_account = 'finalprojectsa'
    blob_container = 'images'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')       #From environment variables
    CONNECTION_STR = os.getenv('STORAGE_CONNECTION')            #From enviornment variables
    STORAGE_URL = os.getenv('BLOB_STORAGE_URL')                 #From enviornment variables
    print(CONNECTION_STR)
    print(BLOB_STORAGE_KEY)
    
    #Retrieve a Blob
    blob_service = BlobServiceClient(account_url=STORAGE_URL, credential=BLOB_STORAGE_KEY)
    contiainer_client = blob_service.get_container_client(blob_container)
    blob_list = contiainer_client.list_blobs()

    for blob in blob_list:
     print("\t" + blob.name)
     #Delete Blobs in images container
     contiainer_client.delete_blob(blob.name)

    #Store a blob in images container
    blob_client = BlobClient(account_url=STORAGE_URL,
                  container_name=blob_container,
                  blob_name='blog-solution.png',
                  credential=BLOB_STORAGE_KEY)
    with open(upload_file_path, "rb") as data: 
        blob_client.upload_blob(data, blob_type="BlockBlob", overwrite=True)
    blob_client.delete_blob

except Exception as ex:
    print('Exception:')
    print(ex)
    print(traceback.format_exc())
