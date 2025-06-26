from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "N2 Auto Reply Bot")
API_ID = 29236719
API_HASH = "1ccf1bd0a86af974e3210a55f662c062"
USER_SESSION = environ.get("USER_SESSION", "1BVtsOMEBu2I5WvSpxWG9nE6eM1WQHJ5q50D4XVIqd7-3vpI49sxR6yZfWNURzs4d6mjhJ2W41VR_Jo_nXSJJX69_N9WHv9OdjOUbtTciBs7BtcyKqMPO3eXGiWKml8hQ-u0SxFnXcQN_3XN9dvu4vChNjLM5h2YjaAcrYePhlQOZ2O3UJwnv9shC5wJuSxOxpM1w5e8pP5ltk7SbB2uEi5MetaXHvP90hK7MSR8Rp0qzvtZ1hLccgrxux33_P-AVPGobKLZLbVuVU4ZxSnX53jo8S_sKt1di32ovt-xvY-T5XhPrTNIPK3MFdud4Y3eYsEDlOcMFoBfOjObeIKt7Q457-m0Gg4M=")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002216169351 -1002162221322').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '893383574').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
