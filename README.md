# Agents Project

A Python-based project that leverages the Agno framework and Google's Gemini AI models to create intelligent agents capable of processing text and video inputs. The project demonstrates how to integrate with Google's Vertex AI services and handle various types of media content.

## Features

- Integration with Google's Gemini AI models through Vertex AI
- Support for processing both text and video content
- Environment variable based configuration
- Easy-to-use agent interface for generating AI responses
- Support for streaming responses

## Prerequisites

- Python 3.10 or higher
- Google Cloud account with Vertex AI API enabled
- Google Cloud Project with appropriate permissions
- Python virtual environment (recommended)
- [uv](https://github.com/astral-sh/uv) package manager (optional but recommended)

## Installation

### Option 1: Using uv (Recommended)

1. **Install uv** (if not already installed):
   ```bash
   curl -sSf https://astral.sh/uv/install.sh | sh
   ```
   Restart your terminal after installation.

2. **Clone the repository** (if not already cloned):
   ```bash
   git clone <repository-url>
   cd Agents
   ```

3. **Create and activate a virtual environment** using uv:
   ```bash
   uv venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies** using uv:
   ```bash
   uv pip install -e .
   ```
   This will install all dependencies listed in `pyproject.toml` in an isolated environment.

### Option 2: Using standard Python tools

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Agents
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Upgrade pip and install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -e .
   ```

### Environment Setup

1. **Create a `.env` file** in the project root with the following variables:
   ```env
   DEFAULT_MODEL="gemini-1.5-flash-002"
   GOOGLE_GENAI_USE_VERTEXAI="true"
   GOOGLE_CLOUD_PROJECT="your-project-id"
   GOOGLE_CLOUD_LOCATION="your-region"
   ```

2. **Install pre-commit hooks** (if configured):
   ```bash
   pre-commit install
   ```

## Using uv for Development

uv provides faster package installation and dependency resolution. Here are some useful commands:

- **Add a new dependency**:
  ```bash
  uv pip install package-name
  ```

- **Add a development dependency**:
  ```bash
  uv pip install --group dev package-name
  ```

- **Update all dependencies**:
  ```bash
  uv pip compile --upgrade
  ```

- **Sync virtual environment** (after updating dependencies):
  ```bash
  uv pip sync
  ```

{{ ... rest of the README.md remains the same ... }}