import streamlit as st
import os
from dotenv import load_dotenv
from models import AiPromptEnchancer
from prompts import TEXT_ENHANCER

load_dotenv()

st.set_page_config(page_title="Prompt Optimizer", layout="wide")
st.title("🚀 Prompt Optimizer")
st.write("Analizuj i ulepszaj swoje prompty do AI")

SELECTED_MODEL = os.getenv("SELECTED_MODEL", "gpt-4o-mini")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Wpisz swój prompt:")
    user_prompt = st.text_area("", height=250, placeholder="Wpisz tutaj swój prompt...")

with col2:
    st.subheader("✨ Analiza:")

    if st.button("🔍 Check", use_container_width=True):
        if user_prompt.strip():
            with st.spinner("Analizuję..."):
                try:
                    enchancer = AiPromptEnchancer(model=SELECTED_MODEL, sys_prompt=TEXT_ENHANCER)
                    result = enchancer.run(user_prompt)

                    st.markdown(result["content"])

                    st.divider()
                    col_tokens = st.columns(3)
                    with col_tokens[0]:
                        st.metric("Wejście", result["tokens"]["prompt_tokens"])
                    with col_tokens[1]:
                        st.metric("Wyjście", result["tokens"]["completion_tokens"])
                    with col_tokens[2]:
                        st.metric("Łącznie", result["tokens"]["total_tokens"])
                except Exception as e:
                    st.error(f"❌ Błąd: {str(e)}")
        else:
            st.warning("⚠️ Wpisz prompt przed kliknięciem Check!")
