import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from config import text1, generation_config, safety_settings
from dotenv import load_dotenv
import os

load_dotenv()

def generate():
    vertexai.init(project=os.getenv("GCP_PROJECT_ID"), location=os.("LOCATION"))
    model = GenerativeModel(
        "gemini-1.5-pro-001",
    )
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=False,
    )
    return responses