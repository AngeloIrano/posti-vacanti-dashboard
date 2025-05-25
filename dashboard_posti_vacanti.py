
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Posti Vacanti", layout="wide")

# Dati ISTAT e Excelsior simulati da analisi precedente
dati = {
    "Settore": ["Industria", "Servizi"],
    "Posizioni lavorative stimate": [5_000_000, 13_000_000],
    "Tasso ISTAT (%)": [1.4, 1.8],
    "Posti vacanti ISTAT": [70000, 234000],
    "Posti vacanti Excelsior": [81820, 324450]
}

df = pd.DataFrame(dati)
df["Gap assoluto"] = df["Posti vacanti Excelsior"] - df["Posti vacanti ISTAT"]
df["Rapporto Exc/ISTAT"] = df["Posti vacanti Excelsior"] / df["Posti vacanti ISTAT"]
df["Indice ISTAT (/1000)"] = df["Posti vacanti ISTAT"] / df["Posizioni lavorative stimate"] * 1000
df["Indice Excelsior (/1000)"] = df["Posti vacanti Excelsior"] / df["Posizioni lavorative stimate"] * 1000

st.title("Dashboard Posti Vacanti - Q1 2025")
st.subheader("Confronto ISTAT vs Excelsior")

st.dataframe(df)

# Grafico comparativo
st.subheader("Grafico comparativo dei posti vacanti")
fig, ax = plt.subplots()
bar_width = 0.35
x = range(len(df))

ax.bar(x, df["Posti vacanti ISTAT"], bar_width, label="ISTAT")
ax.bar([i + bar_width for i in x], df["Posti vacanti Excelsior"], bar_width, label="Excelsior")

ax.set_xticks([i + bar_width / 2 for i in x])
ax.set_xticklabels(df["Settore"])
ax.set_ylabel("Posti vacanti")
ax.set_title("Posti vacanti per settore")
ax.legend()
st.pyplot(fig)

# Indicatori
st.subheader("Indicatori chiave di mismatch")
st.write(f"**Gap totale (posti vacanti):** {df['Gap assoluto'].sum():,.0f}")
st.write(f"**Rapporto medio Excelsior / ISTAT:** {df['Rapporto Exc/ISTAT'].mean():.2f}")
