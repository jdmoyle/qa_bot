from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .services import AnswerQuestionsService
from .file_handlers import DocumentHandler

class QuestionAnsweringAPIView(APIView):
    """
    API view for answering questions based on document content.

    This endpoint allows users to upload a JSON file containing a list of questions
    and a PDF or JSON file containing the document over which the questions will be answered.

    **Request Example**:
    - `questions` file (JSON) containing a list of questions.
    - `document` file (PDF or JSON) containing the document.

    **Response**:
    A JSON object containing the answers for each question.
    """
    parser_classes = [MultiPartParser, FormParser]  # Allow file uploads in form-data
    
    def post(self, request, *args, **kwargs):
        """
        Handle POST request for answering questions based on the provided document.

        - Parses the document and questions files.
        - Uses Langchain to generate answers based on document content.

        **Parameters**:
        - questions (file): A JSON file containing a list of questions.
        - document (file): A PDF or JSON file containing the document for answering questions.

        **Returns**:
        - JSON response with the answers for each question.
        """
        # Get files from the request
        questions_file = request.FILES.get('questions')
        document_file = request.FILES.get('document')

        # Check if both files are provided
        if not questions_file or not document_file:
            return Response(
                {"error": "Both questions and document files are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Use the DocumentHandler factory to handle file parsing based on document type
        handler = DocumentHandler.get_handler(document_file)
        document_content = handler.parse_document(document_file)
        
        # Read the questions from the file
        questions = handler.parse_questions(questions_file)
        
        # Use the service class to get answers
        answer_service = AnswerQuestionsService()
        answers = answer_service.answer_questions(questions, document_content)
        
        return Response({"answers": answers}, status=status.HTTP_200_OK)
