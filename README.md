# HireStream MCP

A Streamlit-based MCP client that tuns the MCP server and interacts with its tools for managing job applying process.

## Prerequisites

- Python 3.12+
- pip (Python package installer)

## Running the Application

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Streamlit application:

```bash
streamlit run src/app.py
```

## Project Structure

```
hirestream_mcp/
├── src/
│   ├── app.py              # Main Streamlit application
│   ├── mcp_client/         # Client-side components
│   ├── hirestream_mcp_server/  # Server-side components
│   ├── utils/              # Utility functions
│   └── tests/              # Test files
├── .streamlit/             # Streamlit configuration
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

### Running Tests

To run the test suite:

```bash
pytest src/tests/
```
