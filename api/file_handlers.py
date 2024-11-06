import json
from langchain_community.document_loaders import PyPDFLoader

class DocumentHandler:
    """
    Factory class for handling different types of document files (PDF, JSON).
    
    Depending on the document file type, it returns the appropriate handler strategy.
    """
    @staticmethod
    def get_handler(file):
        """
        Factory method to get the appropriate handler for the document based on file type.

        **Args**:
        - file: The document file uploaded (PDF or JSON).

        **Returns**:
        - An appropriate handler class (PDFHandler or JSONHandler).
        """
        if file.name.endswith(".pdf"):
            return PDFHandler()  # Use PDF parsing strategy
        elif file.name.endswith(".json"):
            return JSONHandler()  # Use JSON parsing strategy
        else:
            raise ValueError("Unsupported document type. Only PDF and JSON are supported.")


class PDFHandler:
    """
    Handler for parsing PDF documents. Uses Langchain's PyPDFLoader to extract content
    from the uploaded PDF file.

    **Methods**:
    - `parse_document`: Extracts content from the PDF.
    - `parse_questions`: Reads questions from the uploaded JSON file.
    """
    def parse_document(self, pdf_file):
        """
        Parse the PDF document and extract its content using PyPDFLoader.

        **Args**:
        - pdf_file: The uploaded PDF file.

        **Returns**:
        - str: Extracted content from the PDF.
        """
        loader = PyPDFLoader(pdf_file)
        document = loader.load()
        return " ".join([page.page_content for page in document])  # Combine all pages into a single string

    def parse_questions(self, questions_file):
        """
        Parse the list of questions from a JSON file.

        **Args**:
        - questions_file: The uploaded JSON file containing the questions.

        **Returns**:
        - list: List of questions extracted from the JSON file.
        """
        questions = json.load(questions_file)
        return list(questions.keys())  # Return only the question keys


class JSONHandler:
    """
    Handler for parsing JSON documents. Extracts content and questions from JSON files.
    
    **Methods**:
    - `parse_document`: Extracts content from the JSON file.
    - `parse_questions`: Reads questions from the uploaded JSON file.
    """
    def parse_document(self, json_file):
        """
        Parse the JSON document and extract its content.

        **Args**:
        - json_file: The uploaded JSON file.

        **Returns**:
        - str: Extracted content from the JSON document.
        """
        data = json.load(json_file)
        return " ".join([str(value) for value in data.values()])  # Combine all values into a single string
    
    def parse_questions(self, questions_file):
        """
        Parse the list of questions from a JSON file.

        **Args**:
        - questions_file: The uploaded JSON file containing the questions.

        **Returns**:
        - list: List of questions extracted from the JSON file.
        """
        questions = json.load(questions_file)
        return list(questions.keys())  # Return only the question keys
