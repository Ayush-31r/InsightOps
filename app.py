import streamlit as st
import numpy as np
import joblib
import json
import faiss
from dotenv import load_dotenv
load_dotenv()

from rag import explain_risk
from embed import embed_text

# ---------- load artifacts  ----------
lr_model = joblib.load("models/risk_lr_model.joblib")
THRESHOLD = joblib.load("models/risk_threshold.joblib")

index = faiss.read_index("data/tickets.faiss")

with open("data/tickets_metadata.json") as f:
    metadata = json.load(f)

# ---------- UI ----------
st.set_page_config(page_title="Ticket Risk Analyzer", layout="centered")

st.title("Support Ticket Risk Analyzer")
st.write("Enter a new support ticket to estimate operational risk.")

ticket_text = st.text_area("Ticket content", height=200)

if st.button("Analyze"):
    if not ticket_text.strip():
        st.warning("Please enter ticket content.")
    else:
        # 1. Generate embedding
        embedding = np.array(embed_text(ticket_text), dtype="float32")

        # 2. Predict risk
        risk_score = lr_model.predict_proba(embedding.reshape(1, -1))[:, 1][0]
        risk_label = int(risk_score >= THRESHOLD)

        st.subheader("Risk Prediction")
        st.metric("Risk score", f"{risk_score:.3f}")
        st.write("High risk" if risk_label else "Low risk")

        # 3. RAG explanation (only if high risk)
        if risk_label == 1:
            rag_output = explain_risk(embedding, k=5)


            st.subheader("Why this ticket is risky")
            st.write(rag_output["explanation"])

            st.subheader("Similar historical tickets")
            for t in rag_output["similar_tickets"]:
                st.markdown(
                    f"- **Category:** {t['category']} | "
                    f"**Resolution time:** {t['resolution_time']} min"
                )
