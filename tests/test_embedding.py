from rag.embeddings import get_embedding_model
embedding_model = get_embedding_model()
vector= embedding_model.embed_query("What is the purpose of this document?")

print(f"Vector length: {len(vector)}")
print(vector[:10])  # Print the first 10 elements of the vector