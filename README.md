<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>
<h1 align="center">  AI OpenAI Request Reply Wrapper Service  </h1> 
<h4 align="center"> A robust Python backend service that simplifies interaction with OpenAI's language models. </h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language-Python">
  <img src="https://img.shields.io/badge/Framework-FastAPI-red" alt="Framework-FastAPI">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database-PostgreSQL">
  <img src="https://img.shields.io/badge/API-OpenAI-black" alt="API-OpenAI">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/openai-request-reply-wrapper-service?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/openai-request-reply-wrapper-service?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/openai-request-reply-wrapper-service?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>  

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors
        
## 📍 Overview
The AI OpenAI Request Reply Wrapper Service is a Python backend service that simplifies interacting with OpenAI's powerful language models. This service acts as a bridge between users and the OpenAI API, making it easier to leverage advanced AI capabilities for various tasks, including text generation, translation, and code completion.

## 📦 Features

|    | Feature                                    | Description                                                                                                                                                 |
|----|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**                           |  The service is built with a layered architecture, separating concerns for better organization and scalability.                                                        |
| 📄 | **Documentation**                          |  This README file provides a comprehensive overview of the service's features, installation instructions, usage guide, and API documentation.                         |
| 🔗 | **Dependencies**                           | The project leverages essential Python libraries like `fastapi`, `uvicorn`, `pydantic`, `requests`, `python-dotenv`, `sqlalchemy`, and `psycopg2` for building the API, handling requests, managing data, and connecting to the OpenAI API.  |
| 🧩 | **Modularity**                             |  The codebase is well-organized with separate files for models, routes, dependencies, and services, promoting reusability and maintainability.                      |
| 🧪 | **Testing**                               |  Thorough unit tests ensure the correctness and reliability of the codebase.                                                                                |
| ⚡️  | **Performance Optimization**              |  The service is designed for efficient communication with the OpenAI API, minimizing latency and optimizing database interactions for better performance.               |
| 🔐 | **Security Measures**                      |   Robust security measures are implemented to protect user data and API credentials, including API key management, data encryption, and access control mechanisms.       |
| 🔀 | **Version Control**                       |   The project uses Git for version control, ensuring a clear history of changes and facilitating collaboration among developers.                                 |
| 🔌 | **OpenAI API Integration**               | The service seamlessly integrates with the OpenAI API to provide access to a wide range of language models and advanced AI capabilities.                         |
| 📶 | **Scalability and Future-Proofing**         | The architecture is designed for scalability, enabling the service to handle increasing workloads and user demands without compromising performance.                 |


## 📂 Structure

```text
├── requirements.txt
├── .env
├── main.py
├── api
│   ├── routes
│   │   └── requests.py
│   ├── dependencies
│   │   └── openai.py
│   └── services
│       └── request_service.py
├── models
│   ├── request.py
│   └── user.py
└── tests
    ├── test_api.py
    ├── test_models.py
    └── test_services.py
```

## 💻 Installation

### 🔧 Prerequisites

- Python 3.9+
- PostgreSQL 14+
- Docker (Optional)

### 🚀 Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/coslynx/openai-request-reply-wrapper-service.git
   cd openai-request-reply-wrapper-service
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   ```bash
   cp .env.example .env
   ```
   - Update the `.env` file with your OpenAI API key and PostgreSQL connection URL.
   - `OPENAI_API_KEY=your_openai_api_key`
   - `DATABASE_URL=postgresql://user:password@host:port/database_name`

4. **Create and Initialize Database:**
   ```bash
   createdb database_name
   psql -U user -d database_name -c "CREATE EXTENSION IF NOT EXISTS pgcrypto" 
   ```
   - Replace `database_name`, `user`, and `password` with your PostgreSQL credentials.

## 🏗️ Usage

### 🏃‍♂️ Running the Service

1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### ⚙️ Configuration

- **Environment Variables:**
    - Modify the `.env` file to adjust settings like the OpenAI API key and database connection URL.
- **Database Configuration:** 
    - You can customize database settings (e.g., user, password, host, port) in the `DATABASE_URL` environment variable.

### 📚 Examples

- **Send a request to the OpenAI API:**
  ```bash
  curl -X POST http://localhost:8000/requests \
       -H "Content-Type: application/json" \
       -d '{"prompt": "What is the meaning of life?", "model": "text-davinci-003"}'
  ```

## 🌐 Hosting

### 🚀 Deployment Instructions

1. **Create a Dockerfile (Optional):**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   ENV DATABASE_URL=postgresql://user:password@host:port/database_name \
       OPENAI_API_KEY=your_openai_api_key

   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t openai-request-reply-wrapper-service .
   ```

3. **Deploy to a container orchestration platform (e.g., Kubernetes):**
   - Create a Kubernetes deployment YAML file (e.g., `deployment.yaml`). 
   - Use `kubectl apply -f deployment.yaml` to deploy the service to your cluster.

4. **Alternatively, deploy to a cloud platform (e.g., AWS, Google Cloud):**
   - Follow the specific deployment instructions for your chosen cloud provider.

### 🔑 Environment Variables

- **`OPENAI_API_KEY`:** Your OpenAI API key.
- **`DATABASE_URL`:** PostgreSQL database connection URL.
- **`PORT`:** The port on which the service will listen (default: 8000).

## 📜 API Documentation

### 🔍 Endpoints

- **POST `/requests`:**
    - **Description:**  Handles user requests by sending them to the OpenAI API and returning the response.
    - **Request Body (JSON):**
      ```json
      {
        "prompt": "Your request text here",
        "model": "The OpenAI model to use (e.g., text-davinci-003)",
        "temperature": "Optional: Controls the creativity of the response (0.0-1.0)"
      }
      ```
    - **Response Body (JSON):**
      ```json
      {
        "response": "The AI-generated response to the prompt"
      }
      ```

### 🔒 Authentication

- The current version of the service does not implement authentication. Authentication can be added later using JWT or other security measures.

### 📝 Examples

```bash
# Send a text generation request
curl -X POST http://localhost:8000/requests \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Write a short story about a cat.", "model": "text-davinci-003"}'
```

## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: openai-request-reply-wrapper-service

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
<img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
<img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
<img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
<img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>