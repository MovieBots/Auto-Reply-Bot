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
USER_SESSION = environ.get("USER_SESSION", "1BQF-avYAoJqURYzL8gPjnlAZE5J9eVuASycYkZ8AugvjVX2HoiknYVDm5a2Z_Ft6PHkHCRK57j-KVLBETnaP2Wqy2XmoT9EJ7mWTSAalJP5eG_-gIkco_nZkfDCpuxz4NdW5xmSILpJInR5IN1_B_oF3MWQYR3iNQpbSX8ZurhmzA2vtJKguTsavIcMkp2SlF0L0XC5WTaLUDvdveirQCuEzPK91N6uiUu-pK7fHDcgnyaaI7xDWCp3tgHincqPFkJMlL0Xssqjod1ZpXE8bLbuTIsBxAPzJ66-Stfeek3Sz6HZPMOUaN-Bm3hrfQjB4ampIDeiTYwTrGFkGiQbsIUGC2-_VZQAAAAF3rvI7AA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002455191730 -100245519173 -1002686704351 -100268670435').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6302921275 893383574').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")