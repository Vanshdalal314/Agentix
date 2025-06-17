#Setup Streamlit UI
import streamlit as st
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama3-70b-8192"]
st.set_page_config(page_title="Agentix",layout="wide")
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("                   ")
    st.markdown("                   ")
    st.markdown("🛠️ Agent Configuration")
    provider = st.radio("Select Provider", ["Groq"])
    selected_model = st.selectbox("Select Model:", MODEL_NAMES_GROQ)
    allow_web_search = st.checkbox("🌐 Allow Web Search")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.title("Agentix")
    st.write("Smarter conversations, your way.")
    system_prompt=st.text_area("Define your AI Agent: ", height=80, placeholder="Type your system prompt here.. \nExample: Act as an Financial Advisor, Medical Assistant, Data Analyst, Software Developer etc")
    user_query = st.text_area("Enter your Query: ",height=150, placeholder="Ask Anything")

    api_url="http://127.0.0.1:9999/chat"
    if st.button("Ask Agent !"):
        if user_query.strip():
            #Get response from backend and show
            import requests

            payload={
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }

            response=requests.post(api_url, json=payload)
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.subheader("Agent Response")
                    st.markdown(f"🤖 Response: {response_data}")
