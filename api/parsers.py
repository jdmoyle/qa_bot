# parsers.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.document_loaders import JSONLoader

class PDFParser:
    """
    Parser for PDF documents.
    """
    def load_document(self, document_file):
        """
        Loads and parses a PDF document.
        
        Params:
            document_file (file): The PDF file to parse.

        Returns:
            Document: The parsed document object.
        """
        loader = PyPDFLoader(document_file)
        return loader.load()


class JSONParser:
    """
    Parser for JSON documents.
    """
    def load_document(self, document_file):
        """
        Loads and parses a JSON document.
        
        Params:
            document_file (file): The JSON file to parse.

        Returns:
            Document: The parsed document object.
        """
        loader = JSONLoader(document_file)
        return loader.load()


class ParserFactory:
    """
    Factory for creating the appropriate parser based on the file type.
    """
    @staticmethod
    def get_parser(file_name):
        """
        Returns the correct parser based on the file type (PDF or JSON).
        
        Params:
            file_name (str): The name of the document file.
        
        Returns:
            DocumentParser: A parser instance for the document.
        """
        if file_name.endswith(".pdf"):
            return PDFParser()
        elif file_name.endswith(".json"):
            return JSONParser()
        else:
            raise ValueError("Unsupported file type. Only PDF and JSON files are supported.")
