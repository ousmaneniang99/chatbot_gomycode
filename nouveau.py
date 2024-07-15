#pip install openai==0.28
#Checking if Streamlit is installed
import openai
import streamlit as st

# Configurez votre clé API OpenAI
openai.api_key = 'sk-proj-6wIkgsetv8g7g0bPHM3DT3BlbkFJLXEb0Cv2Zf4VlTBLxHZf'

# Function to get response from OpenAI API
def get_openai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit app
def main():
    st.title("Chatbot avec OpenAI")
    st.write("Posez-moi n'importe quelle question !")

    question = st.text_input("Vous :")

    if st.button("Envoyer"):
        response = get_openai_response(question)
        st.write("Chatbot : " + response)

if __name__ == "__main__":
    main()
