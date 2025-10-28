# Import Python's asyncio library for asynchronous programming
import asyncio

# Import async versions of Azure Cosmos DB client and Identity libraries
from azure.cosmos.aio import CosmosClient  # For async DB operations
from azure.identity.aio import DefaultAzureCredential  # For async authentication

# Configuration for Cosmos DB connection
# Replace <cosmos-endpoint> with your actual Cosmos DB endpoint URL
endpoint = "<cosmos-endpoint>"
# DefaultAzureCredential automatically handles available authentication methods
# Tries in order: managed identity, environment variables, and other methods
credential = DefaultAzureCredential()


async def main():
    """Main async function to demonstrate Cosmos DB async operations

    This function shows how to:
    1. Connect to Cosmos DB asynchronously
    2. Query expensive products (price > 500)
    3. Use async pagination to efficiently process results

    The async context manager (async with) ensures proper cleanup of resources
    even if an error occurs during execution.
    """
    # Create an async Cosmos DB client using a context manager
    # This ensures the client is properly closed when we're done
    async with CosmosClient(endpoint, credential=credential) as client:
        # Get references to database and container
        # Note: These operations don't make network calls until used
        database = client.get_database_client("cosmicworks-full")
        container = database.get_container_client("products")

        # Define query to find expensive products (price > 500)
        # Using parameterized queries is recommended for production code
        sql = "SELECT * FROM products WHERE products.price > 500"

        # Create an async query iterator
        # max_item_count=50 sets the page size for efficient data retrieval
        iterator = container.query_items(
            query=sql,
            max_item_count=50,  # Set maximum items per page for memory efficiency
        )

        # Process results page by page asynchronously
        # This approach is memory-efficient as it only loads one page at a time
        async for page in iterator.by_page():
            # Process each product in the current page
            async for product in page:
                # Print product details in a formatted string
                # [id] name $price.00
                print(f"[{product['id']}]	{product['name']}	${product['price']:.2f}")


# Standard Python idiom for running async main function
# asyncio.run() creates an event loop and runs the async function to completion
if __name__ == "__main__":
    asyncio.run(main())
