import os
import openai
import streamlit as st

# Configurez votre clé API OpenAI à partir des variables d'environnement
openai.api_key = os.getenv('sk-proj-BayixLUGzeIG5cpmavpVT3BlbkFJVOTlG2yvqtJlzP6eKRjE')

# Fonction pour obtenir une question de l'API OpenAI GPT-3.5
def generate_question():
    chat_history = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Generate a question about vitamins and minerals for a 3rd-grade quiz."},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        max_tokens=50,
        temperature=0.7,
    )
    question = response['choices'][0]['message']['content'].strip()
    return question

# Interface utilisateur Streamlit
st.title("Vitamin Quiz Bot")

# Initialiser l'état de session
if 'iteration' not in st.session_state:
    st.session_state.iteration = 0
    st.session_state.quiz_active = False
    st.session_state.question = ""

# Boucle principale pour le quiz
user_input = st.text_input(f"Vous (Itération {st.session_state.iteration}):")

if user_input.lower() == "commençons le quiz":
    st.session_state.quiz_active = True
    st.session_state.question = generate_question()
    st.session_state.iteration += 1

if st.session_state.quiz_active:
    # Afficher la question
    st.text(f"Bot: {st.session_state.question}")

    # Obtenir la réponse de l'utilisateur
    user_response = st.text_input("Vous:")

    # Bouton pour soumettre la réponse
    if st.button("Soumettre"):
        st.text(f"Vous avez dit: {user_response}")
        st.session_state.question = generate_question()
        st.session_state.iteration += 1
