
import streamlit as st
from PIL import Image

st.set_page_config(page_title="ShetiMitra Climate", page_icon="🌾", layout="wide")

# ---------- Styling ----------
st.markdown("""
<style>
    .main {background: #f6fbf5;}
    .hero {
        padding: 28px;
        border-radius: 22px;
        background: linear-gradient(135deg,#1f7a45,#6aa84f);
        color: white;
        margin-bottom: 20px;
    }
    .hero h1 {font-size: 42px; margin-bottom: 5px;}
    .hero p {font-size: 18px;}
    .card {
        background: white;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #dce9dc;
        min-height: 150px;
        box-shadow: 0 3px 12px rgba(0,0,0,.04);
    }
    .small {color:#55705b; font-size:14px;}
    .answer {
        background:#eef8ed;
        border-left:5px solid #2e8b57;
        padding:16px;
        border-radius:10px;
        margin-top:10px;
    }
</style>
""", unsafe_allow_html=True)

if "lang" not in st.session_state:
    st.session_state.lang = "Marathi"

# ---------- Header ----------
st.markdown("""
<div class="hero">
<h1>🌾 ShetiMitra Climate</h1>
<p>Climate intelligence in the farmer's own voice.</p>
<p><b>बोला • दाखवा • समजा • निर्णयासाठी माहिती मिळवा</b></p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([2,1,1])
with c1:
    lang = st.selectbox("🌐 भाषा / Language",
                        ["Marathi","Hindi","Telugu","English"],
                        index=["Marathi","Hindi","Telugu","English"].index(st.session_state.lang))
    st.session_state.lang = lang
with c2:
    district = st.selectbox("📍 Location", ["Nandurbar, Maharashtra","Nashik, Maharashtra","Nagpur, Maharashtra","Guntur, Andhra Pradesh"])
with c3:
    crop = st.selectbox("🌱 Main Crop", ["Cotton","Soybean","Wheat","Chilli"])

st.divider()

# ---------- Voice assistant ----------
st.subheader("🎤 Ask ShetiMitra")
st.caption("Demo mode: type what a farmer would normally say by voice.")

queries = {
    "Marathi": [
        "आज पाऊस पडणार आहे का?",
        "माझ्या कापसासाठी काय काळजी घ्यायची?",
        "माझ्यासाठी कोणती योजना आहे?"
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

q = st.selectbox("Choose a sample farmer question", queries[lang])
if st.button("🤖 Ask ShetiMitra", type="primary"):
    if "rain" in q.lower() or "पाऊस" in q or "बारिश" in q or "వర్షం" in q:
        answers = {
            "Marathi": f"आज {district} परिसरात पावसाची शक्यता आहे. शेतातील निचरा तपासा आणि फवारणी/शेतीचे काम करण्यापूर्वी स्थानिक हवामानाचा अंदाज तपासा.",
            "Hindi": f"आज {district} क्षेत्र में बारिश की संभावना है। खेत की जल निकासी देखें और स्प्रे या अन्य काम से पहले स्थानीय मौसम पूर्वानुमान जांचें.",
            "Telugu": f"ఈ రోజు {district} ప్రాంతంలో వర్షం అవకాశం ఉంది. పొలంలో నీటి పారుదల పరిస్థితిని పరిశీలించి, వ్యవసాయ పనికి ముందు స్థానిక వాతావరణ సూచనను చూడండి.",
            "English": f"Rain is possible around {district} today. Check field drainage and verify the local forecast before spraying or carrying out sensitive farm operations."
        }
    elif "योजना" in q or "scheme" in q.lower() or "పథకం" in q:
        answers = {
            "Marathi": "तुमच्या पिक, जमीन आणि पात्रतेनुसार कृषी योजनांची यादी तपासता येईल. अंतिम अर्ज करण्यापूर्वी अधिकृत सरकारी पोर्टलवरील पात्रता आणि कागदपत्रे तपासा.",
            "Hindi": "आपकी फसल, जमीन और पात्रता के आधार पर कृषि योजनाएं देखी जा सकती हैं। आवेदन से पहले आधिकारिक सरकारी पोर्टल पर पात्रता और दस्तावेज़ जांचें.",
            "Telugu": "మీ పంట, భూమి మరియు అర్హత ఆధారంగా వ్యవసాయ పథకాలను చూడవచ్చు. దరఖాస్తు ముందు అధికారిక ప్రభుత్వ పోర్టల్‌లో అర్హతను పరిశీలించండి.",
            "English": "Relevant agricultural schemes can be filtered using your crop, land and eligibility details. Verify eligibility and documents on the official government portal before applying."
        }
    else:
        answers = {
            "Marathi": f"{crop} पिकासाठी स्थानिक हवामान, मातीची स्थिती आणि पिकाची अवस्था लक्षात घेणे महत्त्वाचे आहे. खालील Crop Health tool मधून फोटो तपासा.",
            "Hindi": f"{crop} फसल के लिए स्थानीय मौसम, मिट्टी और फसल की अवस्था को ध्यान में रखना जरूरी है। नीचे Crop Health tool में फोटो जांचें.",
            "Telugu": f"{crop} పంటకు స్థానిక వాతావరణం, నేల పరిస్థితి మరియు పంట దశను గమనించడం ముఖ్యం. క్రింద Crop Health టూల్‌లో ఫోటోను పరిశీలించండి.",
            "English": f"For {crop}, local weather, soil conditions and crop stage matter. Use the Crop Health tool below for an image-based first check."
        }
    st.markdown(f'<div class="answer"><b>ShetiMitra:</b><br>{answers[lang]}</div>', unsafe_allow_html=True)

# ---------- Feature cards ----------
st.divider()
st.subheader("🌾 ShetiMitra Tools")
a,b,c = st.columns(3)
with a:
    st.markdown('<div class="card"><h3>🌦️ ClimateMitra</h3><p>Weather information explained in simple farmer-friendly language.</p></div>', unsafe_allow_html=True)
    st.metric("Rain probability", "68%")
    st.metric("Temperature", "28°C")
with b:
    st.markdown('<div class="card"><h3>🌱 CropMitra</h3><p>Upload a crop image for a preliminary visual check.</p></div>', unsafe_allow_html=True)
    uploaded = st.file_uploader("📷 Upload crop photo", type=["jpg","jpeg","png"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded crop image", use_container_width=True)
        if st.button("🔎 Analyze crop image"):
            st.success("Demo result: Possible leaf stress detected. This is a preliminary AI check, not a confirmed diagnosis.")
            st.info("For serious crop damage, verify the issue with a qualified agricultural expert.")
with c:
    st.markdown('<div class="card"><h3>🏛️ YojanaMitra</h3><p>Understand agricultural schemes, eligibility and required documents.</p></div>', unsafe_allow_html=True)
    scheme = st.selectbox("Example scheme category", ["Crop insurance","Irrigation support","Farm equipment support","Income support"])
    st.write("**Demo output:**")
    st.write(f"Selected: {scheme}")
    st.write("Eligibility and application steps would be fetched from verified official sources.")

# ---------- Document explainer ----------
st.divider()
st.subheader("📄 KagadMitra — Understand a farming document")
doc = st.file_uploader("Upload a notice, bill or agriculture document", type=["jpg","jpeg","png","pdf"], key="doc")
if doc:
    st.success("Document received.")
    st.info("Demo: ShetiMitra would extract the document text, identify the purpose, deadline and required action, then explain it in the selected local language.")

st.caption("Prototype concept • ShetiMitra Climate • Designed for climate-smart agriculture")
