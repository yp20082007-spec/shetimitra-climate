import streamlit as st
from PIL import Image

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ShetiMitra Climate",
    page_icon="🌾",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: #F7F8F2;
}

/* HERO */

.hero {
    background: linear-gradient(
        120deg,
        #14532D,
        #2E7D32,
        #7CB342
    );
    padding: 35px 42px;
    border-radius: 25px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(0, 80, 30, 0.18);
}

.hero-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.hero-subtitle {
    font-size: 18px;
    margin-top: 5px;
}

.hero-marathi {
    font-size: 21px;
    font-weight: 600;
    margin-top: 18px;
}

/* VOICE BOX */

.voice-box {
    background: linear-gradient(
        135deg,
        #FFF4C2,
        #FFFBE8
    );
    border: 2px solid #E8B923;
    border-radius: 22px;
    padding: 25px;
    text-align: center;
    margin: 25px 0;
}

.voice-icon {
    font-size: 52px;
}

.voice-title {
    font-size: 25px;
    font-weight: 700;
    color: #4A3A00;
}

/* SECTION */

.section-title {
    font-size: 27px;
    font-weight: 700;
    color: #183B22;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* CARDS */

.card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    min-height: 165px;
    border: 1px solid #E1E8DD;
    box-shadow: 0 5px 18px rgba(0, 0, 0, 0.05);
}

.green-card {
    border-top: 5px solid #4CAF50;
}

.blue-card {
    border-top: 5px solid #2196F3;
}

.yellow-card {
    border-top: 5px solid #FFC107;
}

.orange-card {
    border-top: 5px solid #FF8A00;
}

.purple-card {
    border-top: 5px solid #7E57C2;
}

.card-title {
    font-size: 21px;
    font-weight: 700;
    color: #17351F;
}

.card-text {
    color: #68756D;
    font-size: 14px;
    margin-top: 8px;
}

/* WEATHER STAT */

.stat {
    background: white;
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid #E1E7DF;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}

.stat-number {
    font-size: 27px;
    font-weight: 700;
    color: #287A3D;
}

.stat-label {
    font-size: 13px;
    color: #68756D;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #68756D;
    padding: 30px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown("""
<div class="hero">

    <div class="hero-title">
        🌾 ShetiMitra Climate
    </div>

    <div class="hero-subtitle">
        Climate intelligence for farmers
    </div>

    <div class="hero-marathi">
        तुमच्या शेतासाठी • तुमच्या भाषेत • तुमच्या आवाजात
    </div>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FARMER INFORMATION
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    language = st.selectbox(
        "🌐 Language / भाषा",
        [
            "Marathi",
            "Hindi",
            "Telugu",
            "English"
        ]
    )

with col2:

    location = st.selectbox(
        "📍 Location",
        [
            "Nandurbar, Maharashtra",
            "Nashik, Maharashtra",
            "Nagpur, Maharashtra",
            "Guntur, Andhra Pradesh"
        ]
    )

with col3:

    crop = st.selectbox(
        "🌱 Main Crop",
        [
            "Cotton",
            "Soybean",
            "Wheat",
            "Chilli"
        ]
    )


# --------------------------------------------------
# VOICE ASSISTANT
# --------------------------------------------------

st.markdown("""
<div class="voice-box">

    <div class="voice-icon">
        🎤
    </div>

    <div class="voice-title">
        बोला — ShetiMitra ऐकते
    </div>

    <p>
        Ask about weather, crops, schemes or farming information.
    </p>

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
    "🎙️ Farmer question",
    questions[language]
)


if st.button(
    "🎤 Ask ShetiMitra",
    type="primary",
    use_container_width=True
):

    # WEATHER QUESTION

    if (
        "पाऊस" in question
        or "बारिश" in question
        or "వర్షం" in question
        or "rain" in question.lower()
    ):

        if language == "Marathi":

            answer = (
                f"🌦️ {location} परिसरात आज पावसाची शक्यता आहे. "
                "शेतातील निचरा तपासा आणि फवारणीसारख्या कामांपूर्वी "
                "स्थानिक हवामानाचा अंदाज तपासा."
            )

        elif language == "Hindi":

            answer = (
                f"🌦️ {location} में आज बारिश की संभावना है। "
                "खेत की जल निकासी देखें और स्प्रे जैसे काम से पहले "
                "स्थानीय मौसम पूर्वानुमान जांचें।"
            )

        elif language == "Telugu":

            answer = (
                f"🌦️ {location} ప్రాంతంలో ఈ రోజు వర్షం అవకాశం ఉంది. "
                "పొలంలో నీటి పారుదలను పరిశీలించండి మరియు వ్యవసాయ పనికి "
                "ముందు స్థానిక వాతావరణ సూచనను చూడండి."
            )

        else:

            answer = (
                f"🌦️ Rain is possible around {location}. "
                "Check field drainage and verify the local forecast "
                "before sensitive farm operations."
            )


    # GOVERNMENT SCHEME QUESTION

    elif (
        "योजना" in question
        or "పథకం" in question
        or "scheme" in question.lower()
    ):

        if language == "Marathi":

            answer = (
                "🏛️ तुमच्या पीक, जमीन आणि पात्रतेनुसार "
                "कृषी योजनांची माहिती तपासता येईल. "
                "अर्ज करण्यापूर्वी अधिकृत सरकारी पोर्टलवर "
                "पात्रता आणि कागदपत्रे तपासा."
            )

        elif language == "Hindi":

            answer = (
                "🏛️ आपकी फसल, जमीन और पात्रता के आधार पर "
                "कृषि योजनाएं देखी जा सकती हैं। "
                "आवेदन से पहले आधिकारिक सरकारी पोर्टल पर "
                "पात्रता और दस्तावेज जांचें।"
            )

        elif language == "Telugu":

            answer = (
                "🏛️ మీ పంట, భూమి మరియు అర్హత ఆధారంగా "
                "వ్యవసాయ పథకాలను చూడవచ్చు. "
                "దరఖాస్తు ముందు అధికారిక ప్రభుత్వ పోర్టల్‌లో "
                "అర్హతను పరిశీలించండి."
            )

        else:

            answer = (
                "🏛️ Agricultural schemes can be filtered using "
                "your crop and eligibility. Always verify the "
                "latest eligibility and documents on the official "
                "government portal."
            )


    # CROP QUESTION

    else:

        if language == "Marathi":

            answer = (
                f"🌱 {crop} पिकासाठी हवामान, माती आणि पिकाची "
                "अवस्था महत्त्वाची आहे. खाली CropMitra मध्ये "
                "फोटो तपासा."
            )

        elif language == "Hindi":

            answer = (
                f"🌱 {crop} फसल के लिए मौसम, मिट्टी और फसल की "
                "अवस्था महत्वपूर्ण है। नीचे CropMitra में "
                "फोटो जांचें."
            )

        elif language == "Telugu":

            answer = (
                f"🌱 {crop} పంటకు వాతావరణం, నేల మరియు పంట దశ "
                "ముఖ్యమైనవి. క్రింద CropMitraలో ఫోటోను పరిశీలించండి."
            )

        else:

            answer = (
                f"🌱 For {crop}, local weather, soil and crop "
                "stage matter. Use CropMitra below for a "
                "preliminary image check."
            )


    st.success(answer)


# --------------------------------------------------
# WEATHER
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🌦️ Today\'s Climate Snapshot</div>',
    unsafe_allow_html=True
)


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
        <div class="stat-label">Wind Speed</div>
    </div>
    """, unsafe_allow_html=True)


with w4:

    st.markdown("""
    <div class="stat">
        <div class="stat-number">72%</div>
        <div class="stat-label">Humidity</div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# FARMER TOOLS
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">🌾 ShetiMitra Tools</div>',
    unsafe_allow_html=True
)


