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
    "portfolio":     f"{BASE}/ashwin_gopal_portfolio.html",
    "architecture":  f"{BASE}/ashwin_architecture.html",
    "flow":          f"{BASE}/autorequest_flow.html",
    "resume":        f"{BASE}/ashwin_gopal_resume.html",
}

# ── FETCH HTML FROM GITHUB ───────────────────────────────────
@st.cache_data(ttl=300)  # Refresh every 5 minutes
def fetch_html(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"<h2 style='color:red;padding:40px;'>Failed to load: {e}</h2>"

# ── CUSTOM CSS ───────────────────────────────────────────────
st.markdown("""
<style>
  /* Hide default Streamlit elements */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }

  /* Sidebar styling */
  [data-testid="stSidebar"] {
    background: #1e2130 !important;
    border-right: 1px solid rgba(255,255,255,0.08) !important;
  }
  [data-testid="stSidebar"] * { color: white !important; }

  /* Profile card */
  .profile-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;
    text-align: center;
  }
  .profile-avatar {
    width: 64px; height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, #e94560, #8b5cf6);
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; font-weight: 800;
    margin: 0 auto 10px;
    color: white;
  }
  .profile-name { font-size: 15px; font-weight: 700; color: white; }
  .profile-role { font-size: 11px; color: rgba(255,255,255,0.5); margin-top: 3px; }
  .online-badge {
    display: inline-block;
    background: rgba(16,185,129,0.2);
    color: #10b981;
    font-size: 10px; font-weight: 700;
    padding: 2px 10px; border-radius: 20px;
    margin-top: 8px;
    border: 1px solid rgba(16,185,129,0.3);
  }

  /* Metric cards */
  .metric-row {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    margin-bottom: 16px;
  }
  .metric-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 12px;
    text-align: center;
  }
  .metric-val {
    font-size: 20px; font-weight: 800;
    line-height: 1;
  }
  .metric-lbl {
    font-size: 10px;
    color: rgba(255,255,255,0.4);
    margin-top: 3px;
  }

  /* Link buttons */
  .link-btn {
    display: flex; align-items: center; gap: 8px;
    padding: 8px 14px; border-radius: 8px;
    font-size: 12px; font-weight: 600;
    text-decoration: none;
    margin-bottom: 6px;
    transition: opacity 0.2s;
    border: 1px solid rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.75) !important;
    background: rgba(255,255,255,0.05);
  }
  .link-btn:hover { opacity: 0.75; }
  .link-btn-green {
    background: rgba(16,185,129,0.12) !important;
    border-color: rgba(16,185,129,0.3) !important;
    color: #10b981 !important;
  }
  .link-btn-blue {
    background: rgba(59,130,246,0.12) !important;
    border-color: rgba(59,130,246,0.3) !important;
    color: #60a5fa !important;
  }
  .link-btn-red {
    background: rgba(233,69,96,0.12) !important;
    border-color: rgba(233,69,96,0.3) !important;
    color: #ff7d94 !important;
  }

  /* Section label */
  .sidebar-section {
    font-size: 9.5px; font-weight: 700;
    text-transform: uppercase; letter-spacing: 1.5px;
    color: rgba(255,255,255,0.25) !important;
    padding: 4px 0 6px;
  }

  /* iFrame container */
  .iframe-container {
    width: 100%;
    border-radius: 0;
    overflow: hidden;
    border: none;
  }

  /* Streamlit radio as nav — hide default */
  div[data-testid="stRadio"] > label { display: none; }
  div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex; flex-direction: column; gap: 4px;
  }
  div[data-testid="stRadio"] label {
    background: transparent !important;
    border: none !important;
    padding: 8px 12px !important;
    border-radius: 8px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    color: rgba(255,255,255,0.6) !important;
    cursor: pointer !important;
  }
  div[data-testid="stRadio"] label:hover {
    background: rgba(255,255,255,0.06) !important;
    color: white !important;
  }
  div[data-testid="stRadio"] label[data-checked="true"] {
    background: rgba(233,69,96,0.15) !important;
    color: #ff7d94 !important;
    border: 1px solid rgba(233,69,96,0.25) !important;
  }

  /* Download button */
  .stDownloadButton button {
    width: 100% !important;
    background: linear-gradient(135deg, #e94560, #c41d3c) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    padding: 10px !important;
  }

  /* Page header */
  .page-header {
    background: linear-gradient(135deg, #1a1a2e, #0f3460);
    padding: 20px 32px 18px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
  }
  .page-header-title {
    font-size: 18px; font-weight: 800;
    color: white; margin-bottom: 3px;
  }
  .page-header-sub {
    font-size: 12.5px; color: rgba(255,255,255,0.45);
  }
  .page-header-tags {
    display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap;
  }
  .page-tag {
    font-size: 11px; font-weight: 600;
    padding: 3px 12px; border-radius: 20px;
    background: rgba(255,255,255,0.08);
    color: rgba(255,255,255,0.6);
  }
  .page-tag-green { background: rgba(16,185,129,0.15); color: #10b981; }
  .page-tag-blue  { background: rgba(59,130,246,0.15); color: #60a5fa; }
  .page-tag-red   { background: rgba(233,69,96,0.15);  color: #ff7d94; }
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR ──────────────────────────────────────────────────
with st.sidebar:

    # Profile card
    st.markdown("""
    <div class="profile-card">
      <div class="profile-avatar">AG</div>
      <div class="profile-name">Ashwin Gopal</div>
      <div class="profile-role">Senior Automation Developer</div>
      <div class="profile-role" style="margin-top:2px;">WPP Production · Chennai</div>
      <div class="online-badge">⚡ Open to Opportunities</div>
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    st.markdown("""
    <div class="metric-row">
      <div class="metric-card">
        <div class="metric-val" style="color:#3b82f6;">7+</div>
        <div class="metric-lbl">Years Exp</div>
      </div>
      <div class="metric-card">
        <div class="metric-val" style="color:#10b981;">113k</div>
        <div class="metric-lbl">Hrs/yr Saved</div>
      </div>
      <div class="metric-card">
        <div class="metric-val" style="color:#8b5cf6;">2</div>
        <div class="metric-lbl">AI Projects</div>
      </div>
      <div class="metric-card">
        <div class="metric-val" style="color:#f59e0b;">3</div>
        <div class="metric-lbl">Certs</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-section">Navigation</div>', unsafe_allow_html=True)

    # Navigation
    page = st.radio(
        "nav",
        ["🧑  Portfolio", "🏗️  Architecture", "🔀  AutoRequest Flow"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown('<div class="sidebar-section">Quick Links</div>', unsafe_allow_html=True)

    # Quick links
    st.markdown("""
    <a class="link-btn link-btn-green" href="https://aiworkshop-8dzupftsephfx7iq3xrq9p.streamlit.app/" target="_blank">🚀 Live AI App</a>
    <a class="link-btn link-btn-red" href="https://github.com/Charlie2094/AutoRequest-Pro" target="_blank">🐙 AutoRequest Pro</a>
    <a class="link-btn link-btn-blue" href="https://www.linkedin.com/in/ashwin-gopal-aa06967b" target="_blank">💼 LinkedIn</a>
    <a class="link-btn" href="https://github.com/Charlie2094" target="_blank">🐙 GitHub Profile</a>
    <a class="link-btn" href="https://charlie2094.github.io/Ashwin-portfolio/" target="_blank">🌐 Portfolio Site</a>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Download resume button
    resume_html = fetch_html(URLS["resume"])
    st.download_button(
        label="⬇️  Download Resume",
        data=resume_html,
        file_name="Ashwin_Gopal_Resume.html",
        mime="text/html",
        use_container_width=True
    )

    st.markdown("""
    <div style="font-size:10px; color:rgba(255,255,255,0.2); text-align:center; margin-top:12px; line-height:1.6;">
    Auto-syncs from GitHub<br/>
    Updates within 5 mins of push
    </div>
    """, unsafe_allow_html=True)


# ── MAIN CONTENT ─────────────────────────────────────────────

# Page: Portfolio
if "Portfolio" in page:
    st.markdown("""
    <div class="page-header">
      <div class="page-header-title">🧑 Portfolio</div>
      <div class="page-header-sub">Projects · Skills · Experience · Certifications</div>
      <div class="page-header-tags">
        <span class="page-tag page-tag-green">✅ Open to Opportunities</span>
        <span class="page-tag page-tag-blue">📍 Chennai, India</span>
        <span class="page-tag">gopal2ashwin@gmail.com</span>
        <span class="page-tag">+91 9790964452</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    html = fetch_html(URLS["portfolio"])
    st.components.v1.html(html, height=900, scrolling=True)

# Page: Architecture
elif "Architecture" in page:
    st.markdown("""
    <div class="page-header">
      <div class="page-header-title">🏗️ Architecture</div>
      <div class="page-header-sub">Power Platform AI · Agentic AI · System Design</div>
      <div class="page-header-tags">
        <span class="page-tag page-tag-red">⚡ Power Platform AI</span>
        <span class="page-tag page-tag-blue">🤖 Agentic AI</span>
        <span class="page-tag">LLaMA 3 · Groq · ReAct</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    html = fetch_html(URLS["architecture"])
    st.components.v1.html(html, height=900, scrolling=True)

# Page: AutoRequest Flow
elif "AutoRequest" in page:
    st.markdown("""
    <div class="page-header">
      <div class="page-header-title">🔀 AutoRequest Pro — Flow Diagram</div>
      <div class="page-header-sub">Power Automate · 9-Step Flow · Phase 1 Live · Phase 2 In Dev · Phase 3 Planned</div>
      <div class="page-header-tags">
        <span class="page-tag page-tag-green">✅ Phase 1 Live</span>
        <span class="page-tag" style="color:#f59e0b;">🔧 Phase 2 In Dev</span>
        <span class="page-tag page-tag-blue">🔮 Phase 3 Planned</span>
        <a class="page-tag page-tag-red" href="https://github.com/Charlie2094/AutoRequest-Pro" target="_blank" style="text-decoration:none;">🐙 GitHub</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    html = fetch_html(URLS["flow"])
    st.components.v1.html(html, height=900, scrolling=True)
