
---

### 1. Repository Classification
*   **Classification:** API/Backend Service
*   **Reasoning:** The repository contains a `main.py` file, a `requierment.txt` file (common for Python dependencies), and the repository description explicitly states: "Local API for self-training purposes to get familiar with FastAPI. The goal of the API is to provide railway transport connections, as well as to list stations by transport line." This clearly indicates a backend API project.

### 2. Technology Stack Detection
*   **Runtime:** Python (detected from `.py` files, `requierment.txt`, and `language` in metadata).
*   **Frameworks:** FastAPI (explicitly mentioned in the description, and a key dependency for Python APIs).
*   **Backend Technologies:**
    *   **Server:** Uvicorn (standard ASGI server for FastAPI, assumed as a dependency in `requierment.txt`).
    *   **Data Handling:** Pandas (inferred due to the presence of a `Dataset` directory, highly likely for loading and processing data from files like CSV or Excel).
    *   **Database:** No explicit database (e.g., PostgreSQL, MongoDB) or ORM (e.g., SQLAlchemy, Pydantic with ORM features) is detected. Data is likely loaded from static files within the `Dataset` directory.
    *   **Authentication:** Not detected.
*   **DevOps & Tools:** No specific CI/CD, containerization (Docker), or cloud configurations detected.
*   **Testing:** No dedicated test files or testing frameworks detected.

### 3. Project Structure Analysis
```
project-root/
├── Dataset/             # Directory to store data files (e.g., CSV, Excel)
├── main.py              # Main application entry point for the FastAPI server
├── requierment.txt      # Lists Python project dependencies
└── README.md            # Project README (to be updated)
```
*   **Entry Points:** `main.py` serves as the primary entry point for the FastAPI application.
*   **Configuration Files:** `requierment.txt` for dependencies. No explicit environment configuration (`.env` or `.env.example`) detected, but environment variables might still be used for runtime settings.
*   **Source Code Organization:** Simple, with a single `main.py` file likely containing all API logic and data loading.
*   **Asset Locations:** The `Dataset/` directory is dedicated to data assets.

### 4. Feature Extraction
*   **Core Functionalities (from description and inferred from name):**
    *   **Railway Transport Line Listing:** Ability to retrieve a list of all available transport lines (e.g., Métro, RER lines in Paris).
    *   **Station Listing by Line:** Ability to query and list all stations associated with a specific transport line.
    *   **Transport Connection Queries:** (Inferred) Potentially providing routes or connections between two given stations.
    *   **Station Details Retrieval:** (Inferred) Ability to get detailed information about a specific station.
*   **API Endpoints (inferred based on typical FastAPI for this purpose):**
    *   `GET /`: Basic root endpoint (e.g., health check or welcome message).
    *   `GET /lines`: Retrieve all transport lines.
    *   `GET /lines/{line_id}/stations`: Retrieve stations for a specific line.
    *   `GET /stations/{station_id}`: Retrieve details for a specific station.
    *   (Potentially) `GET /connections`: For finding routes between stations.
*   **Configuration Options:** Likely runtime configuration for the server, such as port.
*   **Environment Variables:** No `.env.example` but common for production deployments to configure port, host, etc.
*   **Dependencies and their purposes:**
    *   `fastapi`: Web framework for building the API.
    *   `uvicorn`: ASGI server for running the FastAPI application.
    *   `pandas`: Data manipulation and analysis, likely used for loading and querying data from the `Dataset` directory.

### 5. Installation & Setup Detection
*   **Package Manager:** `pip` (standard for Python projects using `requierment.txt`).
*   **Installation Commands:** `pip install -r requierment.txt`.
*   **Build Processes:** No explicit build process for a Python API, it's run directly.
*   **Development Server Setup:** `uvicorn main:app --reload`.
*   **Environment Requirements:** Python 3.x.
*   **Database Setup Needs:** No external database setup required. Data is loaded from files.
*   **External Service Dependencies:** None detected.

---

## 📄 README.md

