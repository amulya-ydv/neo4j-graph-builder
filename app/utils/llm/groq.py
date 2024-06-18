from langchain_groq import ChatGroq

from app.settings.config import settings
from app.utils.llm.base import LLMWrapper


class Groq(LLMWrapper):
    def __init__(self):
        self.model_version = "mixtral-8x7b-32768"
        self.groq_api_key = settings.get("GROQ_API_KEY")
        self.temperature = settings.get("MODEL_TEMPERATURE")

    def get_llm(self):
        return ChatGroq(
            model_name=self.model_version,
            groq_api_key=self.groq_api_key,
            temperature=self.temperature,
        )

    def get_embedding_model(self):
        raise NotImplementedError