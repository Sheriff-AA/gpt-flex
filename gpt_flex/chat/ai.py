# LANGCHAIN -> LLMS
from decouple import config
from openai import OpenAI
from groq import Groq

OPENAI_API_KEY=config("OPENAI_API_KEY", default=None, cast=str)
GROQ_API_KEY = config("GROQ_API_KEY", default=None, cast=str)

OPENAI_MODEL = "gpt-4o-mini"
LLAMA_MODEL = "llama-3.3-70b-versatile"

def get_client():   
    # return OpenAI(api_key=OPENAI_API_KEY)
    return Groq(api_key=GROQ_API_KEY)


def get_llm_response(gpt_messages):
    client = get_client()
    completion = client.chat.completions.create(
        model=LLAMA_MODEL,
        messages=gpt_messages
    )
    return completion.choices[0].message.content


