import os
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    APP_CONFIG_CONNECTION_STRING = os.environ.get('AZURE_APP_CONFIG_CONNECTION_STRING') 
    print("App Connection String: "+ APP_CONFIG_CONNECTION_STRING )                    #TODO: Add to Web app configurations
    app_config_client = AzureAppConfigurationClient.from_connection_string(APP_CONFIG_CONNECTION_STRING)

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'                                               #TODO: Add to Web app configurations Don't know what this is used for or how it's used

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'finalprojectsa'                                       #TODO: Add to Web app configurations
    BLOB_STORAGE_KEY = app_config_client.get_configuration_setting(key='BLOB_STORAGE_KEY').value
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'                                           #TODO: Add to Web app configurations
    #STORAGE_CONNECTION = os.environ.get('STOREAGE_CONNECTION')
    STORAGE_URL = app_config_client.get_configuration_setting(key='BLOB_STORAGE_URL').value 


    #retrieved_config_setting = app_config_client.get_configuration_setting(key='TestApp:Settings:Message')
    SQL_SERVER = app_config_client.get_configuration_setting(key='SQL_SERVER').value           
    SQL_DATABASE = app_config_client.get_configuration_setting(key='SQL_DATABASE').value              
    SQL_USER_NAME = app_config_client.get_configuration_setting(key='SQL_USER_NAME').value            
    SQL_PASSWORD = app_config_client.get_configuration_setting(key='SQL_PASSWORD').value              
    
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    # For Mac and Linux
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    # For Windows
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    #CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = app_config_client.get_configuration_setting(key='CLIENT_SECRET').value
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")
       

    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    AUTHORITY = app_config_client.get_configuration_setting(key='AUTHORITY').value

    CLIENT_ID = os.environ.get('CLIENT_ID')                                                             #TODO: Add to Web app configurations

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
