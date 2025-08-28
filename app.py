import streamlit as st
from openai import OpenAI

# Create a client
client = OpenAI(api_key="")


st.set_page_config(page_title="AI Support Agent", page_icon="🤖")
st.title("🤖 AI Customer Support Agent")

user_input = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a helpful support agent."},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=150
                )
                answer = response.choices[0].message.content
                st.success(answer)

            except Exception as e:
                st.error(f"Error: {str(e)}")
