# Import required classes from the Azure Cosmos DB SDK
# CosmosClient: Main class to interact with Azure Cosmos DB
# PartitionKey: Class to define the partition key for a container
from azure.cosmos import CosmosClient, PartitionKey

# Initialize the Cosmos DB client with connection details
# url: The endpoint URL for your Cosmos DB instance (using local emulator here)
# credential: The primary key for authentication (using emulator's default key)
client = CosmosClient(
    url="https://localhost:8081",  # Local emulator endpoint
    credential=(  # Default emulator key (this is a fixed value for local development)
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGG"
        "yPMbIZnqyMsEcaGQy67XIw/Jw=="
    ),
)

# Create a database if it doesn't exist
# id: The unique name for the database
# offer_throughput: The provisioned RU/s (Request Units per second) for the database
# 400 is the minimum RU/s for manual provisioning
database = client.create_database_if_not_exists(
    id="cosmicworks",  # Database name
    offer_throughput=400,  # Minimum throughput allocation
)

# Create a container (similar to a table in relational databases) if it doesn't exist
# id: The unique name for the container
# partition_key: Defines how data is distributed across partitions
# path: Specifies which property in your documents will be used as the partition key
container = database.create_container_if_not_exists(
    id="products",  # Container name
    partition_key=PartitionKey(
        path="/id",  # Using 'id' field as partition key
    ),
)

# Define a sample item (document) to insert
# Must include 'id' field as it's our partition key
# Additional fields (like 'name') can be added as needed
item = {"id": "68719518371", "name": "Kiama classic surfboard"}

# Upsert the item into the container
# Upsert = Update + Insert (creates if not exists, updates if exists)
# This operation is atomic and will replace the entire item if it exists
container.upsert_item(item)

# Print the upserted item to confirm the operation
print("Item upserted:", item)
