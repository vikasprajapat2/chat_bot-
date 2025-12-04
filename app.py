import os
import traceback
import logging
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__, static_folder='statics', static_url_path='/static')

# Configure Gemini API
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'AIzaSyBSJ5ev58OHqk_DXMuHeAhME0gD_pikAG8')
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it before running the app.")

genai.configure(api_key=GOOGLE_API_KEY)
system_instruction = "You are Nexa, an advanced AI assistant. You are helpful, clever, and concise. You do not sound like a generic AI. You have a distinct, slightly futuristic personality."
model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=system_instruction)

# Initialize chat session with history
chat_session = model.start_chat(history=[])

# Configure basic logging to a file for easier debugging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        user_message = data.get('message', '').strip()
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Generate response from Gemini using the chat session
        response = chat_session.send_message(user_message)
        bot_response = response.text
        return jsonify({'response': bot_response})
    except Exception as e:
        tb = traceback.format_exc()
        # Log full traceback to both console and file
        print("Error in /chat endpoint:\n", tb)
        logging.error("Error in /chat endpoint: %s", tb)
        return jsonify({'error': 'Server error. Check server logs for details.'}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Chatbot is running at: http://127.0.0.1:5000")
    print("="*60 + "\n")
    app.run(debug=False, host='0.0.0.0', port=5000)