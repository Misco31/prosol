import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import openai

# Configura la tua chiave API di OpenAI
openai.api_key = 'YOUR_API_KEY_HERE'

# Lista per memorizzare i problemi
if 'problemi' not in st.session_state:
    st.session_state.problemi = []

def aggiungi_problema(descrizione, gravità, impatto, data, categoria, priorità, note):
    problema = {
        'Descrizione': descrizione,
        'Gravità': gravità,
        'Impatto': impatto,
        'Data': data,
        'Categoria': categoria,
        'Priorità': priorità,
        'Note': note
    }
    st.session_state.problemi.append(problema)

def visualizza_problemi():
    df = pd.DataFrame(st.session_state.problemi)
    if df.empty:
        st.write("Nessun problema da visualizzare.")
        return
    
    st.write("## Panoramica dei Problemi")
    
    # Tabella interattiva
    st.write("### Tabella dei Problemi")
    st.dataframe(df, use_container_width=True)
    
    # Statistiche di base
    st.write("### Statistiche di Base")
    st.write(f"Numero totale di problemi: {df.shape[0]}")
    st.write(f"Gravità media: {df['Gravità'].mean():.2f}")
    st.write(f"Impatto medio: {df['Impatto'].mean():.2f}")

    # Grafico a dispersione migliorato
    st.write("### Grafico a Dispersione di Gravità vs Impatto")
    fig, ax = plt.subplots()
    sns.scatterplot(x='Gravità', y='Impatto', data=df, ax=ax, hue='Gravità', palette='viridis', s=100, alpha=0.7)
    ax.set_title('Gravità vs Impatto')
    ax.set_xlabel('Gravità')
    ax.set_ylabel('Impatto')
    plt.grid(True)
    st.pyplot(fig)
    
    # Grafico a barre per la distribuzione dei problemi
    st.write("### Distribuzione dei Problemi per Gravità")
    fig, ax = plt.subplots()
    sns.countplot(x='Gravità', data=df, ax=ax, palette='viridis')
    ax.set_title('Distribuzione dei Problemi per Gravità')
    ax.set_xlabel('Gravità')
    ax.set_ylabel('Numero di Problemi')
    plt.grid(True)
    st.pyplot(fig)
    
    # Esportazione in CSV
    st.write("### Esporta Dati")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Scarica CSV",
        data=csv,
        file_name='problemi_report.csv',
        mime='text/csv'
    )

def suggerisci_soluzioni(descrizione_problema):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Proponi soluzioni per il seguente problema: {descrizione_problema}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    st.title("Gestione Problemi Aziendali")

    menu = st.sidebar.selectbox("Seleziona un'opzione", ["Aggiungi Problema", "Visualizza Problemi", "Suggerisci Soluzioni"])

    if menu == "Aggiungi Problema":
        st.header("Aggiungi un Nuovo Problema")
        descrizione = st.text_input("Descrizione del problema")
        gravità = st.slider("Gravità", 1, 5, 1)
        impatto = st.slider("Impatto", 1, 5, 1)
        data = st.date_input("Data")
        categoria = st.selectbox("Categoria", ["Amministrativa", "Tecnica", "Finanziaria", "Altro"])
        priorità = st.selectbox("Priorità", ["Alta", "Media", "Bassa"])
        note = st.text_area("Note aggiuntive")
        
        if st.button("Aggiungi Problema"):
            aggiungi_problema(descrizione, gravità, impatto, data, categoria, priorità, note)
            st.success("Problema aggiunto con successo!")

    elif menu == "Visualizza Problemi":
        st.header("Visualizza i Problemi")
        visualizza_problemi()

    elif menu == "Suggerisci Soluzioni":
        st.header("Suggerisci Soluzioni")
        problema = st.text_input("Descrizione del problema per cui vuoi suggerire soluzioni")
        
        if st.button("Suggerisci Soluzioni"):
            if problema:
                soluzioni = suggerisci_soluzioni(problema)
                st.write("## Soluzioni Suggerite")
                st.write(soluzioni)
            else:
                st.write("Inserisci una descrizione del problema.")

if __name__ == "__main__":
    main()
