import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ShetiMitra Climate",
    page_icon="🌾",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: #F7F8F2;
}

/* Hero */
.hero {
    background: linear-gradient(120deg, #14532D, #2E7D32, #6BAA45);
    padding: 34px 42px;
    border-radius: 24px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(31, 90, 48, 0.18);
}

.hero-title {
    font-size: 42px;
    font-weight: 700;
    margin: 0;
}

.hero-sub {
    font-size: 17px;
    margin-top: 8px;
    opacity: 0.95;
}

.hero-local {
    font-size: 20px;
    font-weight: 600;
    margin-top: 18px;
}

/* Cards */
.card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #E3E9DD;
    box-shadow: 0 5px 18px rgba(0,0,0,0.05);
    min-height: 175px;
}

.card-green { border-top: 5px solid #3D8B40; }
.card-blue { border-top: 5px solid #3196D2; }
.card-yellow { border-top: 5px solid #E8B923; }
.card-orange { border-top: 5px solid #F28C28; }
.card-purple { border-top: 5px solid #8064A2; }

.card-title {
    font-size: 21px;
    font-weight: 700;
    color: #17351F;
}

.card-text {
    color: #65716A;
    font-size: 14px;
}

/* Voice */
.voice-box {
    background: linear-gradient(135deg, #FFF7D6, #FFFDF1);
    border: 2px solid #F0C84B;
    border-radius: 22px;
    padding: 25px;
    text-align: center;
    margin-bottom: 25px;
}

.voice-icon {
    font-size: 55px;
}

.voice-title {
    font-size: 25px;
    font-weight: 700;
    color: #493A09;
}

/* Section title */
.section-title {
    font-size: 27px;
    font-weight: 700;
    color: #183B22;
    margin-top: 12px;
}

/* Stat */
.stat {
    background: white;
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #E1E7DF;
}

.stat-number {
    font-size: 28px;
    font-weight: 700;
    color: #25753A;
}

.stat-label {
    font-size: 13px;
    color: #68756D;
}

/* Footer */
.footer {
    text-align: center;
    color: #718076;
    padding: 25px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="hero-title">🌾 ShetiMitra Climate</div>
    <div class="hero-sub">
        Climate intelligence in the farmer's own voice.
    </div>
    <div class="hero-local">
        तुमच्या शेतासाठी • तुमच्या भाषेत • तुमच्या आवाजात
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- FARMER CONTEXT ----------
c1, c2, c3 = st.columns([1.5, 1.2, 1.2])

with c1:
    language = st.selectbox(
        "🌐 Language / भाषा",
        ["Marathi", "Hindi", "Telugu", "English"]
    )

with c2:
    location = st.selectbox(
        "📍 Location",
        [
            "Nandurbar, Maharashtra",
            "Nashik, Maharashtra",
            "Nagpur, Maharashtra",
            "Guntur, Andhra Pradesh"
        ]
    )

with c3:
    crop = st.selectbox(
        "🌱 Main Crop",
        ["Cotton", "Soybean", "Wheat", "Chilli"]
    )


# ---------- VOICE ----------
st.markdown("""
<div class="voice-box">
    <div class="voice-icon">🎤</div>
    <div class="voice-title">बोला — ShetiMitra ऐकते</div>
    <p>Ask about weather, crops, schemes or farming information.</p>
</div>
""", unsafe_allow_html=True)

questions = {
    "Marathi": [
        "आज पाऊस पडणार आहे का?",
        "माझ्या कापसासाठी काय काळजी घ्यायची?",
        "माझ्यासाठी कोणती सरकारी योजना आहे?"
    ],
    "Hindi": [
        "आज बारिश होने वाली है क्या?",
        "मेरी कपास की फसल के लिए क्या ध्यान रखना चाहिए?",
        "मेरे लिए कौन सी सरकारी योजना है?"
    ],
    "Telugu": [
        "ఈ రోజు వర్షం పడుతుందా?",
        "నా పత్తి పంటకు ఏమి జాగ్రత్తలు తీసుకోవాలి?",
        "నాకు ఏ ప్రభుత్వ పథకం ఉపయోగపడుతుంది?"
    ],
    "English": [
        "Will it rain today?",
        "What should I watch for in my cotton crop?",
        "Which government scheme may be relevant to me?"
    ]
}

question = st.selectbox(
    "🎙️ What would you like to ask?",
    questions[language]
)

if st.button("🎤 Ask ShetiMitra", type="primary", use_container_width=True):

    if "पाऊस" in question or "बारिश" in question or "వర్షం" in question or "rain" in question.lower():

        if language == "Marathi":
            answer = f"🌦️ {location} साठी आज पावसाची शक्यता आहे. शेतातील निचरा तपासा आणि फवारणीसारख्या कामांपूर्वी स्थानिक हवामानाचा अंदाज तपासा."

        elif language == "Hindi":
            answer = f"🌦️ {location} में आज बारिश की संभावना है। खेत की जल निकासी देखें और स्प्रे जैसे काम से पहले स्थानीय मौसम पूर्वानुमान जांचें."

        elif language == "Telugu":
            answer = f"🌦️ {location} ప్రాంతంలో ఈ రోజు వర్షం అవకాశం ఉంది. పొలంలో నీటి పారుదలను పరిశీలించండి."

        else:
            answer = f"🌦️ Rain is possible around {location}. Check field drainage and verify the local forecast before sensitive farm operations."

    elif "योजना" in question or "पథకం" in question or "scheme" in question.lower():

        if language == "Marathi":
            answer = "🏛️ तुमच्या पीक, जमीन आणि पात्रतेनुसार कृषी योजनांची माहिती तपासता येईल. अर्ज करण्यापूर्वी अधिकृत सरकारी पोर्टलवर पात्रता तपासा."

        elif language == "Hindi":
            answer = "🏛️ आपकी फसल, जमीन और पात्रता के आधार पर कृषि योजनाएं देखी जा सकती हैं। आवेदन से पहले आधिकारिक पोर्टल पर पात्रता जांचें."

        elif language == "Telugu":
            answer = "🏛️ మీ పంట మరియు అర్హత ఆధారంగా వ్యవసాయ పథకాలను పరిశీలించవచ్చు. దరఖాస్తు ముందు అధికారిక పోర్టల్‌ను చూడండి."

        else:
            answer = "🏛️ Agricultural schemes can be filtered using your crop and eligibility. Always verify the latest eligibility and documents on the official government portal."

    else:

        if language == "Marathi":
            answer = f"🌱 {crop} पिकासाठी हवामान, माती आणि पिकाची अवस्था महत्त्वाची आहे. खाली CropMitra मध्ये फोटो तपासा."

        elif language == "Hindi":
            answer = f"🌱 {crop} फसल के लिए मौसम, मिट्टी और फसल की अवस्था महत्वपूर्ण है। नीचे CropMitra में फोटो जांचें."

        elif language == "Telugu":
            answer = f"🌱 {crop} పంటకు వాతావరణం, నేల మరియు పంట దశ ముఖ్యమైనవి. క్రింద CropMitraలో ఫోటోను పరిశీలించండి."

        else:
            answer = f"🌱 For {crop}, local weather, soil and crop stage matter. Use CropMitra below for a preliminary image check."

    st.success(answer)


# ---------- WEATHER ----------
st.markdown('<div class="section-title">🌦️ Today's Climate Snapshot</div>',
            unsafe_allow_html=True)

w1, w2, w3, w4 = st.columns(4)

with w1:
    st.markdown("""
    <div class="stat">
    <div class="stat-number">28°C</div>
    <div class="stat-label">Temperature</div>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown("""
    <div class="stat">
    <div class="stat-number">68%</div>
    <div class="stat-label">Rain Probability</div>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown("""
    <div class="stat">
    <div class="stat-number">14 km/h</div>
    <div class="stat-label">Wind</div>
    </div>
    """, unsafe_allow_html=True)

with w4:
    st.markdown("""
    <div class="stat">
    <div class="stat-number">72%</div>
    <div class="stat-label">Humidity</div>
    </div>
    """, unsafe_allow_html=True)


st.divider()


# ---------- TOOLS ----------
st.markdown('<div class="section-title">🌾 Farmer Tools</div>',
            unsafe_allow_html=True)

a, b, c = st.columns(3)

with a:
    st.markdown("""
    <div class="card card-green">
        <div class="card-title">🌱 CropMitra</div>
        <div class="card-text">
        Upload a crop image for a preliminary visual check.
        </div>
    </div>
    """, unsafe_allow_html=True)

    crop_image = st.file_uploader(
        "📷 Upload crop photo",
        type=["jpg", "jpeg", "png"]
    )

    if crop_image:
        image = Image.open(crop_image)
        st.image(image, use_container_width=True)

        if st.button("🔎 Check Crop"):
            st.warning(
                "Possible crop stress detected. "
                "This is a preliminary AI check — confirm serious crop problems with an agricultural expert."
            )


with b:
    st.markdown("""
    <div class="card card-yellow">
        <div class="card-title">🏛️ YojanaMitra</div>
        <div class="card-text">
        Understand agricultural schemes, eligibility and required documents.
        </div>
    </div>
    """, unsafe_allow_html=True)

    scheme = st.selectbox(
        "Choose a category",
        [
            "Crop Insurance",
            "Irrigation Support",
            "Farm Equipment",
            "Income Support"
        ]
    )

    st.info(
        f"Demo: Showing verified information for **{scheme}**. "
        "Final eligibility should be checked on the official government portal."
    )


with c:
    st.markdown("""
    <div class="card card-blue">
        <div class="card-title">📄 KagadMitra</div>
        <div class="card-text">
        Show a farming document and understand what it means.
        </div>
    </div>
    """, unsafe_allow_html=True)

    document = st.file_uploader(
        "📄 Upload document",
        type=["jpg", "jpeg", "png", "pdf"]
    )

    if document:
        st.success("Document received.")
        st.write(
            "Demo: ShetiMitra would extract the document, "
            "identify important dates/actions and explain them in the selected language."
        )


# ---------- IMPACT ----------
st.divider()

st.markdown('<div class="section-title">🌍 Why ShetiMitra?</div>',
            unsafe_allow_html=True)

i1, i2, i3, i4 = st.columns(4)

impact = [
    ("🎤", "Voice First", "No complicated typing"),
    ("🌐", "Local Languages", "Marathi • Hindi • Telugu"),
    ("🌦️", "Climate Aware", "Understand weather risks"),
    ("👨‍🌾", "Farmer Focused", "Simple actionable information")
]

for col, (icon, title, text) in zip([i1, i2, i3, i4], impact):
    with col:
        st.markdown(f"""
        <div class="card card-purple">
            <div style="font-size:30px">{icon}</div>
            <div class="card-title">{title}</div>
            <div class="card-text">{text}</div>
        </div>
        """, unsafe_allow_html=True)


st.markdown("""
<div class="footer">
🌾 <b>ShetiMitra Climate</b> • Climate intelligence in the farmer's own voice.<br>
Prototype for SANKALP by Satin Finserv — Climate Edition
</div>
""", unsafe_allow_html=True)
