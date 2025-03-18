import pandas as pd
import json
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import plugins
import matplotlib.pyplot as plt
import branca.colormap as cm

# Sidebar met tabbladen
pagina = st.sidebar.radio("Selecteer een pagina", ['Kaart', 'Fiets vs Weer'])

@st.cache_data
def load_data_metro():
    bez_2007 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2007_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2008 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2008_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2009 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2009_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2010 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2010_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2011 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2011_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2012 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2012_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2013 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2013_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2014 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2014_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2015 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2015_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2016 = pd.read_csv(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2016_Entry_Exit.csv", dtype=str, low_memory=False)
    bez_2017 = pd.read_excel(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2017_Entry_Exit.xlsx", dtype=str)
    bez_2018 = pd.read_excel(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2018_Entry_Exit.xlsx", dtype=str)
    bez_2019 = pd.read_excel(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2019_Entry_Exit.xlsx", dtype=str)
    bez_2020 = pd.read_excel(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2020_Entry_Exit.xlsx", dtype=str)
    bez_2021 = pd.read_excel(r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\2021_Entry_Exit.xlsx", dtype=str)
    return bez_2007, bez_2008, bez_2009, bez_2010, bez_2011, bez_2012, bez_2013, bez_2014, bez_2015, bez_2016, bez_2017, bez_2018, bez_2019, bez_2020, bez_2021

bez_2007, bez_2008, bez_2009, bez_2010, bez_2011, bez_2012, bez_2013, bez_2014, bez_2015, bez_2016, bez_2017, bez_2018, bez_2019, bez_2020, bez_2021 = load_data_metro()

@st.cache_data
def load_data_fiets():
    jun2021_1 = pd.read_csv('./Data/Fiets data/267JourneyDataExtract26May2021-01Jun2021.csv')
    jun2021_2 = pd.read_csv('./Data/Fiets data/268JourneyDataExtract02Jun2021-08Jun2021.csv')
    jun2021_3 = pd.read_csv('./Data/Fiets data/269JourneyDataExtract09Jun2021-15Jun2021.csv')
    jun2021_4 = pd.read_csv('./Data/Fiets data/270JourneyDataExtract16Jun2021-22Jun2021.csv')
    jun2021_5 = pd.read_csv('./Data/Fiets data/271JourneyDataExtract23Jun2021-29Jun2021.csv')
    jun2021_6 = pd.read_csv('./Data/Fiets data/272JourneyDataExtract30Jun2021-06Jul2021.csv')

    dec2021_1 = pd.read_csv('./Data/Fiets data/294JourneyDataExtract01Dec2021-07Dec2021.csv')
    dec2021_2 = pd.read_csv('./Data/Fiets data/295JourneyDataExtract08Dec2021-14Dec2021.csv')
    dec2021_3 = pd.read_csv('./Data/Fiets data/296JourneyDataExtract15Dec2021-21Dec2021.csv')
    dec2021_4 = pd.read_csv('./Data/Fiets data/297JourneyDataExtract22Dec2021-28Dec2021.csv')
    dec2021_5 = pd.read_csv('./Data/Fiets data/298JourneyDataExtract29Dec2021-04Jan2022.csv')

    jun2022_1 = pd.read_csv('./Data/Fiets data/320JourneyDataExtract01Jun2022-07Jun2022.csv')
    jun2022_2 = pd.read_csv('./Data/Fiets data/321JourneyDataExtract08Jun2022-14Jun2022.csv')
    jun2022_3 = pd.read_csv('./Data/Fiets data/322JourneyDataExtract15Jun2022-21Jun2022.csv')
    jun2022_4 = pd.read_csv('./Data/Fiets data/323JourneyDataExtract22Jun2022-28Jun2022.csv')
    jun2022_5 = pd.read_csv('./Data/Fiets data/324JourneyDataExtract29Jun2022-05Jul2022.csv')

    dec2022_1 = pd.read_csv('./Data/Fiets data/346JourneyDataExtract28Nov2022-04Dec2022.csv')
    dec2022_2 = pd.read_csv('./Data/Fiets data/347JourneyDataExtract05Dec2022-11Dec2022.csv')
    dec2022_3 = pd.read_csv('./Data/Fiets data/348JourneyDataExtract12Dec2022-18Dec2022.csv')
    dec2022_4 = pd.read_csv('./Data/Fiets data/349JourneyDataExtract19Dec2022-25Dec2022.csv')
    dec2022_5 = pd.read_csv('./Data/Fiets data/350JourneyDataExtract26Dec2022-01Jan2023.csv')

    jun2023_1 = pd.read_csv('./Data/Fiets data/372JourneyDataExtract29May2023-04Jun2023.csv')
    jun2023_2 = pd.read_csv('./Data/Fiets data/373JourneyDataExtract05Jun2023-11Jun2023.csv')
    jun2023_3 = pd.read_csv('./Data/Fiets data/374JourneyDataExtract12Jun2023-18Jun2023.csv')
    jun2023_4 = pd.read_csv('./Data/Fiets data/375JourneyDataExtract19Jun2023-30Jun2023.csv')

    dec2023_1 = pd.read_csv('./Data/Fiets data/385JourneyDataExtract01Dec2023-14Dec2023.csv')
    dec2023_2 = pd.read_csv('./Data/Fiets data/386JourneyDataExtract15Dec2023-31Dec2023.csv')
    return jun2021_1, jun2021_2, jun2021_3, jun2021_4, jun2021_5, jun2021_6, dec2021_1, dec2021_2, dec2021_3, dec2021_4, dec2021_5, jun2022_1, jun2022_2, jun2022_3, jun2022_4, jun2022_5, dec2022_1, dec2022_2, dec2022_3, dec2022_4, dec2022_5, jun2023_1, jun2023_2, jun2023_3, jun2023_4, dec2023_1, dec2023_2

# Laad de dataframes
jun2021_1, jun2021_2, jun2021_3, jun2021_4, jun2021_5, jun2021_6, dec2021_1, dec2021_2, dec2021_3, dec2021_4, dec2021_5, jun2022_1, jun2022_2, jun2022_3, jun2022_4, jun2022_5, dec2022_1, dec2022_2, dec2022_3, dec2022_4, dec2022_5, jun2023_1, jun2023_2, jun2023_3, jun2023_4, dec2023_1, dec2023_2 = load_data_fiets()

# # Voeg ze samen
# jun2021 = pd.concat([jun2021_1, jun2021_2, jun2021_3, jun2021_4, jun2021_5, jun2021_6], ignore_index=True)
# dec2021 = pd.concat([dec2021_1, dec2021_2, dec2021_3, dec2021_4, dec2021_5], ignore_index=True)
# jun2022 = pd.concat([jun2022_1, jun2022_2, jun2022_3, jun2022_4, jun2022_5], ignore_index=True)
# dec2022 = pd.concat([dec2022_1, dec2022_2, dec2022_3, dec2022_4, dec2022_5], ignore_index=True)
# jun2023 = pd.concat([jun2023_1, jun2023_2, jun2023_3, jun2023_4], ignore_index=True)
# dec2023 = pd.concat([dec2023_1, dec2023_2], ignore_index=True)

@st.cache_data
def load_data_weer():
    weer = pd.read_csv("./Data/Weer data/weather_london.csv", dtype=str, low_memory=False)
    return weer

# Cache the loading of train lines using st.cache_data
@st.cache_data
def load_train_lines():
    link_train_lines = r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\London Train Lines.JSON"
    with open(link_train_lines, "r", encoding="utf-8") as b:
        data = json.load(b)
    features = data["features"]
    train_lines = pd.json_normalize(features, sep="_")
    return train_lines

# Cache the loading of stations using st.cache_data
@st.cache_data
def load_stations():
    link_station1 = r"C:\Users\tomgo\OneDrive\Bureaublad\Data Science\Case 3 - Londen\Data\Londen data\London stations.JSON"
    with open(link_station1, "r", encoding="utf-8") as a:
        data = json.load(a)
    features = data["features"]
    station1 = pd.json_normalize(features, sep="_")
    return station1

station1 = load_stations()


if "pagina" in locals() and pagina == "Kaart":
    @st.cache_resource
    def create_m():
        zone_colors = {
            "1": "red",
            "2": "orange",
            "3": "yellow",
            "4": "lime",
            "5": "cyan",
            "6": "blue"
        }

        m = folium.Map(location=[51.517544, -0.010726], zoom_start=10)
        plugins.Draw().add_to(m)

        station1 = load_stations()

        for _, row in station1.iterrows():
            coords = row['geometry_coordinates']
            lat, lon = coords[1], coords[0]
            zone = row.get("properties_zone", "6")
            color = zone_colors.get(zone, "gray")

            folium.CircleMarker(
                location=[lat, lon],
                radius=8,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                popup=row["properties_name"]
            ).add_to(m)
        
        return m  # Zorg dat return buiten de for-loop staat

    st.title("London Metro Map")

    m = create_m()
    st_folium(m, width=700, height=500)


    datasets = {
    '2007': bez_2007,
    '2008': bez_2008,
    '2009': bez_2009,
    '2010': bez_2010,
    '2011': bez_2011,
    '2012': bez_2012,
    '2013': bez_2013,
    '2014': bez_2014,
    '2015': bez_2015,
    '2016': bez_2016
}

# Dropdown voor het selecteren van het jaar
    year = st.selectbox("Kies een jaar", options=list(datasets.keys()))

# Haal de geselecteerde dataset op
    dataset = datasets[year]

# Hardcoded kolom die je wilt gebruiken voor de visualisatie
    column = 'AnnualEntryExit_Mill'  # De kolom die je wilt visualiseren
    column1 = 'Station'  # Kolom die stationnamen bevat

# Zorg ervoor dat de data numeriek zijn
    dataset[column] = pd.to_numeric(dataset[column], errors='coerce')

# Creëer de kaart
    def create_p():
        p = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Londen coördinaten

    # Bepaal de min/max van de geselecteerde kolom
        # vmin = dataset[column].min()
        # vmax = dataset[column].max()
        vmin = 0
        vmax = 100

    # Creëer een lineaire colormap (groen -> geel -> rood)
        colormap = cm.LinearColormap(colors=['green', 'yellow', 'red'], vmin=vmin, vmax=vmax)
        colormap.caption = f'{column} (in miljoenen)'  # Voeg de gekozen kolomnaam toe aan de colormap
        p.add_child(colormap)

    # Itereer over de stations en pas de juiste kleuren toe
        for idx, row in station1.iterrows():
            station_name = row["properties_name"]  # Stationnaam uit station1
        # Zoek de waarde voor de gekozen kolom voor het station
            value = dataset[dataset[column1] == station_name][column].values

            if len(value) > 0:
                value = value[0]  # Haal de eerste waarde uit de lijst (aangenomen dat het unieke station is)
            else:
                value = None  # Geen waarde gevonden

            if pd.isna(value):
            # Geen data gevonden? Gebruik een standaard kleur
                continue
            else:
            # Bepaal de kleur op basis van de colormap
                color = colormap(value)

        # Haal de coördinaten op (ervan uitgaande dat dit [lon, lat] is)
            coords = row['geometry_coordinates']
            lon, lat = coords[0], coords[1]

        # Voeg de marker toe aan de kaart
            folium.CircleMarker(
                location=[lat, lon],
                radius=8,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                popup=f"{station_name}: {value}"
            ).add_to(p)

        return p

# Titel van de pagina
    st.title(f"London Metro Map met {column} Data - {year}")

# Genereer de kaart
    p = create_p()

# Toon de kaart in Streamlit
    st_folium(p, width=700, height=500)



elif pagina == "Fiets vs Weer":
    st.title("Fietsritten vs Weer in Londen")

    # Fietsdata-bestanden laden
    fiets_files = [
        "./Data/Fiets data/267JourneyDataExtract26May2021-01Jun2021.csv",
        "./Data/Fiets data/268JourneyDataExtract02Jun2021-08Jun2021.csv",
        "./Data/Fiets data/269JourneyDataExtract09Jun2021-15Jun2021.csv",
        "./Data/Fiets data/270JourneyDataExtract16Jun2021-22Jun2021.csv",
        "./Data/Fiets data/271JourneyDataExtract23Jun2021-29Jun2021.csv",
        "./Data/Fiets data/272JourneyDataExtract30Jun2021-06Jul2021.csv",
    ]

    # Alle fietsdata samenvoegen
    fiets_data = pd.concat([pd.read_csv(file) for file in fiets_files], ignore_index=True)

    # Datumkolommen converteren naar datetime-formaat
    fiets_data["Start Date"] = pd.to_datetime(fiets_data["Start Date"], format="%d/%m/%Y %H:%M")

    # Groeperen op dag en tellen van ritten
    fiets_data["Date"] = fiets_data["Start Date"].dt.date
    fiets_per_dag = fiets_data.groupby("Date").size().reset_index(name="Total Rides")

    # Weerdata inladen
    weather_data = pd.read_csv("./Data/Weer data/weather_london.csv")

    # Datumkolom hernoemen en converteren
    weather_data.rename(columns={"Unnamed: 0": "date"}, inplace=True)
    weather_data["date"] = pd.to_datetime(weather_data["date"], format="%Y-%m-%d")

    # Beschikbare weeropties
    weer_opties = {
        "Gemiddelde Temperatuur (°C)": "tavg",
        "Minimale Temperatuur (°C)": "tmin",
        "Maximale Temperatuur (°C)": "tmax",
        "Neerslag (mm)": "prcp",
        "Windkracht (m/s)": "wspd",
        "Luchtdruk (hPa)": "pres"
    }

    # Dropdown voor weerfactor
    weer_keuze = st.selectbox("Kies een weerfactor:", list(weer_opties.keys()))

    # Data combineren op datum
    fiets_per_dag["Date"] = pd.to_datetime(fiets_per_dag["Date"])
    toegevoegde_data = weather_data[["date", weer_opties[weer_keuze]]]
    merged_data = fiets_per_dag.merge(toegevoegde_data, left_on="Date", right_on="date", how="inner")
    merged_data = merged_data[["Date", "Total Rides", weer_opties[weer_keuze]]]

    # Gecombineerde grafiek plotten
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(merged_data["Date"], merged_data["Total Rides"], color='b', label="Aantal Fietsritten")
    ax1.set_xlabel("Datum")
    ax1.set_ylabel("Aantal Fietsritten", color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    ax2 = ax1.twinx()
    ax2.plot(merged_data["Date"], merged_data[weer_opties[weer_keuze]], color='r', linestyle="dashed", label=weer_keuze)
    ax2.set_ylabel(weer_keuze, color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    fig1.suptitle(f"Aantal fietsritten vs {weer_keuze} in Londen (Mei - Juli 2021)")
    fig1.autofmt_xdate()

    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")

    # Grafiek tonen
    st.pyplot(fig1)