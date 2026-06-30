import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# load variables from env
load_dotenv()

def get_llm():
      """
      Returns a configured Groq LLM instance.
      """
      return ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.7,
      )