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
API_ID = 27732327
API_HASH = "7c7c0a2b3b5dc1eb6b84433228dcf4c8"
USER_SESSION = environ.get("USER_SESSION", "BQGnKWcAlqPO45_eOHMD38mcvBXSHgppo0Kg8AChKgD40YJQHX7vVyrPffIiBbgcTJ8X60yiBDjJnUBaVcKI_rDZwjsbJ873wAWI63L8Z-s8LgGsPskeDO5GIqUrDQbm3RgGy4ecldViaxPaIm46h31I5GT9oX9A7M3N9MZgIUfbqo70pu0R7APjFNs35xiHnDBGkmA2yhE54eEOpZR5FJu8nXBHSV59U6k0eWqbxjzk3wb5qeN1gWwX1SvalaM7QcKePJRYdhP4c3vtR4CWm32RC1ModPsA1wxRP80Uy-6hygYRoSkiCiGoHIhDMKbevqWUHXC1jvfHre_avC0_TcgnMllUiwAAAAHVJZ9QAA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002216169351 -1002162221322').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7870979920').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
