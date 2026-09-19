"""Optional learner-run real embedding probe; downloads weights on first run."""
from fastembed import TextEmbedding
from qdrant_client import QdrantClient, models

def main():
    encoder = TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2",
                            cache_dir=".cache/models")
    texts = ["Books can be returned within thirty days.", "Bicycles need inflated tyres."]
    vectors = [v.tolist() for v in encoder.embed(texts)]
    query = list(encoder.embed(["What is the deadline for returning a book?"]))[0].tolist()
    client = QdrantClient(":memory:")
    client.create_collection("semantic", vectors_config=models.VectorParams(
        size=len(query), distance=models.Distance.COSINE))
    client.upsert("semantic", points=[models.PointStruct(id=i, vector=v,
        payload={"text": text}) for i, (text, v) in enumerate(zip(texts, vectors))])
    hits = client.query_points("semantic", query=query, limit=2, with_payload=True).points
    print("dimensions:", len(query))
    for hit in hits:
        print(hit.id, round(hit.score, 4), hit.payload["text"])
    client.close()

if __name__ == "__main__":
    main()