tool1, tool2, tool3 = st.columns(3)


# --------------------------------------------------
# CROP MITRA
# --------------------------------------------------

with tool1:

    st.markdown("""
    <div class="card green-card">

        <div class="card-title">
            🌱 CropMitra
        </div>

        <div class="card-text">
            Upload a crop image for a preliminary
            visual health check.
        </div>

    </div>
    """, unsafe_allow_html=True)

    crop_image = st.file_uploader(
        "📷 Upload crop photo",
        type=["jpg", "jpeg", "png"]
    )

    if crop_image:

        image = Image.open(crop_image)

        st.image(
            image,
            use_container_width=True
        )

        if st.button("🔎 Check Crop"):

            st.warning(
                "Possible crop stress detected. "
                "This is a preliminary AI check. "
                "For serious crop problems, confirm "
                "the issue with an agricultural expert."
            )


# --------------------------------------------------
# YOJANA MITRA
# --------------------------------------------------

with tool2:

    st.markdown("""
    <div class="card yellow-card">

        <div class="card-title">
            🏛️ YojanaMitra
        </div>

        <div class="card-text">
            Understand agricultural schemes,
            eligibility and required documents.
        </div>

    </div>
    """, unsafe_allow_html=True)

    scheme = st.selectbox(
        "Select a scheme category",
        [
            "Crop Insurance",
            "Irrigation Support",
            "Farm Equipment",
            "Income Support"
        ]
    )

    st.info(
        f"Demo information for: {scheme}. "
        "Final eligibility should be verified "
        "on the official government portal."
    )


# --------------------------------------------------
# KAGAD MITRA
# --------------------------------------------------

with tool3:

    st.markdown("""
    <div class="card blue-card">

        <div class="card-title">
            📄 KagadMitra
        </div>

        <div class="card-text">
            Upload a farming document and understand
            what it means.
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
            "Demo: ShetiMitra would extract important "
            "information, identify dates and actions, "
            "and explain the document in the selected language."
        )


# --------------------------------------------------
# IMPACT
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="section-title">🌍 Why ShetiMitra?</div>',
    unsafe_allow_html=True
)


i1, i2, i3, i4 = st.columns(4)


impact = [

    (
        "🎤",
        "Voice First",
        "No complicated typing"
    ),

    (
        "🌐",
        "Local Languages",
        "Marathi • Hindi • Telugu"
    ),

    (
        "🌦️",
        "Climate Aware",
        "Understand weather risks"
    ),

    (
        "👨‍🌾",
        "Farmer Focused",
        "Simple useful information"
    )
]


for col, item in zip(
    [i1, i2, i3, i4],
    impact
):

    icon, title, description = item

    with col:

        st.markdown(
            f"""
            <div class="card purple-card">

                <div style="font-size:32px">
                    {icon}
                </div>

                <div class="card-title">
                    {title}
                </div>

                <div class="card-text">
                    {description}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

🌾 <b>ShetiMitra Climate</b>

<br>

Climate intelligence in the farmer's own voice.

<br><br>

Prototype for SANKALP by Satin Finserv — Climate Edition

</div>
""", unsafe_allow_html=True)
