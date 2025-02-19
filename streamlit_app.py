# Install
# pip install streamlit
# pip install pyngrok
# pip install plotly
# pip install joblib
# pip install scikit-learn
# pip install xgboost

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

st.title('🌍 Destin_AI_tion 🌍')
st.subheader("Find the perfect country for your ERASMUS or moving abroad in Europe")

# Titel der App
st.write("**Who are you? - Where do you come from, what do you believe in, what are ypu passionate about?**")
st.write("The decision to move to another country or spend an Erasmus semester abroad is probably one of the most exciting and challenging decisions in life. "
         "But which European country best suits your personality, values, attitudes and preferences? ")
st.write("This is exactly where our tool “DestinAItion” comes in. Using a data-based prediction model, we analyze your individual preferences and recommend the three most suitable European countries for your semester abroad or your emigration. ")
st.write("The following countries can be predicted in our model: Austria, Belgium, Bulgaria, Switzerland, Cyprus, Czech Republic, Germany, Denmark, Estonia, Spain, Finland, France, Great Britain, Croatia, "
         "Hungary, Ireland, Iceland, Italy, Lithuania, Latvia, Montenegro, Netherlands, Norway, Poland, Portugal, Serbia, Sweden, Slovenia, Slovakia")
# Eingabefelder
# Mapping von Ländernamen zu Ländercodes
st.divider()
country_map = {
    'Germany': 'DE', 'Austria': 'AT', 'Belgium': 'BE', 'Bulgaria': 'BG', 'Switzerland': 'CH', 'Cyprus': 'CY',
    'Czech Republic': 'CZ', 'Denmark': 'DK', 'Estonia': 'EE', 'Spain': 'ES',
    'Finland': 'FI', 'France': 'FR', 'United Kingdom': 'GB', 'Croatia': 'HR', 'Hungary': 'HU',
    'Ireland': 'IE', 'Iceland': 'IS', 'Italy': 'IT', 'Lithuania': 'LT', 'Latvia': 'LV', 'Montenegro': 'ME',
    'Netherlands': 'NL', 'Norway': 'NO', 'Poland': 'PL', 'Portugal': 'PT', 'Serbia': 'RS', 'Sweden': 'SE',
    'Slovenia': 'SI', 'Slovakia': 'SK'
}

# Wählen eines Landes aus der Liste (anzeigen der Ländernamen)
selected_country = st.selectbox(
    '**Where do you come from?**',
    list(country_map.keys())  # Nur die Ländernamen anzeigen
)
# Abrufen des Ländercodes im Hintergrund
cntry = country_map[selected_country]

# 1 Social contact
st.divider()
st.subheader("**1. Social contact and relationships**")

sclmeet = st.slider('How often do you meet socially with friends, relatives or work colleagues?', 1, 7)
st.caption("1 = Never| 3 = Once a month| 5 = Once a week | 7 = Every Day")

