import pandas as pd
import streamlit as st
import ast
import os
import google.generativeai as genai
from dotenv import load_dotenv
import re

# --- Page Configuration ---
st.set_page_config(layout="wide", page_title="AI Marketing Persona Generator")
st.title("🤖 AI Marketing Persona Designer")

# --- Load API Key and Configure AI Model ---
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error configuring the AI model. Have you set your GEMINI_API_KEY in the .env file? Error: {e}")
    st.stop()


# --- Data Loading ---
@st.cache_data
def load_data():
    df = pd.read_csv('zomato.csv')
    df.dropna(subset=['reviews_list', 'name'], inplace=True)
    restaurant_names = sorted(df['name'].unique().tolist())
    return df, restaurant_names

df, restaurant_names = load_data()


# --- Session State Initialization ---
if 'personas' not in st.session_state:
    st.session_state.personas = ""


# --- UI Section 1: Restaurant Selection ---
st.header("1. Select a Restaurant")
restaurant_name = st.selectbox(
    "Choose a restaurant to analyze:",
    restaurant_names,
    on_change=lambda: st.session_state.update(personas="")
)

selected_restaurant_data = df[df['name'] == restaurant_name].iloc[0]
st.write(f"You selected: **{restaurant_name}**")


# --- Data Processing Function ---
def get_reviews_for_restaurant(review_string):
    try:
        reviews = ast.literal_eval(review_string)
        review_texts = [review[1].strip() for review in reviews if len(review) > 1 and review[1]]
        return review_texts
    except (ValueError, SyntaxError):
        return []

st.header("2. Customer Reviews Analysis")
reviews = get_reviews_for_restaurant(selected_restaurant_data['reviews_list'])

if not reviews:
    st.warning("No usable reviews found for this restaurant in the dataset.")
    st.stop()

st.success(f"Found **{len(reviews)}** reviews to analyze for **{restaurant_name}**.")
with st.expander("Click to see a sample of the reviews"):
    st.markdown("\n\n".join([f"- *{text}*" for text in reviews[:5]]))


# --- AI Agent Section ---
st.header("3. Generate & Refine AI-Powered Personas")

def generate_personas(reviews_for_prompt, refinement_instruction=""):
    """Calls the Gemini API to generate or refine personas."""
    
    base_prompt = f"""
    You are an expert marketing analyst for restaurants in Bengaluru, India.
    Your task is to read a collection of raw customer reviews for a restaurant and generate 2 detailed, distinct customer personas.

    **Instructions:**
    1.  Analyze the following customer reviews:
        ---
        {reviews_for_prompt}
        ---
    2.  Based on your analysis, create 2 customer personas. Use clear headings for each persona.
    3.  For each persona, provide: Persona Name, Bio, Primary Goal, Key Pain Point, Campaign Idea, and Campaign Description.
    """
    
    if refinement_instruction:
        final_prompt = f"{base_prompt}\n\n**IMPORTANT REFINEMENT:** Now, please regenerate the personas and campaigns based on this new instruction: '{refinement_instruction}'"
    else:
        final_prompt = base_prompt

    try:
        response = model.generate_content(final_prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred while calling the AI: {e}")
        return ""

if st.button("✨ Generate Initial Personas", type="primary"):
    with st.spinner("🤖 AI is analyzing reviews and crafting personas..."):
        reviews_to_send = "\n".join(reviews[:50])
        st.session_state.personas = generate_personas(reviews_to_send)

# --- Display Personas and Refinement Form ---
if st.session_state.personas:
    persona_parts = re.split(r'\*\*Persona 2\*\*|\*\*Persona Name 2\*\*|### Persona 2', st.session_state.personas, flags=re.IGNORECASE)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Persona 1")
        st.markdown(persona_parts[0])

    if len(persona_parts) > 1:
        with col2:
            st.markdown("### Persona 2")
            st.markdown(persona_parts[1])

    st.markdown("---")
    
    # Using a form to prevent the loop
    with st.form(key='refine_form'):
        refinement = st.text_input("Refine these personas (e.g., 'make them more budget-conscious')")
        submitted = st.form_submit_button("Submit Refinement")

        if submitted and refinement:
            with st.spinner("🤖 AI is refining the personas based on your feedback..."):
                reviews_to_send = "\n".join(reviews[:50])
                st.session_state.personas = generate_personas(reviews_to_send, refinement)
                st.rerun() # This is now safe inside a form