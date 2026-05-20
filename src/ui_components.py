import streamlit as st
import streamlit.components.v1 as components
import html
import json

def render_header(title: str, subtitle: str):
    st.markdown(f"""
    <div style="padding: 0.2rem 0 1rem 0;">
        <h1 style="margin-bottom:0.2rem;">{title}</h1>
        <p style="color:#666; margin-top:0;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def render_puter_image_generator(image_prompt: str):
    safe_prompt = json.dumps(image_prompt)
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <script src="https://js.puter.com/v2/"></script>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background: white;
          margin: 0;
          padding: 0;
        }}
        .wrap {{
          border: 1px solid #ddd;
          border-radius: 12px;
          padding: 16px;
        }}
        .btn {{
          background: black;
          color: white;
          border: none;
          padding: 10px 16px;
          border-radius: 8px;
          cursor: pointer;
          font-size: 14px;
        }}
        .btn:disabled {{
          opacity: 0.6;
          cursor: not-allowed;
        }}
        .status {{
          margin-top: 10px;
          color: #444;
          font-size: 14px;
        }}
        .imgbox {{
          margin-top: 16px;
          min-height: 120px;
        }}
        img {{
          max-width: 100%;
          border-radius: 10px;
          border: 1px solid #ddd;
        }}
        .prompt {{
          font-size: 13px;
          color: #555;
          white-space: pre-wrap;
          margin-bottom: 8px;
        }}
      </style>
    </head>
    <body>
      <div class="wrap">
        <div class="prompt"><strong>Image prompt:</strong> {html.escape(image_prompt)}</div>
        <button id="genBtn" class="btn">Generate incident image with Puter.js</button>
        <div id="status" class="status">Ready.</div>
        <div id="imgbox" class="imgbox"></div>
      </div>

      <script>
        const prompt = {safe_prompt};
        const btn = document.getElementById("genBtn");
        const status = document.getElementById("status");
        const imgbox = document.getElementById("imgbox");

        btn.addEventListener("click", async () => {{
          try {{
            btn.disabled = true;
            status.textContent = "Generating image... please complete Puter authentication if prompted.";
            imgbox.innerHTML = "";

            const img = await puter.ai.txt2img(prompt, {{
              model: "flux-schnell"
            }});

            img.style.maxWidth = "100%";
            img.style.height = "auto";
            imgbox.appendChild(img);
            status.textContent = "Done. You can right-click and save the image.";
          }} catch (err) {{
            status.textContent = "Image generation failed: " + (err?.message || err);
          }} finally {{
            btn.disabled = false;
          }}
        }});
      </script>
    </body>
    </html>
    """
    components.html(html_code, height=520, scrolling=False)