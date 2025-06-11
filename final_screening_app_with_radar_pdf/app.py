
import streamlit as st

st.set_page_config(page_title="Prédiction du Risque de Blessure", layout="wide")

st.title("🩺 Application de Prédiction du Risque de Blessure Sportive")
st.markdown("Remplis les données ci-dessous pour estimer ton risque de blessure et sa localisation probable.")

# Formulaire de saisie utilisateur
with st.form("user_data"):
    st.subheader("📊 Données de l'Athlète")

    col1, col2, col3 = st.columns(3)

    with col1:
        dorsiflexion = st.slider("Amplitude dorsiflexion (en °)", 0, 40, 20)
        adducteur_strength = st.slider("Force adducteurs (en kg)", 0, 100, 50)
        vertical_jump = st.slider("Saut vertical (cm)", 10, 100, 50)

    with col2:
        sprint_time = st.number_input("Temps sprint 10m (s)", 1.0, 10.0, 2.5)
        squat_1RM = st.slider("Squat 1RM (kg)", 0, 200, 100)
        charge_var = st.slider("Variation charge entraînement (%)", 0, 100, 20)

    with col3:
        fatigue = st.slider("Fatigue perçue (1: faible, 5: forte)", 1, 5, 3)
        sommeil = st.slider("Qualité du sommeil (1: très mauvais, 5: excellent)", 1, 5, 3)
        historique_blessure = st.selectbox("Blessure antérieure ?", ["Aucune", "Cheville", "Ischio", "Adducteurs"])

    submit = st.form_submit_button("Analyser le risque")

# Analyse simplifiée heuristique
if submit:
    score = 0
    localisation = set()
    facteurs = []

    if dorsiflexion < 15:
        localisation.add("Cheville")
        score += 2
        facteurs.append("Amplitude de dorsiflexion faible (<15°)")

    if adducteur_strength < 40:
        localisation.add("Adducteurs")
        score += 2
        facteurs.append("Faible force des adducteurs (<40kg)")

    if sprint_time > 3.5:
        localisation.add("Ischio-jambiers")
        score += 2
        facteurs.append("Sprint lent (>3.5s)")

    if squat_1RM < 80:
        localisation.add("Genou")
        score += 1
        facteurs.append("Force générale insuffisante (Squat <80kg)")

    if vertical_jump < 40:
        localisation.add("Explosivité basse")
        score += 1
        facteurs.append("Explosivité réduite (saut <40cm)")

    if charge_var > 40:
        score += 2
        facteurs.append("Grande variation de charge (>40%)")

    if fatigue >= 4 or sommeil <= 2:
        score += 2
        facteurs.append("Fatigue élevée ou mauvais sommeil")

    if historique_blessure != "Aucune":
        localisation.add(historique_blessure)
        score += 2
        facteurs.append(f"Antécédent de blessure ({historique_blessure})")

    # Évaluation du niveau de risque
    if score <= 3:
        risque = "Faible"
        couleur = "🟢"
    elif score <= 6:
        risque = "Modéré"
        couleur = "🟠"
    else:
        risque = "Élevé"
        couleur = "🔴"

    st.subheader("🧠 Résultat de l'analyse")
    st.markdown(f"**Risque estimé : {couleur} {risque}**")
    st.markdown(f"**Localisation(s) probable(s) :** {', '.join(localisation) if localisation else 'Non déterminée'}")
    st.markdown("### 🔍 Facteurs identifiés :")
    for f in facteurs:
        st.markdown(f"- {f}")
