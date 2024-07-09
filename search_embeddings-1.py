import openai
from qdrant_client import QdrantClient

openai.api_key = "<openai-api-key>"

client = QdrantClient(
    url="<qdrant-url",
    api_key="qdrant-api-key"
)

embedding_model = "text-embedding-3-small"
collection_name = "example_collection"

# get the query embedding you want to search
query_embedding = openai.embeddings.create(
    input=["How would i search for a vector?"],
    model=embedding_model
).data[0].embedding

# performs similarity search between the query embedding and each of the stored embeddings
search_results = client.search(
    collection_name=collection_name,
    query_vector=query_embedding,
)

print("Search Results:")
for result in search_results:
    print(f"id: {result.id}, Score: {result.score}, Payload: {result.payload}")
# id = created when embedding the texts
# score = degree of similarity (-1 (less similarity) to 1 (perfect similarity))
# payload = data being carried, in this case... the original text
