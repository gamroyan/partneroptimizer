import openai

from qdrant_client import QdrantClient, models
from qdrant_client.models import PointStruct

openai.api_key = "<openai-api-key>"

client = QdrantClient(
    url="<qdrant-url>",
    api_key="<qdrant-api-key>"
)

texts = [
    "Qdrant is the best vector search engine!",
    "Loved by Enterprises and everyone.",
]

# Embedding a document
embedding_model = "text-embedding-3-small"

result = openai.embeddings.create(input=texts, model=embedding_model)

# Converting the model outputs to Qdrant points
points = [
    PointStruct(
        id=idx,
        vector=data.embedding,
        payload={"text": text},
    )
    for idx, (data, text) in enumerate(zip(result.data, texts))
]

collection_name = "example_collection"

client.create_collection(
    collection_name,
    vectors_config=models.VectorParams(
        size=1536, 
        distance=models.Distance.COSINE),
)
client.upsert(collection_name, points)

print("Embeddings stored successfully in Qdrant")
