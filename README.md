# Chat with Multiple PDFs using LangChain and OpenAI

This Streamlit application enables users to engage in a conversation about the content of multiple PDF documents. Leveraging LangChain for text processing and OpenAI for natural language understanding, the app offers a user-friendly interface to interact with and extract valuable information from uploaded PDFs.

## Features

- **Document Processing**: The app processes the text content of multiple PDF documents, making them available for conversation.

- **Natural Language Understanding**: Utilizing OpenAI, the app interprets and responds to user queries about the uploaded PDFs with informative and context-aware answers.

- **Conversational Interface**: The answers are presented in a conversational format, providing a seamless interaction experience.

## Example Use Case

Imagine you have a set of research papers or documents related to a specific topic. You can use this app to:

1. **Upload PDFs**: Upload multiple PDF documents containing research papers or articles.

2. **Ask Questions**: Pose questions about the content, such as "What are the key findings in document A?" or "Summarize the main points of the second PDF."

3. **Converse with the App**: Engage in a natural language conversation with the app, receiving detailed and contextualized responses based on the content of the uploaded PDFs.

## Prerequisites

Make sure you have the required Python packages installed. You can install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the repository:**
  ```bash
  git clone https://github.com/your-username/your-repo.git
  cd your-repo
  ```

2. **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

3. **Run the Streamlit app:**
  ```bash
  streamlit run app.py
  ```

4. **Open the provided URL in your web browser.**
  ```bash
  streamlit run app.py
  ```

# How to Use

1. **Ask a Question**: Enter a question related to the content of your uploaded PDF documents.

2. **Upload PDFs**: In the sidebar, upload one or more PDF documents.

3. **Provide OpenAI API Key**: Enter your OpenAI API key in the provided password field.

4. **Process**: Click the "Process" button to start the conversation.

5. **View Answer**: The answers will be displayed in a conversational format, with alternating user and bot messages.

## Note

- Make sure you have an active internet connection to access the OpenAI API.
- Ensure the provided OpenAI API key is valid.

## Acknowledgments

- [LangChain](https://github.com/langchain)
- [OpenAI](https://platform.openai.com/)
- [Streamlit](https://streamlit.io/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
