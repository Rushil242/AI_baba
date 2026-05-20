import streamlit as st
import streamlit.components.v1 as components


def inject_custom_css():
    """Inject React-style light theme CSS into the Streamlit app."""
    st.markdown(
        """
        <style>
        /* ── Global reset & font ───────────────────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }

        /* ── Background & main container ───────────────────────────────── */
        .stApp {
            background-color: #f5f7fa !important;
        }
        .block-container {
            padding: 2rem 3rem !important;
            max-width: 1200px;
        }

        /* ── Sidebar ────────────────────────────────────────────────────── */
        [data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 1px solid #e5e7eb !important;
        }
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] li,
        [data-testid="stSidebar"] h3 {
            color: #374151 !important;
        }

        /* ── Page header ─────────────────────────────────────────────────── */
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

        /* ── Input card ──────────────────────────────────────────────────── */
        .card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 1.5rem 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        }

        /* ── Inputs ──────────────────────────────────────────────────────── */
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

        /* ── Primary button ──────────────────────────────────────────────── */
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

        /* ── Zodiac badge ────────────────────────────────────────────────── */
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

        /* ── Stat pills ──────────────────────────────────────────────────── */
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
            flex: 1;
            min-width: 140px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }
        .stat-pill strong {
            display: block;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #9ca3af;
            margin-bottom: 4px;
        }

        /* ── Result cards ────────────────────────────────────────────────── */
        .result-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 1.4rem 1.6rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            color: #374151;
        }
        .highlight-card {
            border-left: 4px solid #6366f1 !important;
            background: #fafafa !important;
        }

        /* ── Empty state ─────────────────────────────────────────────────── */
        .empty-state {
            text-align: center;
            color: #9ca3af;
            padding: 3rem 1rem;
            font-size: 1rem;
            border: 2px dashed #e5e7eb;
            border-radius: 12px;
            margin-top: 1rem;
        }

        /* ── Headings & text ─────────────────────────────────────────────── */
        h1, h2, h3, h4 {
            color: #111827 !important;
        }
        p, li, label {
            color: #374151 !important;
        }

        /* ── Expander ────────────────────────────────────────────────────── */
        .streamlit-expanderHeader {
            background: #f9fafb !important;
            border-radius: 8px !important;
            color: #374151 !important;
            font-weight: 500 !important;
        }

        /* ── Divider ─────────────────────────────────────────────────────── */
        hr {
            border: none;
            border-top: 1px solid #e5e7eb !important;
            margin: 1.5rem 0 !important;
        }

        /* ── Hide Streamlit branding ─────────────────────────────────────── */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_header(title: str, subtitle: str):
    """Render a clean page header."""
    st.markdown(
        f"""
        <div class="app-header">
            <h1>🔮 {title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_auto_image(image_prompt: str):
    """
    Auto-trigger Puter.js image generation on load.
    No button shown, no prompt shown — image appears automatically.
    """
    safe_prompt = image_prompt.replace("`", "'").replace('"', "'")

    html = f"""
    <div id="img-wrapper" style="
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 340px;
        background: #f9fafb;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        overflow: hidden;
        margin-top: 0.5rem;
    ">
        <div id="loading-msg" style="
            color: #9ca3af;
            font-family: Inter, sans-serif;
            font-size: 0.95rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
        ">
            <div style="
                width: 32px; height: 32px;
                border: 3px solid #e5e7eb;
                border-top-color: #6366f1;
                border-radius: 50%;
                animation: spin 0.8s linear infinite;
            "></div>
            Generating incident image…
        </div>
        <img id="gen-img" src="" alt="Incident image"
             style="display:none; max-width:100%; max-height:480px; border-radius:10px; object-fit:cover;" />
    </div>

    <style>
        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
    </style>

    <script src="https://js.puter.com/v2/"></script>
    <script>
        (async () => {{
            try {{
                const imgEl     = document.getElementById('gen-img');
                const loadingEl = document.getElementById('loading-msg');
                const result    = await puter.ai.txt2img("{safe_prompt}");
                const src       = (typeof result === 'string') ? result : (result.src || result.url || '');
                if (src) {{
                    imgEl.src     = src;
                    imgEl.style.display = 'block';
                    loadingEl.style.display = 'none';
                }} else {{
                    loadingEl.innerHTML = '⚠️ Image generation returned no result.';
                }}
            }} catch (e) {{
                document.getElementById('loading-msg').innerHTML =
                    '⚠️ Image generation failed: ' + e.message;
            }}
        }})();
    </script>
    """
    components.html(html, height=500)