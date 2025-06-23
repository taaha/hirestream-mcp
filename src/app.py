import nest_asyncio
import streamlit as st

from utils.parse import parse_resume

from mcp_client.mcp_client import run_mcp_client

# from utils.process_async import process_async_response

nest_asyncio.apply()

st.title("Hirestream MCP Client")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "agent_message_history" not in st.session_state:
    st.session_state.agent_message_history = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input(
    "Hello, How can I help you today?", accept_file=True, file_type=["pdf"]
):
    if prompt.text:
        processed_prompt = prompt.text
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": processed_prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(processed_prompt)

    else:
        pdf_content = prompt.files[0].read()
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": "Resume uploaded"})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown("Resume uploaded")
        processed_prompt = "Data extracted from resume: " + str(
            parse_resume(pdf_content)
        )

        if processed_prompt is None:
            st.error("Failed to parse PDF file. Please try again.")
            st.stop()

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = process_async_response(
            processed_prompt, st.session_state.agent_message_history
        )

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
