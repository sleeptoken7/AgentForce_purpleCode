# Sentiview AI - AgentForce Hackathon

**Team:** purpleCode
**Track:** Track 3: AI for Industry Use Cases
**Problem Statement:** AI Marketing Persona Builder

## 🚀 Project Description

Sentiview AI is an interactive web application designed to help marketing teams for restaurants in Bengaluru. It leverages a large dataset of Zomato reviews and a powerful AI agent (Google's Gemini) to automatically generate detailed customer personas and actionable campaign ideas.

Unlike static reports, Sentiview AI allows users to have a conversation with the agent, providing refinement instructions (e.g., "make them more budget-conscious") to reshape the personas in real-time.

## ✨ Key Features

* **Restaurant Selection:** Users can select from thousands of restaurants in the Bengaluru dataset.
* **Automated Review Analysis:** The app instantly pulls and displays sample reviews for the chosen restaurant.
* **AI Persona Generation:** With one click, the AI reads the reviews and generates two distinct, detailed marketing personas.
* **Interactive Refinement:** Users can provide natural language feedback to the agent to regenerate the personas based on new criteria.

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Data Handling:** Pandas
* **AI Model:** Google Gemini 1.5 Flash API
* **Environment:** Managed with Conda

## ⚙️ How to Run

1.  Create and activate the conda environment:
    ```bash
    conda create --name agentforce python=3.9 -y
    conda activate agentforce
    ```
2.  Install dependencies:
    ```bash
    conda install -c conda-forge pandas streamlit python-dotenv -y
    python -m pip install google-generativeai
    ```
3.  Create a `.env` file with your `GEMINI_API_KEY`.
4.  Run the app:
    ```bash
    streamlit run main.py
    ```