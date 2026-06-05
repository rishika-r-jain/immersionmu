import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Mahindra University | School of Management",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        padding: 50px 40px;
        border-radius: 24px;
        background: linear-gradient(135deg, #7b1113, #1f2937);
        color: white;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 52px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 20px;
        line-height: 1.6;
        max-width: 900px;
    }

    .section-title {
        font-size: 30px;
        font-weight: 750;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #1f2937;
    }

    .card {
        background-color: white;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        min-height: 180px;
    }

    .card h3 {
        color: #7b1113;
        margin-bottom: 10px;
    }

    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.07);
    }

    .footer {
        margin-top: 40px;
        padding: 24px;
        text-align: center;
        background-color: #1f2937;
        color: white;
        border-radius: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("School of Management")
st.sidebar.markdown("**Mahindra University, Hyderabad**")
st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")
st.sidebar.markdown("- About")
st.sidebar.markdown("- Programs")
st.sidebar.markdown("- Learning Approach")
st.sidebar.markdown("- Contact")

# -----------------------------
# Hero Section
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <h1>Hello World 👋</h1>
        <h2>Welcome to Mahindra University School of Management</h2>
        <p>
        A new-age management school designed to prepare students for leadership in a fast-changing,
        technology-driven business environment. The School of Management blends business fundamentals,
        analytics, digital thinking, strategic decision-making, and interdisciplinary learning.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Intro Section
# -----------------------------
st.markdown('<div class="section-title">About the School</div>', unsafe_allow_html=True)

st.write(
    """
    The **School of Management at Mahindra University** focuses on developing future-ready business
    professionals who can operate at the intersection of management, technology, economics, analytics,
    entrepreneurship, and responsible leadership.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Business Foundations</h3>
            <p>
            Strong grounding in management, economics, finance, marketing, strategy,
            entrepreneurship, and decision-making.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>Technology Orientation</h3>
            <p>
            Emphasis on digital technologies, analytics, computational business thinking,
            and practical problem-solving.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>Industry Relevance</h3>
            <p>
            Designed to connect classroom learning with managerial practice, innovation,
            and emerging business challenges.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Programs Section
# -----------------------------
st.markdown('<div class="section-title">Programs Offered</div>', unsafe_allow_html=True)

programs = [
    "BBA",
    "BBA in Digital Technologies",
    "BBA in Computational Business Analytics",
    "BBA in Applied Economics & Finance",
    "BBA in Entrepreneurship & Family Business",
    "BBA in Infrastructure Management",
    "MBA",
    "Ph.D. Programmes in Management and allied areas"
]

for program in programs:
    st.markdown(f"✅ {program}")

# -----------------------------
# Learning Approach
# -----------------------------
st.markdown('<div class="section-title">Learning Approach</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Interdisciplinary", "Applied", "Future-Ready"])

with tab1:
    st.write(
        """
        The School encourages students to combine management education with economics,
        finance, technology, analytics, and social science perspectives.
        """
    )

with tab2:
    st.write(
        """
        Students are expected to learn through projects, cases, business problem-solving,
        data-driven analysis, and managerial decision-making exercises.
        """
    )

with tab3:
    st.write(
        """
        The curriculum orientation supports careers in digital business, analytics,
        entrepreneurship, consulting, finance, marketing, and technology-led management roles.
        """
    )

# -----------------------------
# Highlights
# -----------------------------
st.markdown('<div class="section-title">Why Mahindra University School of Management?</div>', unsafe_allow_html=True)

h1, h2, h3, h4 = st.columns(4)

with h1:
    st.markdown(
        """
        <div class="metric-card">
            <h2>01</h2>
            <p>New-age management education</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with h2:
    st.markdown(
        """
        <div class="metric-card">
            <h2>02</h2>
            <p>Technology-integrated curriculum</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with h3:
    st.markdown(
        """
        <div class="metric-card">
            <h2>03</h2>
            <p>Interdisciplinary business learning</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with h4:
    st.markdown(
        """
        <div class="metric-card">
            <h2>04</h2>
            <p>Hyderabad-based university campus</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Call to Action
# -----------------------------
st.markdown('<div class="section-title">Explore More</div>', unsafe_allow_html=True)

st.info(
    """
    Interested students can explore undergraduate, postgraduate, and doctoral opportunities
    through Mahindra University's official admissions and School of Management pages.
    """
)

if st.button("Visit Mahindra University Website"):
    st.markdown("https://www.mahindrauniversity.edu.in/")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div class="footer">
        <h3>Mahindra University School of Management</h3>
        <p>Survey No: 62/1A, Bahadurpally, Jeedimetla, Hyderabad – 500043, Telangana, India</p>
        <p>Built with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)