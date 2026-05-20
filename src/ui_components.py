import streamlit as st
import urllib.parse


def inject_custom_css():
    """Inject React-style light theme CSS into the Streamlit app."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }

        /* ── App background ── */
        .stApp {
            background-color: #f5f7fa !important;
        }
        .block-container {
            padding: 2rem 3rem !important;
            max-width: 1200px;
        }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 1px solid #e5e7eb !important;
        }
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] li,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] div {
            color: #374151 !important;
        }

        /* ── App header ── */
        .app-header {
            padding: 1.5rem 0 0.5rem 0;
            border-bottom: 2px solid #e5e7eb;
            margin-bottom: 1.5rem;
        }
        .app-header h1 {
            font-size: 2rem;
            font-weight: 700;
            color: #111827;
            margin: 0;
        }
        .app-header p {
            font-size: 0.95rem;
            color: #6b7280;
            margin: 4px 0 0 0;
        }

        /* ── Input card container (now using st.container border) ── */
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #ffffff !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 12px !important;
            padding: 0.5rem !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
        }

        /* ── ALL widget labels — force dark so they're always visible ── */
        .stTextInput label,
        .stTextInput label p,
        .stDateInput label,
        .stDateInput label p,
        .stCheckbox label,
        .stCheckbox label p,
        .stSelectbox label,
        .stSelectbox label p,
        label[data-testid="stWidgetLabel"],
        label[data-testid="stWidgetLabel"] p,
        [data-testid="stWidgetLabel"],
        [data-testid="stWidgetLabel"] p {
            color: #111827 !important;
            font-weight: 500 !important;
            font-size: 0.9rem !important;
        }

        /* ── Text inputs ── */
        input[type="text"], input[type="number"] {
            border-radius: 8px !important;
            border: 1px solid #d1d5db !important;
            background: #f9fafb !important;
            color: #111827 !important;
            font-family: 'Inter', sans-serif !important;
        }
        input[type="text"]:focus {
            border-color: #6366f1 !important;
            box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
        }

        /* ── Date input ── */
        [data-testid="stDateInput"] input {
            border-radius: 8px !important;
            border: 1px solid #d1d5db !important;
            background: #f9fafb !important;
            color: #111827 !important;
        }

        /* ── Checkbox ── */
        .stCheckbox span {
            color: #111827 !important;
        }

        /* ── Button ── */
        .stButton > button {
            background: #6366f1 !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            padding: 0.6rem 1.5rem !important;
            transition: background 0.2s ease !important;
        }
        .stButton > button:hover {
            background: #4f46e5 !important;
        }

        /* ── Zodiac badge ── */
        .zodiac-badge {
            display: inline-block;
            background: #eef2ff;
            color: #4338ca;
            font-size: 1.1rem;
            font-weight: 700;
            padding: 0.4rem 1.1rem;
            border-radius: 999px;
            margin-bottom: 1.2rem;
            border: 1px solid #c7d2fe;
        }

        /* ── Stats row ── */
        .stats-row {
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }
        .stat-pill {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 0.8rem 1.4rem;
            text-align: center;
            font-size: 0.9rem;
            color: #374151;
            min-width: 130px;
        }

        /* ── Result cards ── */
        .result-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 1.4rem 1.6rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .highlight-card {
            border-left: 4px solid #6366f1;
            background: #fafafe;
        }
        .result-card h4,
        .result-card p,
        .result-card span {
            color: #111827 !important;
        }

        /* ── General markdown text (personality, prediction content) ── */
        .stMarkdown p,
        .stMarkdown span,
        .stMarkdown li {
            color: #374151 !important;
        }

        /* ── Empty state ── */
        .empty-state {
            text-align: center;
            color: #9ca3af;
            padding: 3rem 1rem;
            font-size: 1rem;
        }

        /* ── Incident image ── */
        .incident-image {
            width: 100%;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin-top: 0.5rem;
        }

        /* ── Divider ── */
        hr {
            border-color: #e5e7eb !important;
        }

        /* ── Expander ── */
        [data-testid="stExpander"] summary,
        [data-testid="stExpander"] summary p {
            color: #374151 !important;
            font-weight: 500 !important;
        }

        /* ── Spinner / status text ── */
        [data-testid="stStatusWidget"] span,
        .stSpinner p {
            color: #6b7280 !important;
        }

        /* ── Warning / error / info messages ── */
        .stAlert p {
            color: #111827 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header(title: str, subtitle: str):
    st.markdown(
        f"""
        <div class="app-header">
            <h1>🔮 {title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_auto_image(image_prompt: str):
    """
    Renders an AI-generated image using Pollinations.ai.
    Completely free, no API key, no WebSocket — just a URL.
    """
    if not image_prompt:
        st.info("No image prompt available.")
        return

    # Encode prompt for URL
    encoded_prompt = urllib.parse.quote(image_prompt)

    # Pollinations.ai free image generation — no API key needed
    seed = abs(hash(image_prompt)) % 99999
    image_url = (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width=800&height=500&seed={seed}&nologo=true&enhance=true"
    )

    st.markdown(
        f'<img src="{image_url}" class="incident-image" alt="Incident Image" />',
        unsafe_allow_html=True,
    )
    st.caption("🎨 Generated by Pollinations.ai (free, no API key)")
