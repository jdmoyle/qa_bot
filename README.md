Question Answering Bot API
The Question Answering Bot API is a RESTful service built with Django and Django Rest Framework (DRF). It allows you to upload a document (either PDF or JSON) and a set of questions. The API uses Langchain with OpenAI's GPT-3 to generate answers based on the provided document content.

Key Features:
Supports PDF or JSON document input.
Accepts a JSON file containing a list of questions.
Uses Langchain to process the document and answer the questions.
The solution is designed using Strategy Pattern and Dependency Injection (DI) for flexibility in document handling.
Built using Django Rest Framework (DRF) to handle API requests.
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.7+
Django 3.2+
Django Rest Framework
Langchain
OpenAI API key (you'll need this for the Langchain integration)
Installation Steps
1. Clone the Repository
git clone https://github.com/your-repo/question-answering-bot.git
cd question-answering-bot
2. Set up a Virtual Environment
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Dependencies
Install the required dependencies listed in the requirements.txt:
pip install -r requirements.txt
4. Set up OpenAI API Key
Create an account on OpenAI and get an API key. Then, add the key to your Django settings (settings.py):

python
Copy code
OPENAI_API_KEY = 'your-openai-api-key'
5. Apply Migrations
Run database migrations (if any models are used):
python manage.py migrate
6. Run the Development Server
Start the Django development server:
python manage.py runserver
The API will now be available at http://localhost:8000/.

API Endpoints
1. POST /api/answer_questions/
This endpoint accepts two types of input files:

A JSON file with a list of questions.
A PDF or JSON document containing the content to answer those questions.
Request (form-data)
questions (JSON file): A file containing a list of questions.
document (PDF/JSON file): The document (either PDF or JSON format) with content based on which answers will be generated.
Example Request for questions.json
{
  "What is Langchain?": "",
  "What does Langchain do?": "",
  "Who created Langchain?": ""
}
Example Request for document.pdf
Upload a PDF file containing relevant content about Langchain.
Response
A JSON object with the answers for each question.
Example Response:
{
  "answers": [
    {
      "question": "What is Langchain?",
      "answer": "Langchain is a framework for building applications that use language models."
    },
    {
      "question": "What does Langchain do?",
      "answer": "Langchain helps developers integrate language models like GPT-3, Cohere, or Hugging Face transformers into their applications."
    },
    {
      "question": "Who created Langchain?",
      "answer": "Langchain was developed by Harrison Chase."
    }
  ]
}
Code Architecture
1. views.py
Contains the main logic of the API endpoint, processes the uploaded files, and sends the files for parsing and answering.

2. file_handlers.py
Implements the Strategy Pattern for handling different types of files (PDF and JSON). This file is responsible for parsing the document based on its type and extracting content.

3. services.py
Contains the core logic for interacting with Langchain. It processes the document, sends the content to Langchain, and retrieves the answers.

4. models.py
Defines models for storing data related to the questions, answers, or any other relevant information. You can expand this as per your application's requirements.

5. serializers.py
Serializes data, including question-answer pairs if storing answers is required.

6. urls.py
Defines the URL patterns for accessing the API endpoints.

Example Files for Testing
Example questions.json

{
  "What is Langchain?": "",
  "What does Langchain do?": "",
  "Who created Langchain?": ""
}
Example document.pdf
A PDF document that contains relevant information about Langchain (or any other topic for testing).
Sample Input and Output
Sample Input Request
questions.json:

{
  "What is Langchain?": "",
  "What does Langchain do?": "",
  "Who created Langchain?": ""
}
document.pdf: A PDF file with relevant content (e.g., a document describing Langchain).
Sample Output Response

{
  "answers": [
    {
      "question": "What is Langchain?",
      "answer": "Langchain is a framework for building applications that use language models."
    },
    {
      "question": "What does Langchain do?",
      "answer": "Langchain helps developers integrate language models like GPT-3, Cohere, or Hugging Face transformers into their applications."
    },
    {
      "question": "Who created Langchain?",
      "answer": "Langchain was developed by Harrison Chase."
    }
  ]
}
Testing the API with Postman
Step 1: Set Up the Request
Method: POST
URL: http://localhost:8000/api/answer_questions/
Body: form-data
Step 2: Upload Files
questions: Upload the questions.json file.
document: Upload either the document.pdf or document.json file.
Step 3: Send the Request
Click Send to see the response with answers to your questions.

Troubleshooting
Invalid API Key: Ensure that the OpenAI API key is correctly set in settings.py.
File Parsing Errors: Ensure that the file you upload is either a valid PDF or JSON.
Missing Fields: Both the questions and document fields are required in the form-data. Ensure they are included in your request.
