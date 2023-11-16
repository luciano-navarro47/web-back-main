import os
import spacy
import numpy as np
import openai
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

previous_questions = []
previous_answers = []
model_spacy = spacy.load("es_core_news_sm")
forbidden_words = ["madrid", "Word2"]

def cosine_similarity(vector1, vector2):
    superposicion = np.dot(vector1, vector1)
    magnitud1 = np.linalg.norm(vector1)
    magnitud2 = np.linalg.norm(vector2)
    cos_sim = superposicion / (magnitud1 * magnitud2)
    return cos_sim


def is_relevant(response, input, umbral=0.5):
    vector_input = model_spacy(input).vector
    vector_response = model_spacy(response).vector
    similarity = cosine_similarity(vector_input, vector_response)
    return similarity >= umbral


def filter_black_list(text, black_list):
    token = model_spacy(text)
    result = []

    for t in token:
        if t.text.lower() not in black_list:
            result.append(t.text)
        else:
            result.append("[xxxx]")

    return " ".join(result)


def ask_chat_gpt(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    n=1,
    max_tokens=150,
    temperature=1.5
    )

    response_without_control = response.choices[0].text.strip()
    controlled_response = filter_black_list(response_without_control, forbidden_words)
    return controlled_response

print("Welcome to our chatbot. Type 'exit' when you want to finish")

while True:
    historical_conversation = ""
    user_input = input("\nYou:")
    if user_input.lower() == "exit":
        break

    for question, answer in zip(previous_questions, previous_answers):
        historical_conversation += f"User asks: {question}\n"
        historical_conversation += f"ChatGpt responds: {answer}\n"

    prompt = f"The user asks: {user_input}\n"
    historical_conversation += prompt
    responds_gpt = ask_chat_gpt(historical_conversation)

    relevant = is_relevant(responds_gpt, user_input)

    if(relevant):
        print(f"{responds_gpt}")
        previous_questions.append(user_input)
        previous_answers.append(responds_gpt)
    else:
        print("The answer is not relevant")

    
    print(f"{responds_gpt}")

    previous_questions.append(user_input)
    previous_answers.append(responds_gpt)