st.write(" ")
st.write("*How much does the following description match your personality?*")
iplylfr = st.slider('“It is important to me to be loyal to my friends. I want to devote myself to people close to me.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")
iphlppl = st.slider('“It is very important to me to help the people around me. I want to care for their well-being.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")


# 2 Religion and Ideology
st.divider()
st.subheader("**2. Religion and Ideology**")
# Mapping von angezeigten Optionen zu Variablennamen
religion_mapping = {
    'Roman Catholic': 'RomanCatholic',
    'Protestant': 'Protestant',
    'Eastern Orthodox': 'EasternOrthodox',
    'Jewish': 'Jewish',
    'Islam': 'Islam',
    'Eastern Religions': 'EasternReligions',
    'Other Christian Denomination': 'Other_Christian_denom',
    'Not applicable': 'NA'
}
# Auswahlfeld für die Religion
selected_religion = st.selectbox('What Religion do you belong to?',
                                 ['Roman Catholic',
                                  'Protestant',
                                  'Eastern Orthodox',
                                  'Jewish',
                                  'Islam',
                                  'Eastern Religions',
                                  'Other Christian Denomination',
                                  'Not applicable'])
# Zuordnung des ausgewählten Werts zu einer Variablen
selected_religion_var = religion_mapping[selected_religion]
st.write(" ")
# Erstellen der One-Hot-Encoding-Variablen
def create_one_hot_encoding(religion_choice):
    one_hot_dict = {
        'RomanCatholic': 0,
        'Protestant': 0,
        'EasternOrthodox': 0,
        'Other_Christian_denom': 0,
        'Jewish': 0,
        'Islam': 0,
        'EasternReligions': 0,
        'Other_NonChristian_rel': 0
    }
    if religion_choice == 'Roman Catholic':
        one_hot_dict['RomanCatholic'] = 1
    elif religion_choice == 'Protestant':
        one_hot_dict['Protestant'] = 1
    elif religion_choice == 'Eastern Orthodox':
        one_hot_dict['EasternOrthodox'] = 1
    elif religion_choice == 'Jewish':
        one_hot_dict['Jewish'] = 1
    elif religion_choice == 'Islam':
        one_hot_dict['Islam'] = 1
    elif religion_choice == 'Eastern Religions':
        one_hot_dict['EasternReligions'] = 1
    elif religion_choice == 'Other Christian Denomination':
        one_hot_dict['Other_Christian_denom'] = 1
    return one_hot_dict
# Generiere One-Hot-Encoding basierend auf der Auswahl
religion_one_hot = create_one_hot_encoding(selected_religion)

st.write("*How much does the following description match your personality?*")
imptrad = st.slider('“Tradition is important to me. I try to follow the customs handed down by my religion or my family.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")
bctprd = st.radio("Have you boycotted certain products during the last 12 months?", ('Yes', 'No'))


#3 Mindset / Values
st.divider()
st.subheader("**3. Mindset and Values**")

pplfair = st.slider('Do you think that most people would try to take advantage of you if they got the chance, or would they try to be fair?', 0, 10)
st.caption("0 =  Most people try to take advantage of me | 10 = Most people try to be fair")

ppltrst = st.slider('Would you say that most people can be trusted, or that you cannot be too careful in dealing with people?', 0, 10)
st.caption("0 =  You cannot be too careful | 10 = Most people can be trusted")

pplhlp = st.slider('Would you say that most of the time people try to be helpful or that they are mostly looking out for themselves?', 0, 10)
st.caption("0 =  People mostly look out for themselves| 10 = People mostly try to be helpful")

st.write(" ")
st.write("*How much does the following description match your personality?*")
ipudrst = st.slider('“It is important to me to listen to people who are different from me. Even when I disagree with them, I still want to understand them.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")
ipbhprp = st.slider('“It is important to me always to behave properly. I want to avoid doing anything people would say is wrong.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")
iprspot = st.slider('“It is important to me to get respect from others. I want people to do what I say.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")


#4 Politics and Europe
st.divider()
st.subheader("**4. Politics and Europe**")

trstep = st.slider('How much do you trust the European Parliament?', 0, 10)
st.caption("0 = No Trust at all | 10 = Complete Trust")

lrscale = st.slider("In politics people sometimes talk of 'left' and 'right'. Where would you place yourself on this scale, where 0 means left and 10 means right?", 0, 10)
st.caption("0 = Left | 10 = Right")

atcherp = st.slider('How emotionally attached do you feel to Europe?', 0, 10)
st.caption("0 = Not at all emotionally attached | 10 = Very emotionally attached")


#5 Satisfaction
st.divider()
st.subheader("**5. Satisfaction**")

stflife = st.slider('All things considered, how satisfied are you with your life as a whole nowadays?', 0, 10)
st.caption("0 = Extremely dissatisfied | 10 = Extremely satisfied")

happy = st.slider('Taking all things together, how happy would you say you are?', 0, 10)
st.caption("0 = Extremely unhappy | 10 = Extremely happy")

st.write(" ")
st.write("*How much does the following description match your personality?*")
ipgdtim = st.slider("“Having a good time is important to me. I like to 'spoil' myself.”", 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")
impfun = st.slider('“I seek every chance I can to have fun. It is important to me to do things that give me pleasure.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")


#6 Security
st.divider()
st.subheader("**6. Security**")
plnftr = st.slider('Do you generally plan for your future, or do you just take each day as it comes?', 0, 10)
st.caption("0 = I plan for my future as much as possible | 10 = I just take each day as it comes")
st.write(" ")
st.write("*How much does the following description match your personality?*")
impsafe = st.slider('“It is important to me to live in secure surroundings. I avoid anything that might endanger my safety.”', 1, 6)
st.caption("1 = Very much like me | 6 = Not like me at all")

# Speichern der Daten
st.divider()
if st.button('Click here for your result'):
    # Dictionary mit den Eingabewerten
    response_data = {
        'cntry': cntry,
        'trstep': trstep,
        'pplfair': pplfair,
        'ppltrst': ppltrst,
        'pplhlp': pplhlp,
        'lrscale': lrscale,
        'atcherp': atcherp,
        'stflife': stflife,
        'happy': happy,
        'sclmeet': sclmeet,
        'iplylfr': iplylfr,
        'ipgdtim': ipgdtim,
        'impsafe': impsafe,
        'iphlppl': iphlppl,
        'impfun': impfun,
        'ipudrst': ipudrst,
        'ipbhprp': ipbhprp,
        'imptrad': imptrad,
        'iprspot': iprspot,
        'plnftr': plnftr,
        'bctprd': 0 if bctprd == 'Ja' else 1,
        # Hier verwendest du das One-Hot-Encoding, das du vorher erstellt hast
        'RomanCatholic': religion_one_hot['RomanCatholic'],
        'Protestant': religion_one_hot['Protestant'],
        'EasternOrthodox': religion_one_hot['EasternOrthodox'],
        'Other_Christian_denom': religion_one_hot['Other_Christian_denom'],
        'Jewish': religion_one_hot['Jewish'],
        'Islam': religion_one_hot['Islam'],
        'EasternReligions': religion_one_hot['EasternReligions'],
        'Other_NonChristian_rel': religion_one_hot['Other_NonChristian_rel']
    }
    st.markdown('⏳ Please wait for a second. We will check for your perfect fit!')
    st.divider()

    # Speichern der Eingabedaten in einen DataFrame für direkte Weiterverarbeitung
    responses_data = pd.DataFrame([response_data])  # DataFrame mit einer Zeile

    # Standardisierung der Eingabedaten
    # Lade den gespeicherten Scaler
    scaler_z = joblib.load('scaler_europa.joblib')
    df_features = responses_data.drop(columns=['cntry'])
    # Wende den StandardScaler auf die Eingabedaten an
    df_scaled = pd.DataFrame(scaler_z.transform(df_features), columns=df_features.columns)
    # Füge die 'cntry'-Spalte wieder hinzu (wird nicht standardisiert)
    df_scaled['cntry'] = responses_data['cntry']

    # XGBoost-Modell laden
    xgboost_model = joblib.load('xgboost_model.joblib')
    # LabelEncoder für die Rückübersetzung der Vorhersage laden
    le = joblib.load('label_encoder.joblib')  # Wenn du den LabelEncoder gespeichert hast

    # Funktion zur Vorhersage mit XGBoost (inkl. Wahrscheinlichkeiten)
    def predict_with_xgboost(xgboost_model, df_scaled):
        # Stelle sicher, dass df_scaled nur die Features enthält, keine Zielvariable (z.B. 'cntry')
        df_scaled = df_scaled.drop(columns=['cntry'])
        # Konvertiere df_scaled in ein numpy.ndarray
        scaled_array = df_scaled.values
        # Vorhersage mit Wahrscheinlichkeiten für alle Klassen
        probabilities = xgboost_model.predict_proba(scaled_array)
        return probabilities

    # Vorhersagewahrscheinlichkeiten erhalten
    probabilities = predict_with_xgboost(xgboost_model, df_scaled)

    # Label der Klassen (Ländercodes)
    class_labels = le.classes_
    # Sortiere die Wahrscheinlichkeiten in absteigender Reihenfolge
    sorted_indices = probabilities[0].argsort()[::-1]
    sorted_country_codes = class_labels[sorted_indices]

    # Ursprünglich eingegebenes Land
    original_country_code = df_scaled['cntry'].values[0]
    # Filtere das eigene Land aus den Top-Ergebnissen
    top_countries = [code for code in sorted_country_codes if code != original_country_code]
    # Wähle die Top 3 (ohne das eigene Land)
    top_3_countries = top_countries[:3]

    # Umwandlung der Länderkürzel in die vollständigen Ländernamen
    top_3_country_names = []
    for code in top_3_countries:
        for country, country_code in country_map.items():
            if country_code == code:
                top_3_country_names.append(f"{country} ({code})")
                break

    # Ausgabe der Vorhersagen
    st.subheader("Top 3 suggestions based on your survey data:")
    for i, country in enumerate(top_3_country_names, start=1):
        st.write(f"{i}. {country}")


    ## Visualisierung
    # Barchart
    # Extrahiere die Wahrscheinlichkeiten der Top 3 Länder
    top_3_probs = probabilities[0][sorted_indices[:3]]
    # Erstelle einen DataFrame für die Visualisierung
    df_plot = pd.DataFrame({
        "Country": top_3_country_names,
        "Probability": top_3_probs
    })
    # Balkendiagramm
    fig = px.bar(df_plot, x="Country", y="Probability", text="Probability",
                 labels={"Probability": "Prediction Confidence"})
    # Werte auf den Balken anzeigen
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    fig.update_layout(yaxis=dict(range=[0, max(top_3_probs) * 1.2]))  # 20% mehr Platz oben
    # Diagramm in Streamlit anzeigen
    st.plotly_chart(fig)


    # Europakarte
    # Koordinaten der Länder (Mapping-Tabelle mit Ländern und Koordinaten)
    country_coords = {
        "Germany": [51.1657, 10.4515],
        "France": [46.6034, 1.8883],
        "Spain": [40.4637, -3.7492],
        "Croatia": [45.1, 15.2],
        "Austria": [47.5162, 14.5501],
        "Belgium": [50.8503, 4.3517],
        "Bulgaria": [42.7339, 25.4858],
        "Switzerland": [46.8182, 8.2275],
        "Czech Republic": [49.8175, 15.4729],
        "Denmark": [56.2639, 9.5018],
        "Estonia": [58.5953, 25.0136],
        "Finland": [61.9241, 25.7482],
        "United Kingdom": [55.3781, -3.4360],
        "Hungary": [47.1625, 19.5033],
        "Ireland": [53.1424, -7.6921],
        "Iceland": [64.9631, -19.0208],
        "Italy": [41.8719, 12.5674],
        "Lithuania": [55.1694, 23.8813],
        "Latvia": [56.8796, 24.6032],
        "Montenegro": [42.7087, 19.3744],
        "Netherlands": [52.1326, 5.2913],
        "Norway": [60.4720, 8.4689],
        "Poland": [51.9194, 19.1451],
        "Portugal": [39.3999, -8.2245],
        "Serbia": [44.0165, 21.0059],
        "Sweden": [60.1282, 18.6435],
        "Slovenia": [46.1512, 14.9955],
        "Slovakia": [48.6690, 19.6990]
    }

    # Extrahiere die Koordinaten der Top 3 Länder
    latitudes = [country_coords[c.split(" (")[0]][0] for c in top_3_country_names]
    longitudes = [country_coords[c.split(" (")[0]][1] for c in top_3_country_names]
    # Nummerierung für die Punkte (1, 2, 3)
    labels = [f"{i + 1}" for i in range(len(latitudes))]
    # Der erste Platz erhält den größten Marker, der dritte den kleineren
    marker_sizes = [25, 20, 15]
    # Erstelle die Karte für rechteckige Darstellung
    fig = go.Figure(go.Scattermapbox(
        lon=longitudes,
        lat=latitudes,
        mode="markers",
        marker=go.scattermapbox.Marker(size=marker_sizes, color='blue'),
    ))
    # Layout anpassen
    fig.update_layout(
            mapbox=dict(
            style="carto-positron",  # Alternativ: "open-street-map", "stamen-terrain"
            center={"lat": 50, "lon": 10},  # Weiter südlich für besseren Europa-Ausschnitt
            zoom=2.3,  # Weiter herausgezoomt, um Südeuropa & Island anzuzeigen
        ),
        margin={"r": 0, "t": 40, "l": 0, "b": 0}  # Keine Ränder
    )
    st.plotly_chart(fig)
