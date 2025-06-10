from flask import Flask, render_template
from api_tennis import get_partidos_dia, get_proximos_eventos, get_h2h

app = Flask(__name__)

@app.route("/")
def index():
    partidos_raw = get_partidos_dia()
    partidos = []

    for p in partidos_raw:
        torneos_1 = get_proximos_eventos(p["jugador_1"])
        torneos_2 = get_proximos_eventos(p["jugador_2"])
        h2h = get_h2h(p["jugador_1"], p["jugador_2"])

        partidos.append({
            "jugador_1": p["jugador_1"],
            "jugador_2": p["jugador_2"],
            "torneos_1": torneos_1,
            "torneos_2": torneos_2,
            "h2h": h2h
        })

    return render_template("index.html", partidos=partidos)

if __name__ == "__main__":
    app.run(debug=True)
