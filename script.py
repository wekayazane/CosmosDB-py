from azure.cosmos.aio import CosmosClient
from azure.identity.aio import DefaultAzureCredential
import asyncio

endpoint = "<cosmos-endpoint>"
credential = DefaultAzureCredential()

async def main():
    async with CosmosClient(endpoint, credential=credential) as client:
        # Get database and container clients
        database = client.get_database_client("cosmicworks-full")
        container = database.get_container_client("products")
    
        sql = "SELECT * FROM products WHERE products.price > 500"
        
        iterator = container.query_items(
            query=sql,
            max_item_count=50  # Set maximum items per page
        )
        
        async for page in iterator.by_page():
            async for product in page:
                print(f"[{product['id']}]	{product['name']}	${product['price']:.2f}")

if __name__ == "__main__":
    asyncio.run(main())