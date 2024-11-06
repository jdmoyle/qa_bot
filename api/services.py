from langchain.llms import OpenAI

class AnswerQuestionsService:
    """
    Service for answering questions based on the document using Langchain.

    **Methods**:
    - `answer_questions`: Takes the questions and document content and generates answers using Langchain.
    """
    def __init__(self):
        self.llm = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # Initialize the OpenAI model

    def answer_questions(self, questions, document_content):
        """
        Answer each question based on the provided document content using Langchain.
        
        **Args**:
        - questions: List of questions to be answered.
        - document_content: The content of the document to use as context.
        
        **Returns**:
        - list: A list of dictionaries containing each question and its corresponding answer.
        """
        answers = []
        
        # Define the prompt template for Langchain
        prompt_template = """You are a helpful assistant. Based on the following document, answer the questions that follow:
        Document: {document}
        Questions: {questions}
        """
        
        # Generate answers for each question using Langchain
        for question in questions:
            prompt = prompt_template.format(document=document_content, questions=question)
            answer = self.llm(prompt)  # Call Langchain to get the answer
            answers.append({"question": question, "answer": answer})
        
        return answers
