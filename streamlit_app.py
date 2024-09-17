import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lista per memorizzare i problemi
if 'problemi' not in st.session_state:
    st.session_state.problemi = []

def aggiungi_problema(descrizione, gravità, impatto, data):
    problema = {
        'Descrizione': descrizione,
        'Gravità': gravità,
        'Impatto': impatto,
        'Data': data
    }
    st.session_state.problemi.append(problema)

def visualizza_problemi():
    df = pd.DataFrame(st.session_state.problemi)
    if df.empty:
        st.write("Nessun problema da visualizzare.")
        return
    
    st.write("## Panoramica dei Problemi")
    st.dataframe(df)
    
    # Creazione di un grafico a dispersione basato su Gravità e Impatto
    fig, ax = plt.subplots()
    ax.scatter(df['Gravità'], df['Impatto'], alpha=0.7)
    ax.set_title('Panoramica dei Problemi')
    ax.set_xlabel('Gravità')
    ax.set_ylabel('Impatto')
    plt.grid(True)
    st.pyplot(fig)

def main():
    st.title("Gestione Problemi Aziendali")

    menu = st.sidebar.selectbox("Seleziona un'opzione", ["Aggiungi Problema", "Visualizza Problemi"])

    if menu == "Aggiungi Problema":
        st.header("Aggiungi un Nuovo Problema")
        descrizione = st.text_input("Descrizione del problema")
        gravità = st.slider("Gravità", 1, 5, 1)
        impatto = st.slider("Impatto", 1, 5, 1)
        data = st.date_input("Data")
        
        if st.button("Aggiungi Problema"):
            aggiungi_problema(descrizione, gravità, impatto, data)
            st.success("Problema aggiunto con successo!")

    elif menu == "Visualizza Problemi":
        st.header("Visualizza i Problemi")
        visualizza_problemi()

if __name__ == "__main__":
    main()
