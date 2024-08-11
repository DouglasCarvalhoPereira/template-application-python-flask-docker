# 🐍 Python Flask Application with Docker

This repository contains a template for a Python Flask web application, fully containerized using Docker. It's a minimal setup to get you started with building and deploying your Flask applications.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Application Structure](#application-structure)
- [Docker Usage](#docker-usage)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Getting Started

This section will guide you through setting up and running the Flask application.

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. **Install dependencies:**

   If you are not using Docker and want to run the app locally, create a virtual environment and install the dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## ▶️ Running the Application

### Running Locally

To run the Flask application locally (without Docker):

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

### Docker Usage

1. **Build the Docker image:**

   ```bash
   docker build -t flask-app .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -d -p 5000:5000 flask-app
   ```

   The application will be available at `http://localhost:5000/`.

## 📁 Application Structure

```
repository-name/
│
├── app.py              # Main Flask application
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
└── static/             # Static files (CSS, JS, images)
```

- **`app.py`**: The main application file where the Flask app is defined.
- **`Dockerfile`**: Contains instructions to build the Docker image.
- **`requirements.txt`**: Lists the Python packages required to run the application.
- **`templates/`**: Directory containing HTML templates.
- **`static/`**: Directory for static files like CSS, JavaScript, and images.

## 🤝 Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
