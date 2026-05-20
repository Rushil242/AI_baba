import streamlit as st
from src.config import APP_TITLE, APP_SUBTITLE, GEMINI_API_KEY, VECTOR_DIR
from src.ui_components import render_header, render_auto_image, inject_custom_css
from src.zodiac import get_zodiac_sign, parse_dob
from src.pdf_utils import get_pdf_paths, extract_text_from_pdfs
from src.rag_pipeline import build_vector_store, load_vector_store, retrieve_context
from src.prompts import build_fortune_prompt
from src.llm_utils import generate_fortune, parse_response_blocks

st.set_page_config(page_title=APP_TITLE, page_icon="🔮", layout="wide")

# Inject React-style light theme CSS
inject_custom_css()


def ensure_vector_store():
    index_file = VECTOR_DIR / "index.faiss"
    pkl_file = VECTOR_DIR / "index.pkl"
    if index_file.exists() and pkl_file.exists():
        return load_vector_store()
    pdfs = get_pdf_paths()
    texts = extract_text_from_pdfs(pdfs)
    return build_vector_store(texts)


def main():
    render_header(APP_TITLE, APP_SUBTITLE)

    if not GEMINI_API_KEY:
        st.error("🔑 Missing GEMINI_API_KEY. Add it to your .env file before running the app.")
        st.stop()

    with st.sidebar:
        st.markdown("### 🔮 About AI Fortune Teller")
        st.markdown(
            "AI Fortune teller is a zodiac-based RAG app powered by **Gemini AI**, "
            "**FAISS vector retrieval**, and **Puter.js image generation**."
        )
        st.markdown("---")
        st.markdown("📁 PDFs are read from `data/pdfs/` and indexed on first run.")
        st.markdown("🖼️ Incident images are generated automatically after each reading.")

    # ── Input card ──────────────────────────────────────────────────────────
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col_a, col_b = st.columns([1, 1], gap="large")
    with col_a:
        name = st.text_input("👤 Your Name", placeholder="e.g. Rushil")
    with col_b:
        dob = st.date_input("🎂 Date of Birth")

    col_c, col_d = st.columns([1, 1], gap="large")
    with col_c:
        build_index = st.checkbox("🔄 Rebuild vector DB from PDFs", value=False)
    with col_d:
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("✨ Generate My Reading", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Generation logic ─────────────────────────────────────────────────────
    if generate_btn:
        if not name.strip():
            st.warning("Please enter your name.")
            st.stop()

        with st.spinner("📚 Preparing knowledge base..."):
            if build_index:
                pdfs = get_pdf_paths()
                texts = extract_text_from_pdfs(pdfs)
                vectordb = build_vector_store(texts)
            else:
                vectordb = ensure_vector_store()

        day, month, year = parse_dob(dob)
        zodiac_sign = get_zodiac_sign(day, month)

        with st.spinner("🔍 Retrieving zodiac context..."):
            context, docs = retrieve_context(vectordb, zodiac_sign)

        prompt = build_fortune_prompt(name=name, zodiac_sign=zodiac_sign, retrieved_context=context)

        with st.spinner("🌟 Generating your reading with Gemini..."):
            output_text = generate_fortune(prompt)
            parsed = parse_response_blocks(output_text)

        st.session_state["result"] = parsed
        st.session_state["sources"] = docs
        st.session_state["zodiac"] = zodiac_sign

    # ── Result display ────────────────────────────────────────────────────────
    result = st.session_state.get("result")
    if result:
        zodiac_sign = result.get("zodiac_sign") or st.session_state.get("zodiac", "")
        st.markdown("---")

        # Top result row — zodiac badge + personality
        st.markdown(
            f'<div class="zodiac-badge">♈ {zodiac_sign}</div>',
            unsafe_allow_html=True
        )

        # Stat pills row
        lucky_color  = result.get("lucky_color", "—")
        lucky_number = result.get("lucky_number", "—")
        best_hour    = result.get("best_hour", "—")

        st.markdown(
            f"""
            <div class="stats-row">
                <div class="stat-pill">🎨 <strong>Lucky Color</strong><br>{lucky_color}</div>
                <div class="stat-pill">🔢 <strong>Lucky Number</strong><br>{lucky_number}</div>
                <div class="stat-pill">⏰ <strong>Best Hour</strong><br>{best_hour}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Personality + Prediction cards side by side
        col1, col2 = st.columns([1, 1], gap="large")
        with col1:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 🧠 Personality Snapshot")
            st.write(result.get("personality_snapshot", ""))
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="result-card highlight-card">', unsafe_allow_html=True)
            st.markdown("#### 🔮 Today's Incident Prediction")
            st.write(result.get("incident_prediction", ""))
            st.markdown('</div>', unsafe_allow_html=True)

        # Auto-generated incident image (no button, no prompt shown)
        image_prompt = result.get("image_prompt", "").strip()
        if image_prompt:
            st.markdown("---")
            st.markdown("#### 🖼️ Incident Image")
            render_auto_image(image_prompt)

        # Context expander
        with st.expander("📄 Retrieved Context Chunks"):
            for i, doc in enumerate(st.session_state.get("sources", []), start=1):
                st.markdown(f"**Chunk {i}:**")
                st.write(doc.page_content[:1200] + ("..." if len(doc.page_content) > 1200 else ""))

    else:
        st.markdown(
            '<div class="empty-state">Enter your name and date of birth above, then click <strong>Generate My Reading</strong>.</div>',
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()