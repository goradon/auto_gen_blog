import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from config import prompt, generation_config, safety_settings
from dotenv import load_dotenv
import os

load_dotenv()

def generate():
    vertexai.init(project=os.getenv("GC_PROJECT_ID"), location=os.getenv("LOCATION"))
    model = GenerativeModel(
        os.getenv("MODEL"),
    )
    responses = model.generate_content(
        [prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=False,
    )
    return responses