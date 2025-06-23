import asyncio

import streamlit as st

from mcp_client.mcp_client import run_mcp_client


def process_async_response(prompt, agent_message_history):
    """Process the prompt asynchronously and return the response."""
    try:
        # Get the current event loop or create a new one
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        # Create a queue to store the chunks
        queue = asyncio.Queue()

        # Define the async producer
        async def producer():
            try:
                async for chunk in run_mcp_client(prompt, agent_message_history):
                    await queue.put(chunk)
            finally:
                await queue.put(None)  # Signal the end

        # Define the sync consumer
        def consumer():
            while True:
                chunk = loop.run_until_complete(queue.get())
                if chunk is None:  # End signal
                    break
                yield chunk

        # Start the producer task
        producer_task = loop.create_task(producer())

        # Run the consumer
        response = st.write_stream(consumer())

        # Clean up
        loop.run_until_complete(producer_task)
        return response

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return "I apologize, but I encountered an error while processing your request."
