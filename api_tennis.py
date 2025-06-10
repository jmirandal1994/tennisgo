import requests

API_KEY = "4e176b2831a6f058cd842511d5d2928cd6ebca5d4dca9e7b5015a00968f1f1af"
BASE_URL = "https://api.api-tennis.com/tennis/"

def get_partidos_dia():
    url = f"{BASE_URL}?method=get_events&APIkey={API_KEY}&timezone=America/Santiago"
    res = requests.get(url)
    data = res.json()

    partidos = []
    if data.get("result"):
        for match in data["result"]:
            jugador_1 = match.get("event_home_team", "")
            jugador_2 = match.get("event_away_team", "")

            if jugador_1 and jugador_2:
                partidos.append({
                    "jugador_1": jugador_1,
                    "jugador_2": jugador_2
                })
    return partidos

def get_proximos_eventos(jugador):
    url = f"{BASE_URL}?method=get_fixtures&APIkey={API_KEY}&player={jugador}"
    res = requests.get(url).json()
    eventos = []

    if res.get("result"):
        for item in res["result"]:
            if any(x in item["league_name"].lower() for x in ["qual", "atp", "challenger"]):
                eventos.append({
                    "torneo": item["league_name"],
                    "fecha": item["event_date"],
                    "es_importante": True
                })
    return eventos

def get_h2h(jugador_1, jugador_2):
    url = f"{BASE_URL}?method=get_H2H&APIkey={API_KEY}&player1={jugador_1}&player2={jugador_2}"
    res = requests.get(url).json()
    if res.get("result"):
        return res["result"]
    return []
