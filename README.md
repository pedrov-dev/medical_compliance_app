# Medical Compliance RAG Application

This repository contains a Python-based web application for a Medical Compliance Retrieval-Augmented Generation (RAG) system. It integrates OpenAI's API for natural language processing and Pinecone for vector-based document retrieval. The application is composed of a FastAPI backend and a simple HTML/JS frontend.

## Key Features

- **FastAPI Backend**: Handles chatbot interactions, context management, and integrates with OpenAI and Pinecone.
- **Frontend UI**: A minimal UI built using HTML, CSS, and JavaScript to interact with the chatbot.
- **Chat Memory**: Maintains conversation history in-memory (expandable to persistent storage).
- **Dockerized**: Dockerfiles for backend and frontend are provided. Use Docker Compose to run the entire application.
- **CI/CD**: GitHub Actions workflow for automated testing, linting, and Docker builds.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- API keys for OpenAI and Pinecone.

### Running Locally with Docker Compose

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/medical-compliance-app.git
   cd medical-compliance-app
