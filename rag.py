import faiss
import json
import numpy as np

# load metadata
with open("data/tickets_metadata.json") as f:
    metadata = json.load(f)

# load FAISS index
index = faiss.read_index("data/tickets.faiss")
assert index.ntotal == len(metadata), "Index and metadata mismatch"


def retrieve_similar(query_embedding, k=5):
    q = np.array(query_embedding, dtype="float32").reshape(1, -1)
    faiss.normalize_L2(q)

    scores, idx = index.search(q, k)
    results = [metadata[i] for i in idx[0]]

    return results, scores[0]


def explain_risk(query_embedding, k=5):
    results, _ = retrieve_similar(query_embedding, k)

    resolution_times = [r["resolution_time"] for r in results]
    risk_labels = [r["risk_label"] for r in results]

    avg_resolution = float(np.mean(resolution_times))
    high_risk_ratio = float(np.mean(risk_labels))

    explanation = (
        f"This ticket is flagged as high risk because similar historical tickets "
        f"had long resolution times (average ≈ {avg_resolution:.0f} minutes). "
        f"{int(high_risk_ratio * 100)}% of similar cases were classified as high risk."
    )

    return {
        "explanation": explanation,
        "avg_resolution_time": avg_resolution,
        "high_risk_ratio": high_risk_ratio,
        "similar_tickets": results
    }
