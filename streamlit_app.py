import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lista per memorizzare i problemi
problemi = []

def aggiungi_problema(descrizione, gravità, impatto, data):
    problema = {
        'Descrizione': descrizione,
        'Gravità': gravità,
        'Impatto': impatto,
        'Data': data
    }
    problemi.append(problema)

def visualizza_problemi():
    df = pd.DataFrame(problemi)
    if df.empty:
        print("Nessun problema da visualizzare.")
        return
    
    # Mostra la panoramica dei problemi
    print("\nPanoramica dei Problemi:")
    print(df)
    
    # Creazione di un grafico a dispersione basato su Gravità e Impatto
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Gravità'], df['Impatto'], alpha=0.7)
    plt.title('Panoramica dei Problemi')
    plt.xlabel('Gravità')
    plt.ylabel('Impatto')
    plt.grid(True)
    plt.show()

def menu():
    while True:
        print("\n1. Aggiungi Problema")
        print("2. Visualizza Problemi")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            descrizione = input("Descrizione del problema: ")
            gravità = int(input("Gravità (1-5): "))
            impatto = int(input("Impatto (1-5): "))
            data = input("Data (YYYY-MM-DD): ")
            aggiungi_problema(descrizione, gravità, impatto, data)
        elif scelta == '2':
            visualizza_problemi()
        elif scelta == '3':
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    menu()
