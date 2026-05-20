import streamlit as st
from src.config import APP_TITLE, APP_SUBTITLE, GEMINI_API_KEY, VECTOR_DIR
from src.ui_components import render_header, render_puter_image_generator
from src.zodiac import get_zodiac_sign, parse_dob
from src.pdf_utils import download_pdfs, extract_text_from_pdfs
from src.rag_pipeline import build_vector_store, load_vector_store, retrieve_context
from src.prompts import build_fortune_prompt
from src.llm_utils import generate_fortune, parse_response_blocks

st.set_page_config(page_title=APP_TITLE, page_icon="🔮", layout="wide")

def ensure_vector_store():
    index_file = VECTOR_DIR / "index.faiss"
    pkl_file = VECTOR_DIR / "index.pkl"
    if index_file.exists() and pkl_file.exists():
        return load_vector_store()

    pdfs = download_pdfs()
    texts = extract_text_from_pdfs(pdfs)
    return build_vector_store(texts)

def main():
    render_header(APP_TITLE, APP_SUBTITLE)

    if not GEMINI_API_KEY:
        st.error("Missing GEMINI_API_KEY. Add it to your .env file before running the app.")
        st.stop()

    with st.sidebar:
        st.header("About")
        st.write("AI baba is a zodiac-based RAG app using PDF knowledge, FAISS retrieval, Gemini text generation, and Puter.js image generation.")
        st.write("First run may take time because PDFs are downloaded and indexed.")

    col1, col2 = st.columns([1, 1])

    with col1:
        name = st.text_input("Enter your name")
        dob = st.date_input("Enter your date of birth")

        build_index = st.checkbox("Rebuild vector DB from PDFs", value=False)

        if st.button("Generate my reading", use_container_width=True):
            if not name.strip():
                st.warning("Please enter your name.")
                st.stop()

            with st.spinner("Preparing knowledge base..."):
                if build_index:
                    pdfs = download_pdfs()
                    texts = extract_text_from_pdfs(pdfs)
                    vectordb = build_vector_store(texts)
                else:
                    vectordb = ensure_vector_store()

            day, month, year = parse_dob(dob)
            zodiac_sign = get_zodiac_sign(day, month)

            with st.spinner("Retrieving zodiac context..."):
                context, docs = retrieve_context(vectordb, zodiac_sign)

            prompt = build_fortune_prompt(name=name, zodiac_sign=zodiac_sign, retrieved_context=context)

            with st.spinner("Generating reading with Gemini..."):
                output_text = generate_fortune(prompt)
                parsed = parse_response_blocks(output_text)

            st.session_state["result"] = parsed
            st.session_state["sources"] = docs
            st.session_state["zodiac"] = zodiac_sign

    with col2:
        st.subheader("Result")
        result = st.session_state.get("result")
        if result:
            st.markdown(f"**Zodiac Sign:** {result.get('zodiac_sign') or st.session_state.get('zodiac','')}")
            st.markdown(f"**Personality Snapshot:** {result.get('personality_snapshot','')}")
            st.markdown(f"**Lucky Color:** {result.get('lucky_color','')}")
            st.markdown(f"**Lucky Number:** {result.get('lucky_number','')}")
            st.markdown(f"**Best Hour:** {result.get('best_hour','')}")
            st.markdown(f"**Today's Incident Prediction:** {result.get('incident_prediction','')}")

            image_prompt = result.get("image_prompt", "").strip()
            if image_prompt:
                st.markdown("### Incident Image")
                render_puter_image_generator(image_prompt)

            with st.expander("Retrieved context chunks"):
                for i, doc in enumerate(st.session_state.get("sources", []), start=1):
                    st.markdown(f"**Chunk {i}:**")
                    st.write(doc.page_content[:1200] + ("..." if len(doc.page_content) > 1200 else ""))
        else:
            st.info("Fill in your details and click 'Generate my reading'.")

if __name__ == "__main__":
    main()