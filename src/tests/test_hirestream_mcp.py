import json
import os
import threading
from pathlib import Path

import pytest
import pytest_asyncio
import uvicorn
from dotenv import load_dotenv
from dummy_server import app, parse_resume
from fastapi.testclient import TestClient
from inline_snapshot import snapshot
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

load_dotenv()

# Set up OpenAI model
model = OpenAIModel(
    "gpt-4.1-2025-04-14",
    provider=OpenAIProvider(api_key=os.getenv("OPENAI_API_KEY")),
)

env = {
    "BASE_API_URL": "http://127.0.0.1:8000",
}

# Get the absolute path to the MCP server script
current_dir = Path(__file__).parent.parent
mcp_server_path = current_dir / "hirestream_mcp_server" / "hirestream_mcp.py"
mcp_servers = [MCPServerStdio("python", [str(mcp_server_path)], env=env)]

# Set up Agent with Server
test_agent = Agent(
    model,
    mcp_servers=mcp_servers,
    instructions="""
You are a helpful assistant that can help with job applications.

Always ask for user's resume before applying to a job.
""",
)


def _get_tool_calls(result):
    tool_calls = []
    history = result.new_messages()
    for message in history:
        try:
            for part in message.parts:
                if part.part_kind == "tool-call":
                    heading = part.tool_name
                    try:
                        content = json.loads(part.args)
                    except:
                        content = part.args
                    tool_calls.append(
                        {
                            "heading": heading,
                            "content": content,
                        }
                    )
        except Exception as e:
            print(e)
    return tool_calls


def _find_tool_call(tool_calls, tool_name):
    for tool_call in tool_calls:
        if tool_call["heading"] == tool_name:
            return {"heading": tool_call["heading"], "content": tool_call["content"]}
    return None


@pytest.fixture
def test_client():
    """Fixture to provide a test client for the FastAPI app."""
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
def start_test_server():
    """Start the test server in a separate thread."""

    def run_server():
        uvicorn.run(app, host="127.0.0.1", port=8000)

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    # Give the server a moment to start
    import time

    time.sleep(1)
    yield
    # The server will be automatically shut down when the test session ends


class TestListJobs:
    """Unit test class for Hirestream MCP tools."""

    @pytest.mark.asyncio
    async def test_list_jobs(self, test_client):
        """Test list jobs."""
        async with test_agent.run_mcp_servers():
            result = await test_agent.run("List jobs")

        tool_calls = _get_tool_calls(result)
        assert _find_tool_call(tool_calls, "list_jobs") == snapshot(
            {"heading": "list_jobs", "content": "{}"}
        )


class TestApplyToJob:
    """Unit test class for Hirestream MCP tools."""

    @pytest.mark.asyncio
    async def test_apply_to_job(self, test_client):
        """Test apply to job."""
        cv_data = await parse_resume()
        async with test_agent.run_mcp_servers():
            result = await test_agent.run(
                user_prompt="Apply to job of social media associate. I am male and my linkedin is https://www.linkedin.com/in/saifullah-1234567890/. \
                    Use random values for next"
                + str(cv_data)
            )

        tool_calls = _get_tool_calls(result)
        assert _find_tool_call(tool_calls, "apply_to_job")["content"][
            "job_apply_request"
        ]["candidate"]["email"] == snapshot("safihum99@gmail.com")
