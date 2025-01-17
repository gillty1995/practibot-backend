Music Practice Chatbot

This project is a Python-based chatbot that I created to practice and learn Python. The chatbot helps users with music practice tips and can provide guitar/bass tablature, all powered by OpenAI’s GPT-4 model.

Key Features:
• Music Coaching: The chatbot offers helpful practice tips for musicians.
• Guitar/Bass Tabs: It provides formatted guitar/bass tablature when requested.
• Conversation History: Tracks and limits conversation history for context.
• Custom Follow-up: Generates follow-up questions based on user queries.

How It Works: 1. The chatbot receives user questions related to music practice. 2. It interacts with OpenAI’s GPT-4 API to generate responses. 3. If the question relates to tabs, the response is formatted for better readability.

Technologies:
• Python
• OpenAI GPT-4 API
• dotenv for environment variables

Project Structure:
• chatbot_backend.py: Main Python script handling chatbot logic.
• services/follow_up.py: Logic for generating follow-up questions.
