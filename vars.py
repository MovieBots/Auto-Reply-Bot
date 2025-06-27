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
USER_SESSION = environ.get("USER_SESSION", "BQGnKWcAJ8qon2MNSAOXZl89b8t9Tleu7SUelCyN5rX5cwdUTLv5Xnx4_bNPiX0i_g8B0k3FoBVt0tleUo3SXJF0JpAz8Rws3vXjRh5UciiLd80kxGPuCn5EDoJ5FFk_zpUSfo0R-RINuTFYGZp2L3VYxv50xRRfue-SsFkmwwcm4epjYUrddXOQphU8STbpl0c0D3Kf3L7mMMyVfq14OD0od4HCTsJoTuNUfKMb7k7yPfsh4uNnde6dIYNnePRB2ff89HKqvd3I4qtNwRWxlAjFFJ6onMlnjqS801ulekDS7qXX6xiwXlruBobPsAtfuYND69vsZqrC0jcUaKHQxIrxB9LArQAAAAHVJZ9QAA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002216169351 -1002162221322').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7870979920').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
