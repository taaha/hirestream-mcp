# PydanticAI Agent with MCP
from pathlib import Path
from typing import Dict, List

import logfire
from decouple import config
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.messages import (
    FunctionToolCallEvent,
    FunctionToolResultEvent,
    PartDeltaEvent,
    TextPartDelta,
)
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

logfire.configure(token=config("LOGFIRE_API_KEY"))
logfire.instrument_openai()

chat_history_size = 50

# Set up OpenAI model
model = OpenAIModel(
    "gpt-4.1-2025-04-14",
    provider=OpenAIProvider(api_key=config("OPENAI_API_KEY")),
)

# Set up environment variables for MCP server
env = {
    "BASE_API_URL": config("BASE_API_URL"),
}

# Get the absolute path to the MCP server script
current_dir = Path(__file__).parent.parent
mcp_server_path = current_dir / "hirestream_mcp_server" / "hirestream_mcp.py"
# mcp_servers = [MCPServerStdio("python", [str(mcp_server_path)], env=env)]
import sys

mcp_servers = [MCPServerStdio(sys.executable, [str(mcp_server_path)], env=env)]

# Set up Agent with Server
agent = Agent(
    model,
    mcp_servers=mcp_servers,
    instructions="""
You are a helpful assistant that can help with job applications.

Always ask for user's resume before applying to a job.
""",
)

nodes = []


async def run_mcp_client(user_prompt: str, agent_message_history: List[Dict]):
    async with agent.run_mcp_servers():
        async with agent.iter(
            user_prompt, message_history=agent_message_history
        ) as run:
            async for node in run:
                if Agent.is_model_request_node(node):
                    async with node.stream(run.ctx) as request_stream:
                        async for event in request_stream:
                            if isinstance(event, PartDeltaEvent):
                                if isinstance(event.delta, TextPartDelta):
                                    yield event.delta.content_delta
                elif Agent.is_call_tools_node(node):
                    async with node.stream(run.ctx) as handle_stream:
                        async for event in handle_stream:
                            if isinstance(event, FunctionToolCallEvent):
                                yield "`Calling tool: " + event.part.tool_name + " with args: " + str(
                                    event.part.args
                                ) + "`\n\n"
                            elif isinstance(event, FunctionToolResultEvent):
                                yield "`Tool call returned => " + str(
                                    event.result.content
                                ) + "`\n\n"

            agent_message_history.extend(run.result.new_messages())
            if len(agent_message_history) >= chat_history_size:
                agent_message_history.pop(0)
