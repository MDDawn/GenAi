import streamlit as st
from perplexity import Perplexity

px = Perplexity(api_key="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")

st.title("My Own AI")

q = st.text_input("Question:")

if st.button("Send"):
    if q:
        with st.spinner("Thinking..."):
            response = px.chat.completions.create(
                model="sonar-pro",
                messages=[
                    {
                        "role": "user",
                        "content": q
                    }
                ],
            )
            st.write("Reply:", response.choices[0].message.content)
    else:
        st.warning("Please enter a question.")
