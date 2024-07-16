#pip install openai==0.28
#Checking if Streamlit is installed
import openai
import streamlit as st
# Configurez votre clé API OpenAI
openai.api_key = 'sk-proj-BayixLUGzeIG5cpmavpVT3BlbkFJVOTlG2yvqtJlzP6eKRjE'

# Ensure streamlit and openai are installed
# pip install streamlit opena


# Function to get a response from the OpenAI GPT-3.5 API
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

# Streamlit UI
st.title("Vitamin Quiz Bot")

# Initialize session state
if 'iteration' not in st.session_state:
    st.session_state.iteration = 0
    st.session_state.quiz_active = False
    st.session_state.question = ""

# Main loop for the quiz
user_input = st.text_input(f"You (Iteration {st.session_state.iteration}):")

if user_input.lower() == "lets begin the quiz":
    st.session_state.quiz_active = True
    st.session_state.question = generate_question()
    st.session_state.iteration += 1

if st.session_state.quiz_active:
    # Display the question
    st.text(f"Bot: {st.session_state.question}")

    # Get user's response
    user_response = st.text_input("You:")

    # Evaluate the response
    if st.button("Submit"):
        st.text(f"You said: {user_response}")
        st.session_state.question = generate_question()
        st.session_state.iteration += 1
