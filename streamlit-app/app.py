import streamlit as st
import requests

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="Ashwin Gopal · Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── GITHUB RAW BASE URL ──────────────────────────────────────
BASE = "https://raw.githubusercontent.com/Charlie2094/Ashwin-portfolio/main/HTML"

URLS = {
    "portfolio":    f"{BASE}/ashwin_gopal_portfolio.html",
    "architecture": f"{BASE}/ashwin_architecture.html",
    "flow":         f"{BASE}/autorequest_flow.html",
    "resume":       f"{BASE}/ashwin_gopal_resume.html",
}

# ── FETCH HTML FROM GITHUB ───────────────────────────────────
@st.cache_data(ttl=300)
def fetch_html(url: str) -> str:
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.text
    except Exception as e:
        return f"<h2 style='color:red;padding:40px;font-family:sans-serif;'>Failed to load: {e}</h2>"

# ── CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Remove extra padding */
  .block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
    max-width: 100% !important;
  }

  /* Hide Streamlit branding */
  #MainMenu { visibility: hidden; }
  footer    { visibility: hidden; }

  /* Force sidebar always visible */
  [data-testid="stSidebar"] {
    min-width: 260px !important;
    max-width: 260px !important;
  }
  [data-testid="stSidebarNav"] { display: none; }

  /* Profile card */
  .profile-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 10px;
    text-align: center;
  }
  .profile-avatar {
    width: 52px; height: 52px; border-radius: 50%;
    background: linear-gradient(135deg, #e94560, #8b5cf6);
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; font-weight: 800;
    margin: 0 auto 8px; color: white;
  }
  .profile-name { font-size: 13px; font-weight: 700; }
  .profile-role { font-size: 10.5px; opacity: 0.5; margin-top: 2px; }
  .online-badge {
    display: inline-block;
    background: rgba(16,185,129,0.2); color: #10b981;
    font-size: 10px; font-weight: 700;
    padding: 2px 10px; border-radius: 20px; margin-top: 6px;
    border: 1px solid rgba(16,185,129,0.3);
  }

  /* Metrics */
  .metric-row {
    display: grid; grid-template-columns: repeat(2,1fr);
    gap: 6px; margin-bottom: 10px;
  }
  .metric-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 8px; padding: 8px; text-align: center;
  }
  .metric-val { font-size: 18px; font-weight: 800; line-height: 1; }
  .metric-lbl { font-size: 9.5px; opacity: 0.4; margin-top: 2px; }

  /* Links */
  .qlink {
    display: flex; align-items: center; gap: 7px;
    padding: 7px 12px; border-radius: 8px;
    font-size: 11.5px; font-weight: 600;
    text-decoration: none; margin-bottom: 5px;
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.05);
    color: rgba(255,255,255,0.75) !important;
  }
  .qlink:hover { opacity: 0.75; }
  .qlink-green { background:rgba(16,185,129,0.12)!important; border-color:rgba(16,185,129,0.3)!important; color:#10b981!important; }
  .qlink-blue  { background:rgba(59,130,246,0.12)!important; border-color:rgba(59,130,246,0.3)!important; color:#60a5fa!important; }
  .qlink-red   { background:rgba(233,69,96,0.12)!important;  border-color:rgba(233,69,96,0.3)!important;  color:#ff7d94!important; }

  /* Section label */
  .slabel {
    font-size: 9px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 1.5px;
    opacity: 0.3; padding: 4px 0 5px; display: block;
  }

  /* Download button */
  .stDownloadButton > button {
    width: 100% !important;
    background: linear-gradient(135deg,#e94560,#c41d3c) !important;
    color: white !important; border: none !important;
    border-radius: 8px !important; font-weight: 700 !important;
  }
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR ──────────────────────────────────────────────────
with st.sidebar:

    st.markdown("""
    <div class="profile-card">
      <div class="profile-avatar">AG</div>
      <div class="profile-name">Ashwin Gopal</div>
      <div class="profile-role">Senior Automation Developer</div>
      <div class="profile-role">WPP Production · Chennai</div>
      <div class="online-badge">⚡ Open to Opportunities</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-row">
      <div class="metric-card"><div class="metric-val" style="color:#3b82f6;">7+</div><div class="metric-lbl">Years Exp</div></div>
      <div class="metric-card"><div class="metric-val" style="color:#10b981;">113k</div><div class="metric-lbl">Hrs Saved</div></div>
      <div class="metric-card"><div class="metric-val" style="color:#8b5cf6;">2</div><div class="metric-lbl">AI Projects</div></div>
      <div class="metric-card"><div class="metric-val" style="color:#f59e0b;">3</div><div class="metric-lbl">Certs</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<span class="slabel">Navigation</span>', unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["🧑  Portfolio", "🏗️  Architecture", "🔀  AutoRequest Flow"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown('<span class="slabel">Quick Links</span>', unsafe_allow_html=True)

    st.markdown("""
    <a class="qlink qlink-green" href="https://aiworkshop-8dzupftsephfx7iq3xrq9p.streamlit.app/" target="_blank">🚀 Live AI App</a>
    <a class="qlink qlink-red"   href="https://github.com/Charlie2094/AutoRequest-Pro" target="_blank">🐙 AutoRequest Pro</a>
    <a class="qlink qlink-blue"  href="https://www.linkedin.com/in/ashwin-gopal-aa06967b" target="_blank">💼 LinkedIn</a>
    <a class="qlink" href="https://github.com/Charlie2094" target="_blank">🐙 GitHub Profile</a>
    <a class="qlink" href="https://charlie2094.github.io/Ashwin-portfolio/" target="_blank">🌐 Portfolio Site</a>
    """, unsafe_allow_html=True)

    st.markdown("---")

    resume_html = fetch_html(URLS["resume"])
    st.download_button(
        label="⬇️  Download Resume",
        data=resume_html,
        file_name="Ashwin_Gopal_Resume.html",
        mime="text/html",
        use_container_width=True
    )

    st.markdown("""
    <div style="font-size:9.5px;opacity:0.2;text-align:center;margin-top:10px;line-height:1.7;">
    Auto-syncs from GitHub<br/>Updates within 5 mins
    </div>
    """, unsafe_allow_html=True)


# ── MAIN — NO extra header, just render HTML directly ────────

if "Portfolio" in page:
    html = fetch_html(URLS["portfolio"])
    st.components.v1.html(html, height=2400, scrolling=True)

elif "Architecture" in page:
    html = fetch_html(URLS["architecture"])
    st.components.v1.html(html, height=2000, scrolling=True)

elif "AutoRequest" in page:
    html = fetch_html(URLS["flow"])
    st.components.v1.html(html, height=2200, scrolling=True)
