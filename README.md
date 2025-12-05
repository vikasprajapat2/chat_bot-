# AI Chatbot Assistant

This is a Flask-based chatbot application powered by Google's Gemini API. It provides an intelligent, conversational interface with a custom personality.

## Features

*   **AI-Powered Conversations:** Utilizes Google's Gemini model for natural and engaging responses.
*   **Custom Personality:** The AI (Nexa) is designed to be helpful, clever, and concise with a futuristic tone.
*   **Web Interface:** Clean and responsive chat interface built with HTML/CSS.
*   **History Awareness:** Maintains conversation context (in-session).

## Prerequisites

*   Python 3.x
*   A Google Cloud Project with the Gemini API enabled.
*   An API Key for the Gemini API.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vikasprajapat2/chat_bot-.git
    cd chat_bot-
    ```

2.  **Install dependencies:**
    ```bash
    pip install flask google-generativeai
    ```

## Configuration

1.  **Set up your API Key:**
    You need to set the `GOOGLE_API_KEY` environment variable.
    
    *   **Windows (PowerShell):**
        ```powershell
        $env:GOOGLE_API_KEY="your_api_key_here"
        ```
    *   **Linux/macOS:**
        ```bash
        export GOOGLE_API_KEY="your_api_key_here"
        ```

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```

2.  **Open your browser:**
    Navigate to `http://127.0.0.1:5000` to start chatting.

## Project Structure

*   `app.py`: Main Flask application and API integration.
*   `templates/index.html`: HTML template for the chat interface.
*   `statics/style.css`: CSS styles for the frontend.