# 🚄 TransferLineParisApi

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/MaxiyaG/TransferLineParisApi?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/MaxiyaG/TransferLineParisApi?style=for-the-badge)](https://github.com/MaxiyaG/TransferLineParisApi/network)
[![GitHub issues](https://img.shields.io/github/issues/MaxiyaG/TransferLineParisApi?style=for-the-badge)](https://github.com/MaxiyaG/TransferLineParisApi/issues)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

**A local API built with FastAPI to explore Paris railway transport connections and stations.**

</div>

## 📖 Overview

`TransferLineParisApi` is a lightweight, local API designed for self-training purposes, providing a practical introduction to building web services with FastAPI. It simulates a data source for Paris's railway transport system, allowing users to query information about transport lines, their associated stations, and potentially discover connections between them. This project serves as an excellent foundation for understanding API development principles, data handling, and routing with Python and FastAPI.

## ✨ Features

-   **Transport Line Listing:** Retrieve a comprehensive list of all available railway transport lines (e.g., Métro, RER).
-   **Stations by Line:** Get all stations that belong to a specified transport line.
-   **Individual Station Details:** Access specific information for any given station.
-   **Connection Discovery (Future):** (Potentially) Query and find transport connections between two different stations.
-   **Self-Documenting API:** Leverages FastAPI's built-in OpenAPI/Swagger UI for easy API exploration and testing.

## 🛠️ Tech Stack

**Backend:**
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-FFC62C?style=for-the-badge&logo=uvicorn&logoColor=black)](https://www.uvicorn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

## 🚀 Quick Start

Follow these steps to get the `TransferLineParisApi` up and running on your local machine.

### Prerequisites
-   **Python 3.8+**

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/MaxiyaG/TransferLineParisApi.git
    cd TransferLineParisApi
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requierment.txt
    ```

3.  **Start development server**
    ```bash
    uvicorn main:app --reload
    ```

4.  **Open your browser**
    Visit `http://localhost:8000` to see the API root.
    Access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.
    Access the alternative API documentation (ReDoc) at `http://localhost:8000/redoc`.

## 📁 Project Structure

```
TransferLineParisApi/
├── Dataset/             # Stores raw data files (e.g., CSV, Excel) for transport lines and stations.
├── main.py              # The core FastAPI application, including routing and business logic.
├── requierment.txt      # Lists all Python package dependencies.
└── README.md            # Project documentation.
```

## ⚙️ Configuration

The API can be configured using environment variables, though none are strictly required for basic operation as defined in this project.

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `PORT`   | The port the Uvicorn server listens on. | `8000` | No       |
| `HOST`   | The host address the Uvicorn server binds to. | `127.0.0.1` | No       |

You can set these variables in your shell before running the server:
```bash
export PORT=5000
uvicorn main:app --reload --port $PORT
```

## 🔧 Development

### Available Commands

| Command                     | Description                                          |
|-----------------------------|------------------------------------------------------|
| `uvicorn main:app --reload` | Starts the development server with auto-reloading.   |
| `uvicorn main:app`          | Starts the production server (without auto-reloading). |

### Development Workflow

1.  Ensure prerequisites are met and dependencies are installed.
2.  Make changes to `main.py` or data in `Dataset/`.
3.  The `--reload` flag in the development command will automatically restart the server on code changes.
4.  Test endpoints using the Swagger UI (`/docs`) or a tool like Postman.

## 🚀 Deployment

To deploy the `TransferLineParisApi` to a production environment, you would typically use a process manager like Gunicorn combined with Uvicorn workers, or containerize it with Docker.

### Production Build

There's no specific "build" step for a Python FastAPI application. The application runs directly.

### Running in Production

To run the application reliably in production, it's recommended to use Gunicorn with Uvicorn workers:

```bash
# Example using Gunicorn with Uvicorn workers (install gunicorn first: pip install gunicorn)
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```
Replace `4` with the desired number of workers based on your server's CPU cores.

## 📚 API Reference

The API automatically generates interactive documentation available at `http://localhost:8000/docs` (Swagger UI) and `http://localhost:8000/redoc` (ReDoc) when the server is running.

### Base URL
`http://localhost:8000` (or your configured host and port)

### Endpoints

#### `GET /`
**Description:** A simple root endpoint to confirm the API is running.
**Response:**
```json
{"message": "Welcome to TransferLineParisApi!"}
```

#### `GET /lines`
**Description:** Retrieves a list of all available transport lines in Paris.
**Response:**
```json
[
  {"line_id": "M1", "name": "Ligne 1"},
  {"line_id": "RER_A", "name": "RER A"},
  // ... more lines
]
```

#### `GET /lines/{line_id}/stations`
**Description:** Retrieves all stations belonging to a specific transport line.
**Parameters:**
-   `line_id` (path): The unique identifier of the transport line (e.g., `M1`, `RER_A`).
**Response:**
```json
[
  {"station_id": "CHLD", "name": "Châtelet-Les Halles", "line_id": "RER_A"},
  {"station_id": "GARE", "name": "Gare de Lyon", "line_id": "RER_A"},
  // ... more stations for RER A
]
```

#### `GET /stations/{station_id}`
**Description:** Retrieves detailed information for a specific station.
**Parameters:**
-   `station_id` (path): The unique identifier of the station (e.g., `CHLD`).
**Response:**
```json
{
  "station_id": "CHLD",
  "name": "Châtelet-Les Halles",
  "latitude": 48.85837,
  "longitude": 2.3488,
  "lines": ["RER_A", "RER_B", "RER_D", "M1", "M4", "M7", "M11", "M14"]
}
```

## 🤝 Contributing

We welcome contributions! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request.

### Development Setup for Contributors
The development setup is identical to the Quick Start guide. Ensure you have Python installed and run `pip install -r requierment.txt`.

## 📄 License

This project currently does not have an explicit license. Please contact the repository owner for licensing information.

## 🙏 Acknowledgments

-   [FastAPI](https://fastapi.tiangolo.com/) - The powerful and modern web framework used for this API.
-   [Uvicorn](https://www.uvicorn.org/) - The lightning-fast ASGI server powering FastAPI.
-   [Pandas](https://pandas.pydata.org/) - For efficient data handling and analysis.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/MaxiyaG/TransferLineParisApi/issues)
-   📧 Email: [TODO: Add contact email]

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [MaxiyaG](https://github.com/MaxiyaG)

</div>
