import streamlit as st
from langchain_helper import generate_restaurant_plan
st.set_page_config(page_title="Restaurant Business Planner", page_icon="appicon.png", layout="wide")
from PIL import Image
import streamlit as st

st.markdown("""
<style>
/* ======== BODY & MAIN FONT ======== */
body {
    background-color: #f8f8f8;
    font-family: 'Helvetica', sans-serif;
}

/* ======== HEADER IMAGE ======== */
.header-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 80%;    /* Adjust image width */
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
}

/* ======== TITLE & CAPTION ======== */
h1 {
    color: #ff4b4b;
    font-size: 3rem !important;  /* Bigger title */
    text-align: center;
    font-weight: 800;
}

.caption-text {
    font-size: 1.3rem;
    color: #333;
    text-align: center;
}

/* ======== SIDEBAR ======== */
[data-testid="stSidebar"] {
    background-color: #f0f0f0;
    color: #333;
    font-size: 1.1rem;
}
[data-testid="stSidebar"] h2 {
    color: #ff4b4b;
    font-size: 1.5rem;
    font-weight: 700;
}

/* ======== BUTTON STYLE ======== */
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
.stButton>button:hover {
    background-color: #ff6666;
}
</style>
""", unsafe_allow_html=True)

# Open image
img = Image.open("restaurent_banner.png")

# Resize image (width, height) -> example: width 600px, height 300px
img_resized = img.resize((1200, 600))
st.image(img_resized)



st.markdown('<h1>Restaurant Business Planner</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption-text">Plan your restaurant business with AI-powered suggestions for names, menu, locations & staff.</p>', unsafe_allow_html=True)




st.sidebar.header("Configuration")
cuisine = st.sidebar.selectbox("Select Cuisine",["Indian", "Italian", "Chinese", "Arabic", "Mexican"])
scale = st.sidebar.selectbox("Select Scale of Restaurant",["Street Style", "Small Restaurant", "Large Restaurant"])
location = st.text_input("Location matters! Type your preferred City or State")






if st.button("Generate Plan"):

    with st.spinner('Generating your Plan Please Wait... ⏳'):

      result = generate_restaurant_plan(cuisine,location,scale)


      tab1, tab2, tab3, tab4 = st.tabs([
        "🏷️ Name & Tagline", 
        "📜 Menu", 
        "📍 Locations", 
        "👥 Staff"
      ])

      with tab1:
        st.subheader("Restaurant Name & Tagline")
        st.write(result['Restaurent'])
      with tab2:
        st.subheader("Curated Menu (Starters • Main Course • Desserts • Beverages)")
        st.write(result['Menu_Items'])
      with tab3:
        st.subheader(" Recommended Hotspots to Start Your Restaurant")
        st.write(result['restaurant_location_suggestions'])
      with tab4:
       st.subheader("Ideal Staff & Team Structure")
       st.write(result['staff_plan'])

else:
  st.info("👆 Enter details & click **Generate Business Plan** to see suggestions.")