# InsightOps

InsightOps is a production-grade support ticket risk analysis system built on a data-first RAG and MLOps backbone. Its primary goal is to identify high-risk customer support tickets from large, noisy datasets, with RAG used as an analysis and explanation layer rather than the core product.

This is not a demo ML project. It is designed to survive real data, real scale, and real failures.

## What It Does

InsightOps predicts and explains high-risk support tickets using historical customer support data. It is built to handle tens of thousands of messy, duplicated, and partially structured tickets without corrupting pipeline state or retrieval quality.

## Core Idea

Most support ticket ML systems fail because they rely on fragile preprocessing and one-off scripts. Most RAG systems fail because they ignore data quality entirely.

InsightOps treats ticket analysis as a data engineering problem first, ML second, and LLMs last.

The focus is on:
- deterministic ticket ingestion
- reproducible NLP features and embeddings
- traceable predictions and retrieval
- restart-safe pipelines

## Architecture Overview

- **Ingestion Layer**
  - Ingests raw support tickets at scale
  - Enforces schemas and normalization
  - Handles nulls and malformed records explicitly

- **Deduplication Engine**
  - Prevents duplicate tickets and duplicate embeddings
  - Enforces one ticket to one feature and embedding set
  - Stops silent dataset inflation

- **Feature and Embedding Pipeline**
  - NLP feature extraction for risk prediction
  - Batch embedding generation for semantic analysis
  - Versioned features and embeddings

- **Datastores**
  - Relational DB as the source of truth
  - Vector DB for semantic retrieval and explanation
  - Strong referential integrity across tables

- **Prediction and Retrieval Layer**
  - Risk scoring of tickets
  - Metadata-aware semantic retrieval
  - Deterministic top-k behavior

- **LLM Explanation Layer**
  - Explains risk using retrieved historical tickets
  - Grounded outputs only
  - Built for observability, not hallucination

## Tech Stack

- **Backend**: Python, FastAPI  
- **Data & Pipelines**: Pandas, SQL, Celery  
- **ML**: PyTorch, NLP models, embeddings  
- **Databases**: PostgreSQL, Vector DB    
- **Async & Jobs**: Celery workers for ingestion, features, and embeddings

## Applied ML: Support Ticket Risk Analysis

**Support Ticket Risk Analysis System (Dec 2025)**  
- Built an end-to-end ML pipeline to predict high-risk support tickets  
- Trained on 20K+ historical tickets using NLP features  
- Designed for reproducibility, retraining, and auditability  
- Integrated with semantic retrieval for explainable risk assessment

## Why This Exists

Most ticket risk models stop at a probability score and cannot explain or debug failures. Most RAG systems cannot be trusted on real enterprise data.

InsightOps exists to answer:
- Why was this ticket flagged as high risk?
- What similar past tickets influenced this prediction?
- Can this pipeline be rerun without changing results?
- Can this scale without corrupting embeddings?

## Current Status

- End-to-end ticket ingestion and deduplication implemented
- Feature extraction and embedding pipelines live
- Risk prediction and retrieval functional
- Ongoing work on agentic workflows and evaluation

## Roadmap

- Agent-based triage and routing
- Model drift and embedding drift detection
- Risk calibration metrics
- Multi-tenant isolation
- Automated retraining and re-embedding

## Disclaimer

InsightOps is a support ticket risk system. RAG and LLMs are supporting components, not the product itself. If you are looking for prompt demos, this is not that.
