# Sentiview AI - Project Documentation

**Team:** purpleCode
**Project:** An interactive AI agent for generating and refining marketing personas from customer reviews.
**Hackathon:** AgentForce Hackathon - August 2025

---

## 1. Architecture

### Overview

Sentiview AI is a web application built with Streamlit that serves as an interactive marketing assistant. It analyzes a large dataset of customer reviews for restaurants in Bengaluru and uses a generative AI model (Google's Gemini) to produce a comprehensive marketing analysis. This includes an overall sentiment score, key customer themes, and detailed personas. The key innovation is its interactive nature, allowing users to refine the generated analysis with natural language commands.

### System Components

Our application is built on three core components:

* **Frontend (UI Layer):**
    * **Technology:** **Streamlit**
    * **Role:** Provides a simple, responsive, and interactive web interface. It handles all user inputs (restaurant selection, refinement commands) and displays the data and AI-generated results in a clean, professional dashboard.

* **Data Layer:**
    * **Technology:** **Pandas** & a **Kaggle CSV Dataset**
    * **Role:** The system's foundation is the `zomato.csv` dataset, which contains thousands of restaurant listings and their associated reviews. We use the Pandas library for efficient loading, cleaning, and filtering of this data in memory.

* **AI Agent Core:**
    * **Technology:** **Google Gemini 1.5 Flash API**
    * **Role:** This is the "brain" of our application. The agent takes a curated list of customer reviews and a carefully engineered prompt as input. It analyzes the unstructured text to identify patterns and synthesizes this information to generate personas and other insights. It also processes refinement requests from the user to create new, updated analyses.

### Data & Logic Flow

1.  **Initialization:** The Streamlit app starts and loads the `zomato.csv` into a Pandas DataFrame, which is cached for performance.
2.  **Restaurant Selection:** The user selects a restaurant from the sidebar dropdown.
3.  **Data Filtering:** The app filters the DataFrame to retrieve all available reviews for the chosen restaurant.
4.  **Initial Generation:** The user clicks the "Generate AI Analysis" button.
5.  **API Call:** A curated set of reviews is sent to the Gemini API along with a detailed prompt asking for a JSON output containing a sentiment score, key themes, and personas.
6.  **Response & Display:** The AI's JSON response is received, parsed, and displayed in a multi-column dashboard with metrics and persona cards.
7.  **Interactive Refinement (Loop):** The user can type a refinement command into a form. This command is added to a new prompt and sent back to the Gemini API, and the process repeats, updating the UI with the refined analysis.

---

## 2. Tech Stack

* **Python:** The core programming language for the entire project.
* **Streamlit:** A powerful open-source framework used to rapidly build and deploy our interactive web application.
* **Pandas:** The primary library for efficient loading, cleaning, and in-memory filtering of the large `zomato.csv` dataset.
* **Google Gemini 1.5 Flash API:** The "brain" of our agent. We leveraged its advanced natural language understanding and generation capabilities for all key analysis tasks.
* **Conda:** The environment manager used to create an isolated and stable development environment, which was crucial for solving complex dependency issues on macOS.
* **Git & GitHub:** Used for version control and to host our public codebase as required by the hackathon.

---

## 3. Usage Guide

This guide explains how to set up and run the Sentiview AI application locally.

### A. Local Setup & Installation

**Prerequisites:**
* Anaconda or Miniconda installed.
* Git installed.

**Step 1: Clone the Repository**
Open your terminal and clone the project's GitHub repository.
```bash
git clone <your-github-repo-url>
cd AgentForce_purpleCode
