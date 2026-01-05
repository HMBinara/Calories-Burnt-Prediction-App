import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. Page Config
st.set_page_config(page_title="BurnFit Dashboard",page_icon="🔥", layout="wide")

# Custom CSS for modern styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .prediction-card {
        background-color: #ffffff;
        padding: 40px 20px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        border-right: 8px solid #ff4b4b;
        position: sticky;
        top: 2rem;
    }
    
    </style>
    """, unsafe_allow_html=True)

# 2. Load the model
@st.cache_resource
def load_model():
    return pickle.load(open('Cb_prediction.pkl', 'rb'))

model = load_model()

# --- SIDEBAR INPUTS ---
st.sidebar.title("🔧 Activity Settings")

def user_input_features():
    gender = st.sidebar.radio('Gender', ('male', 'female'), horizontal=True)
    age = st.sidebar.slider('Age', 10, 100, 25)
    height = st.sidebar.slider('Height (cm)', 120.0, 220.0, 175.0)
    weight = st.sidebar.slider('Weight (kg)', 30.0, 150.0, 70.0)
    duration = st.sidebar.slider('Duration (min)', 1, 60, 20)
    heart_rate = st.sidebar.slider('Heart Rate', 60, 200, 100)
    body_temp = st.sidebar.slider('Body Temperature (C)', 36.0, 42.0, 38.5)
    
    gender_numeric = 0 if gender == 'male' else 1
    
    data = {
        'Gender': gender_numeric, 'Age': age, 'Height': height,
        'Weight': weight, 'Duration': duration,
        'Heart_Rate': heart_rate, 'Body_Temp': body_temp
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()
prediction = model.predict(input_df)[0]


st.title("🔥 BurnLive AI - Fitness Dashboard")

# --- MAIN LAYOUT ---
# Columns: [Middle for Charts, Right for Prediction]
col_charts, col_pred = st.columns([2, 1], gap="medium")



# --- CENTER COLUMN: CHARTS (Vertical Stack) ---
with col_charts:
    
    
    st.header("📊 Activity Analysis")
    # --- ACTIVITY ANALYSIS HEADER & DESCRIPTION ---
    st.write("This graph visualizes the projected calorie burn over a 60-minute session based on your current intensity.As your Duration increases, the cumulative Calories burnt scales according to your heart rate and physical metrics.")
    
    # Chart 1: Prediction Trend Line
    
    durations = np.arange(1, 61)
    temp_df = pd.DataFrame([input_df.iloc[0]] * 60)
    temp_df['Duration'] = durations
    trend_preds = model.predict(temp_df)
    
    fig_trend = px.line(x=durations, y=trend_preds, 
                        title="Calorie Burn Trend (Over Time)",
                        labels={'x': 'Duration (min)', 'y': 'Calories'})
    fig_trend.update_traces(line_color='#ff4b4b', line_width=4)
    fig_trend.update_layout(height=350, plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_trend, use_container_width=True)
    

    
# --- RIGHT COLUMN: PREDICTION RESULT ---
with col_pred:
    st.write("##") # Spacer
    st.markdown(f"""
        <div class="prediction-card">
            <p style="color: #666; font-size: 1.5em; margin-bottom: 10px;">TOTAL CALORIES BURNT</p>
            <h1 style="color: #ff4b4b; font-size: 5em; margin: 0;">{prediction:.1f}</h1>
            <p style="color: #ff4b4b; font-size: 1.5em; font-weight: bold;">KCAL</p>
            <hr style="border: 0.5px solid #eee; margin: 20px 0;">
            <p style="color: #888; font-style: italic;">Adjust settings on the left to see real-time updates.</p>
        </div>
    """, unsafe_allow_html=True)

    