import openai
import streamlit as st

# Configurez votre clé API OpenAI
openai.api_key = 'sk-proj-6wIkgsetv8g7g0bPHM3DT3BlbkFJLXEb0Cv2Zf4VlTBLxHZf'

# Définir une fonction pour obtenir une réponse de l'API OpenAI
def get_openai_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Créer l'application Streamlit
def main():
    st.set_page_config(page_title="Chatbot OpenAI", page_icon="🤖")
    
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Chatbot OpenAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Posez une question et obtenez une réponse instantanée du chatbot.</p>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.4s;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: white;
            color: black;
            border: 2px solid #4CAF50;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Obtenir la question de l'utilisateur
    question = st.text_input("Vous :", "")
    
    # Bouton pour soumettre la question
    if st.button("Envoyer"):
        if question:
            with st.spinner('Le chatbot rédige sa réponse...'):
                response = get_openai_response(question)
            st.success("Réponse du chatbot :")
            st.write(response)
        else:
            st.error("Veuillez entrer une question.")

    st.markdown("<hr style='border:1px solid #4CAF50;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Développé par Ousmane NIANG</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
