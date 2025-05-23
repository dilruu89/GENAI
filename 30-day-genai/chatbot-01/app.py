import streamlit as st
import openai

st.title("WELCOME TO MY CHATBOT... 🧑‍💻💬 ")
"""
Note: This chatbot will give a warning if you put any sensitive information
"""

#connect openai key
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "You are an AI assistant."}]

# Display previous messages
for message in st.session_state["messages"]:
    # Check the role to determine how to display the message
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])
    else:  # Default case, for system messages or any other type
        st.text(message["content"])  # Using st.text for system messages or other roles



if prompt := st.chat_input():

    # Assuming this function call is correctly displaying the user's message in your setup
        st.chat_message("user").write(prompt)
    
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append({"role": "assistant", "content": msg.content})
    
    # Display the assistant's response immediately after getting it
        st.chat_message("assistant").write(msg.content)

if st.button('Clear Conversation'):
    st.session_state.messages = [
        {"role": "system", "content": ""}
    ]
    st.experimental_rerun()