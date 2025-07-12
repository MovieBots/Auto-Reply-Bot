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
API_ID = 28813019
API_HASH = "cc02b3685457d3109515657346ed5cfd"
USER_SESSION = environ.get("USER_SESSION", "1AZWarzQBu2g_-639cBPi3dFsomic5vTSMc08koRpBKNwQiOFxQMoPyOHL64zRnRW8UdzMAFDqMYiIiup5S_PW3abPHmXblfp46Suo8v4B3IWgRDDqoy582UAqFqYqOY0p7p4T8swRS9BYrAkhl2dVGeOqURN4fnoaXEv6uyyYfK1ufAisQfubb5RO92EQXmgP78IbZsnGGK9-r0Pp66OGAf8udI80hpxh_ZQTeFfq-Ko4bVHL_8CQsynhpTA4gWZM-nwfFgPTKsVJp_9YD5qNMOd1X0aZdrxbV3Y7BuyQoMV91Jw4UjMKC8CP_NBBtdK0RLcGbXSHtnkst_1HR51g95aXu9CW6Y=")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002216169351 -1002162221322 -1001619702173').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7908554280').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
