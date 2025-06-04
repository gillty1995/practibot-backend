**Practibot - Music Practice Chatbot**

Practibot is a chatbot designed to assist users in improving their music practice routines. It offers personalized tips, tablature formatting, and engaging conversational capabilities, powered by OpenAI’s GPT-4. This project is hosted on AWS and represents my journey of learning Python, with the help of ChatGPT and documentation, to build a functional and interactive tool.

**Links**
• Deployed Website: https://practibot.mine.bz/
• Frontend Repository: https://github.com/gillty1995/practibot-frontend

**Key Features**

1. Music Coaching: Provides personalized and actionable practice tips for musicians.
2. Guitar/Bass Tablature: Automatically formats guitar and bass tabs for improved readability.
3. Conversation Management: Maintains a limited conversation history to ensure contextually relevant responses.
4. Custom Follow-Up Questions: Suggests insightful follow-up questions based on user input.

**How It Works**

1. Users ask Practibot music-related questions through the chatbot interface.
2. Practibot processes the input using OpenAI’s GPT-4 API.
3. Responses are dynamically formatted, particularly for queries involving tablature.
4. Custom follow-up questions are generated to guide further conversation.

**Technologies Used**

1. Backend Framework: FastAPI
2. Programming Language: Python
3. AI Model: OpenAI GPT-4 API
4. Environment Management: dotenv for secure API key storage
5. Hosting Platform: AWS
6. Testing Framework: Pytest

**Project Structure**

1. main.py: Sets up the FastAPI backend, including routes and middleware.
2. chatbot_service.py: Core chatbot logic, including response generation and conversation management.
3. services/follow_up.py: Handles dynamic generation of follow-up questions.
4. test_chatbot_service.py: Contains unit tests to verify core functionality.

**Learning Journey with Python**
This project was a hands-on opportunity to learn Python from scratch. Key Python concepts and skills I learned include:

1. Basic Syntax: Understanding Python’s structure, indentation rules, and conventions.
2. Functions (def): Writing reusable functions with parameters and return values.
3. Global Variables: Managing state using global variables for conversation history.
4. String Manipulation: Using string methods to format and process text, such as guitar tablature.
5. Error Handling: Implementing try and except blocks to manage unexpected situations.
6. Asynchronous Programming: Creating asynchronous API routes in FastAPI to handle user requests efficiently.
7. Unit Testing: Writing and executing unit tests using Pytest to ensure code reliability.
8. Environment Management: Securing sensitive data like API keys using .env files.

**Future Enhancements**
• Expand support to include other instruments and music theory questions.
• Enhance user interface design for better interaction.
• Add text to voice/audio feature.
• Add more in depth music features through implmenting additional API's for advanced functionality.
