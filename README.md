**Practibot - Music Practice Chatbot**

Practibot is a chatbot designed to assist users in improving their music practice routines. It offers personalized tips, tablature formatting, and engaging conversational capabilities, powered by OpenAI’s GPT-4. This project is hosted on AWS and represents my journey of learning Python, with the help of ChatGPT and documentation, to build a functional and interactive tool.

**Links**
• Deployed Website: https://practibot.mine.bz/
• Frontend Repository: https://github.com/gillty1995/practibot-frontend

**Key Features**
• Music Coaching: Provides personalized and actionable practice tips for musicians.
• Guitar/Bass Tablature: Automatically formats guitar and bass tabs for improved readability.
• Conversation Management: Maintains a limited conversation history to ensure contextually relevant responses.
• Custom Follow-Up Questions: Suggests insightful follow-up questions based on user input.

**How It Works**

1. Users ask Practibot music-related questions through the chatbot interface.
2. Practibot processes the input using OpenAI’s GPT-4 API.
3. Responses are dynamically formatted, particularly for queries involving tablature.
4. Custom follow-up questions are generated to guide further conversation.

**Technologies Used**
• Backend Framework: FastAPI
• Programming Language: Python
• AI Model: OpenAI GPT-4 API
• Environment Management: dotenv for secure API key storage
• Hosting Platform: AWS
• Testing Framework: Pytest

**Project Structure**
• main.py: Sets up the FastAPI backend, including routes and middleware.
• chatbot_service.py: Core chatbot logic, including response generation and conversation management.
• services/follow_up.py: Handles dynamic generation of follow-up questions.
• test_chatbot_service.py: Contains unit tests to verify core functionality.

**Learning Journey with Python**
This project was a hands-on opportunity to learn Python from scratch. Key Python concepts and skills I learned include:
• Basic Syntax: Understanding Python’s structure, indentation rules, and conventions.
• Functions (def): Writing reusable functions with parameters and return values.
• Global Variables: Managing state using global variables for conversation history.
• String Manipulation: Using string methods to format and process text, such as guitar tablature.
• Error Handling: Implementing try and except blocks to manage unexpected situations.
• Asynchronous Programming: Creating asynchronous API routes in FastAPI to handle user requests efficiently.
• Unit Testing: Writing and executing unit tests using Pytest to ensure code reliability.
• Environment Management: Securing sensitive data like API keys using .env files.

**Future Enhancements**
• Expand support to include other instruments and music theory questions.
• Enhance user interface design for better interaction.
• Add text to voice/audio feature.
• Add more in depth music features through implmenting additional API's for advanced functionality.
