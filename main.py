# import json
# import requests
# import streamlit as st

# url = "http://localhost:11434/api/generate"

# headers = {
#     'Content-Type': 'application/json',
# }

# conversation_history = []
# def generate_response(prompt):
#     conversation_history.append(prompt)
#     full_prompt = "\n".join(conversation_history)
    
#     data = {
#         "model": "orca-mini",
#         "stream": False,
#         "prompt": full_prompt
#     }

#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     if response.status_code == 200:
#         response_text = response.text
#         data = json.loads(response_text)
#         actual_response = data["response"]
#         conversation_history.append(actual_response)
#         return actual_response
#     else:
#         return f"Error: {response.status_code}, {response.text}"

# # Streamlit UI
# st.title("Offline - Ollama - GPT")
# st.markdown('<div style="font-family:arial black; color: white;"> </div>', unsafe_allow_html=True)
# user_input = st.text_area("Enter your prompt here....", height=100)
# if st.button("Generate Response"):
#     response = generate_response(user_input)
#     st.write("Generated Response:")
#     st.write(response)

import json
import requests
import streamlit as st

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

# Initialize conversation history
conversation_history = []

def generate_response(prompt):
    conversation_history.append(prompt)
    full_prompt = "\n".join(conversation_history)
    
    data = {
        "model": "orca-mini",
        "stream": False,
        "prompt": full_prompt
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response
    else:
        return f"Error: {response.status_code}, {response.text}"


# Streamlit UI
st.title("Offline - Ollama - GPT")
st.markdown('<div style="font-family:arial black; color: white;"> </div>', unsafe_allow_html=True)
user_input = st.text_area("Enter your prompt here....", height=100)
if st.button("Generate Response"):
    response = generate_response(user_input)
    st.write("Generated Response:")
    st.write(response)
    


