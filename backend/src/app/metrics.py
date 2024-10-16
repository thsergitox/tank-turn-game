from prometheus_client import Counter, Gauge

LOGGEDIN_PLAYERS = Counter(
    "loggedin_player_total", "Total logged ins by player", ["player_name"]
)
REGISTERED_PLAYERS = Counter(
    "register_player_total", "Total number of registered players ", ["player_name"]
)

TOTAL_DAMAGE = Gauge("total_damage", "Total damage done by player", ["player_name"])

TOTAL_GAMES = Gauge("total_games", "Total games played by player", ["player_name"])
