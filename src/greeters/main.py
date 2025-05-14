import os
from typing import List

from sentence_transformers import SentenceTransformer, util

path = os.getcwd()

GUIDES_DIR = os.path.join(path, "guides")
TOURISTS_DIR = os.path.join(path, "tourists")

model = SentenceTransformer("all-mpnet-base-v2", device="cpu")

guide_texts: List[str] = []
guide_ids: List[str] = []
for fname in os.listdir(GUIDES_DIR):
    if not fname.endswith(".txt"):
        continue
    guide_id = os.path.splitext(fname)[0]
    with open(os.path.join(GUIDES_DIR, fname), "r", encoding="utf-8") as f:
        guide_texts.append(f.read())
    guide_ids.append(guide_id)

guide_embeddings = model.encode(
    guide_texts, convert_to_tensor=True, normalize_embeddings=True
)

for fname in os.listdir(TOURISTS_DIR):
    if not fname.endswith(".txt"):
        continue
    tourist_id = os.path.splitext(fname)[0]
    with open(os.path.join(TOURISTS_DIR, fname), "r", encoding="utf-8") as f:
        tourist_text = f.read()
    tourist_embedding = model.encode(
        [tourist_text], convert_to_tensor=True, normalize_embeddings=True
    )

    hits = util.semantic_search(
        query_embeddings=tourist_embedding, corpus_embeddings=guide_embeddings, top_k=5
    )[0]

    print(f"\nTop 5 guide matches for tourist '{tourist_id}':")
    for rank, hit in enumerate(hits, start=1):
        guide_idx = int(hit["corpus_id"])
        score = hit["score"]
        print(f"  {rank}. {guide_ids[guide_idx]} (score: {score:.4f})")
