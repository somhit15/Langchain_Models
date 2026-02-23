from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embedder = NVIDIAEmbeddings(
  model="nvidia/llama-3.2-nemoretriever-300m-embed-v2"
  )

doc = [
        "Komchatka's weather is cold, with long, severe winters.",
        "Italy is famous for pasta, pizza, gelato, and espresso.",
        "I can't recall personal names, only provide information.",
        "Life's purpose varies, often seen as personal fulfillment.",
        "Enjoying life's moments is indeed a wonderful approach.",
    ]

q_embeddings = embedder.embed_query("What’s my name? I bet you don’t remember…")

d_embeddings = embedder.embed_documents(doc)

def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_a = np.linalg.norm(vec1)
    norm_b = np.linalg.norm(vec2)
    return dot_product / (norm_a * norm_b)

for i, doc_emb in enumerate(d_embeddings):
    similarity = cosine_similarity(q_embeddings, doc_emb)
    print(f"Similarity with doc {i}: {similarity:.4f}")
