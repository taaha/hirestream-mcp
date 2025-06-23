from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import dspy

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=[
        "./hirestream_mcp_server/hirestream_mcp.py"
    ],  # Optional command line arguments
    env=None,  # Optional environment variables
)


class DSPyAirlineCustomerService(dspy.Signature):
    """You are an airline customer service agent. You are given a list of tools to handle user requests.
    You should decide the right tool to use in order to fulfill users' requests."""

    user_request: str = dspy.InputField()
    process_result: str = dspy.OutputField(
        desc=(
            "Message that summarizes the process result, and the information users need, "
            "e.g., the confirmation_number if it's a flight booking request."
        )
    )


dspy.configure(lm=dspy.LM("gpt-4.1-2025-04-14"))


async def run(user_request):
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()

            # Convert MCP tools to DSPy tools
            dspy_tools = []
            for tool in tools.tools:
                dspy_tools.append(dspy.Tool.from_mcp_tool(session, tool))

            # Create the agent
            react = dspy.ReAct(DSPyAirlineCustomerService, tools=dspy_tools)

            result = await react.acall(user_request=user_request)
            print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(
        run(
            "please help me book a flight from SFO to JFK on 09/01/2025, my name is Adam"
        )
    )
