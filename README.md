# InsightOps

InsightOps is a production-grade Retrieval-Augmented Generation (RAG) and MLOps system designed to ingest, deduplicate, embed, store, and query large-scale operational and textual datasets with reliability and auditability. It is built to move beyond demo RAG systems and address real-world data engineering, ML lifecycle, and retrieval challenges.

## Core Idea

Most RAG systems fail in production because they ignore data quality, deduplication, versioning, and pipeline orchestration. InsightOps treats RAG as a data system first and an LLM interface second.

The focus is on:
- deterministic ingestion
- reproducible embeddings
- traceable retrieval
- scalable pipelines

## Architecture Overview

- **Ingestion Layer**
  - Structured and semi-structured data ingestion
  - Schema validation and normalization
  - Null handling and consistency checks

- **Deduplication Engine**
  - Content-based and key-based deduplication
  - Guarantees one-to-one mapping between raw records and embeddings
  - Prevents silent data inflation

- **Embedding Pipeline**
  - Batch embedding generation
  - Embedding version control
  - Decoupled from raw data lifecycle

- **Vector Store + Relational DB**
  - Relational DB for metadata and source-of-truth
  - Vector store for semantic retrieval
  - Referential integrity between tables

- **Retrieval Layer**
  - Top-k semantic search
  - Metadata-aware filtering
  - Deterministic query behavior

- **LLM Reasoning Layer**
  - Context grounding from retrieved chunks
  - Explanation-focused outputs
  - Designed for observability, not hallucination

## Tech Stack

- **Backend**: Python, FastAPI
- **Data & Pipelines**: Pandas, SQL, Celery
- **ML**: PyTorch, embedding models
- **Databases**: PostgreSQL, Vector DB
- **Infrastructure**: Docker, Cloud-native deployment (GCP-ready)
- **Async & Jobs**: Celery workers for ingestion and embedding

## Key Features

- End-to-end RAG pipeline built for production
- Strict separation of raw data, deduplicated data, and embeddings
- Embedding tables treated as first-class citizens
- Pipeline state control and restart safety
- Designed for large datasets, not toy examples

## Why InsightOps Exists

Most RAG tutorials work on clean, tiny datasets and collapse under real SaaS or enterprise data. InsightOps is built to answer:
- How do you stop duplicate embeddings?
- How do you re-embed safely?
- How do you trust retrieval results?
- How do you debug pipeline state?

This project is an answer to those problems.

## Current Status

- Core ingestion and deduplication pipelines implemented
- Embedding ingestion integrated
- Retrieval logic functional
- Ongoing work on agentic workflows and evaluation

## Roadmap

- Agent-based query routing
- Embedding drift detection
- Retrieval quality metrics
- Multi-tenant dataset isolation
- Automated re-embedding strategies

## Disclaimer

InsightOps is not a wrapper around an LLM API. It is a data-first system that happens to use LLMs at the final stage. If you are looking for quick demos, this is not that project.

## License

MIT
