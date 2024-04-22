import os
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

CONNECTION_STRING = os.environ['COSMOSDB']
COSMOS_CLIENT = CosmosClient.from_connection_string(conn_str=CONNECTION_STRING)
DATABASE = COSMOS_CLIENT.get_database_client("SiteVisitsDB")
CONTAINER = DATABASE.get_container_client("Visits")

@app.function_name(name="HttpTrigger2")
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    count = 0
    query = f"SELECT * FROM c WHERE c.id = '1'"
    try:
        for item in CONTAINER.query_items(query=query, enable_cross_partition_query=True):
            updated_item = item
            count = int(item['count'])
            count += 1
            updated_item['count'] = str(count)
            CONTAINER.upsert_item(item, updated_item)
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"An error occurred: {e.status_code} - {e.message}")
        count = e.message
        
    return func.HttpResponse(body=str(count), status_code=200)
    #return func.HttpResponse({"count": count}, status_code=200)