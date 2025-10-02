# Agentic News Weaver: An Autonomous AI News Analysis Platform

## 📖 Introduction

Agentic News Weaver is a full-stack web application that leverages a crew of autonomous AI agents to solve the problem of information overload. Instead of manually searching and reading multiple articles, a user can simply input any news topic, and the AI crew will perform real-time research, read the full content of the most relevant articles, and generate a concise, synthesized summary report with sources.

This project demonstrates the power of multi-agent collaboration using **CrewAI**, with a locally-run LLM powered by **Ollama** for privacy and cost-effectiveness. The entire system is served through a **FastAPI** backend and is accessible via a clean, modern web interface.

## ✨ Features

-   **Autonomous Agent Collaboration:** A Researcher Agent and an Analyst Agent work together sequentially to deliver results.
-   **Real-time Web Research:** Uses the Tavily API to find the most current and relevant news articles on any topic.
-   **In-depth Content Analysis:** Scrapes the full content of websites to provide summaries based on complete information, not just snippets.
-   **Local & Private AI:** Powered by Ollama and Llama 3, ensuring that the core reasoning and generation tasks happen on your local machine.
-   **Full-Stack Application:** A robust FastAPI backend serves the AI logic to a user-friendly HTML, CSS, and JavaScript frontend.

## 🏗️ Project Architecture

The application follows a simple yet powerful workflow, where the frontend communicates with a backend that orchestrates the AI agent crew.

![Workflow Diagram](https://i.imgur.com/GzB2X6t.png)

1.  **User Query:** The user inputs a topic on the web frontend.
2.  **API Request:** A request is sent to the FastAPI backend.
3.  **CrewAI Kickoff:** The backend initializes the AI crew with the given topic.
4.  **Research & Scrape:** The Researcher Agent finds top URLs via Tavily and scrapes their full content.
5.  **Analyze & Summarize:** The Analyst Agent receives the scraped text and writes a detailed summary for each source.
6.  **API Response:** The final markdown report is sent back to the frontend.
7.  **Display Results:** The frontend renders the report for the user.

## 💻 Technology Stack

-   **Backend:** Python, FastAPI, Uvicorn
-   **AI Engine / Framework:** CrewAI, LangChain
-   **Local AI Model:** Ollama (running Llama 3)
-   **Frontend:** HTML5, CSS3, JavaScript
-   **Agent Tools:** Tavily Search API, ScrapeWebsiteTool

---

## 🚀 Setup and Installation Guide

Follow these steps to get the project running on your local machine.

### **1. Prerequisites**

Before you begin, ensure you have the following installed and configured:

-   **Python** (version 3.10.11 or newer).
-   **Ollama**: Download and install from [ollama.com](https://ollama.com/).
-   **A local LLM**: Pull the Llama 3.2 3b model by running this command in your terminal:
    ```bash
    ollama run llama3.2:3b
    ```
    **Leave Ollama running in the background.**
-   **Tavily API Key**: Get a free API key from [Tavily AI](https://app.tavily.com/).

### **2. Backend Setup**

1.  **Clone the repository and navigate to the `backend` directory:**
    ```bash
    git clone <your-repo-url>
    cd news-agent-app/backend
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required Python dependencies:**
    Run this command in the terminal of backend directory in vscode terminal
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set your Tavily API Key:**
    Create a new file named `.env` inside the `backend` directory. Open the file and add your key as follows:
    ```
    TAVILY_API_KEY="your_tavily_api_key_here"
    ```

5.  **Run the FastAPI Server:**
    From inside the `backend` directory, execute the following command:
    ```bash
    uvicorn main:app --reload
    ```
    The server should now be running at `http://localhost:8000`. Keep this terminal open.

### **3. Frontend Setup**

1.  **Open a new terminal window.**

2.  **Navigate to the `frontend` directory:**
    ```bash
    cd news-agent-app/frontend
    ```

3.  **Serve the frontend files:**
    The easiest way is to use Python's built-in HTTP server.
    ```bash
    # For Python 3
    python -m http.server 3000
    ```
    The frontend is now accessible at `http://localhost:3000`.

---

## ▶️ How to Use

1.  Make sure both your **Ollama application** and your **FastAPI backend server** are running.
2.  Open your web browser and navigate to **[http://localhost:3000](http://localhost:3000)**.
3.  Enter a news topic into the input field (e.g., "advancements in solid-state battery technology").
4.  Click the "Analyze Topic" button.
5.  Wait for the AI crew to complete its work (this may take a minute depending on your hardware). The final summarized report will appear on the screen.

## 🔮 Future Enhancements

-   **Add a Fact-Checking Agent:** A third agent could be added to the crew to verify claims made in the summarized articles.
-   **Voice Integration:** Implement the Web Speech API on the frontend to allow for voice-based queries and spoken responses.
-   **User Accounts & History:** Add a database and user authentication to save past search reports.
-   **Caching Layer:** Implement a caching system (like Redis) to store results for popular queries, providing instant responses and reducing redundant processing.
