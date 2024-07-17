import openai
import streamlit as st
import time

# Configuration de la  clé API OpenAI
openai.api_key ='sk-proj-8WDxw0HoLkNgmMo4S9EnT3BlbkFJIoaAOrKJEGdiEcdpfpFF'

#  Fonction pour obtenir une réponse de l'API OpenAI GPT-3.5
def get_openai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']

# Application Streamlit
def main():
    # Configurer la page
    st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="wide")

    # En-tête et sous-titre
    st.title("🤖 Chatbot AI")
    st.markdown("### Posez-moi n'importe quelle question !")

    # Ajouter une image ou un logo
    st.image("https://via.placeholder.com/800x200.png?text=Chatbot+AI", use_column_width=True)

    # Conteneur pour la conversation
    conversation = st.container()

    # Saisie de l'utilisateur
    with st.form(key='chat_form'):
        user_input = st.text_input("Vous :", "")
        submit_button = st.form_submit_button(label='Envoyer')

    # Affichage de la réponse du chatbot
    if submit_button and user_input:
        with st.spinner('Le chatbot est en train de répondre...'):
            response = get_openai_response(user_input)
        conversation.markdown(f"**Vous** : {user_input}")
        conversation.markdown(f"**Chatbot** : {response}")

    # Ajouter un espace pour plus de clarté
    st.markdown("<br>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
