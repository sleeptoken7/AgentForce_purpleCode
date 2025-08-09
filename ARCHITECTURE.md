# Sentiview AI - Architecture Document

**Team:** purpleCode
**Project:** An interactive AI agent for generating and refining marketing personas from customer reviews.

## 1. Overview

Sentiview AI is a web application built with Streamlit that serves as an interactive marketing assistant. It analyzes a large dataset of customer reviews for restaurants in Bengaluru and uses a generative AI model (Google's Gemini) to produce detailed customer personas and tailored marketing campaign ideas. The key feature is its interactive nature, allowing users to refine the generated personas with natural language commands.

## 2. System Components

Our application is built on three core components:

* **Frontend (UI Layer):**
    * **Technology:** Streamlit
    * **Role:** Provides a simple, responsive, and interactive web interface. It handles all user inputs (restaurant selection, refinement commands) and displays the data and AI-generated results in a clean, multi-column layout.

* **Data Layer:**
    * **Technology:** Pandas & a Kaggle CSV Dataset
    * **Role:** The system's foundation is the `zomato.csv` dataset, which contains thousands of restaurant listings and their associated reviews. We use the Pandas library for efficient loading, cleaning, and filtering of this data in memory when a user selects a restaurant.

* **AI Agent Core:**
    * **Technology:** Google Gemini 1.5 Flash API
    * **Role:** This is the "brain" of our application. The agent takes a curated list of customer reviews and a carefully engineered prompt as input. It analyzes the unstructured text to identify patterns and synthesizes this information to generate personas. It also processes refinement requests from the user to create new, updated personas, creating an interactive feedback loop.

## 3. Data & Logic Flow

The application follows a simple, linear flow:

1.  **Initialization:** The Streamlit app starts and loads the `zomato.csv` into a Pandas DataFrame, which is cached for performance.
2.  **Restaurant Selection:** The user is presented with a dropdown menu of all unique restaurant names from the dataset.
3.  **Data Filtering:** Upon selection, the app filters the DataFrame to retrieve the list of reviews for the chosen restaurant.
4.  **Initial Generation:** The user clicks the "Generate Initial Personas" button.
5.  **API Call:** A curated set of reviews is sent to the Gemini API along with a detailed prompt.
6.  **Response & Display:** The AI's text response is received, parsed, and displayed in a two-column layout.
7.  **Interactive Refinement (Loop):** The user can type a refinement command into a form. This command is added to a new prompt, sent back to the Gemini API, and the process repeats from Step 6, updating the UI with the new personas.