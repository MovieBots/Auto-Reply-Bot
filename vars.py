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
USER_SESSION = environ.get("USER_SESSION", "AQG3ptsAVSzj1mhUoer0hCY3lwK7xFRC2TCxmHXtvTKMCh7dbotRvVbWoKml6dUyC8KwwmiCujvNlWfGHKLhFg8iWpoiZShKgIoHJwu__9jDmHKp_JYX4CyDG3aslanYLNLdX9iG1kLwm5p0uJJZXurxpyj8fSTesZgegsQpg8zFSMlXEwZ3cDcMx5frGIgi1dY4Q-K-gzziBcI9xAPJwojUNySmN6gHkQEaDhm_VDyyUGgAP9EWRZBUZw43TTvbUoe8idlO2m36-WryIfVtYqkO3ybkUfDFeVYqGhxVDEyVPmJ71KQ8Nox2XJz6vKXy1xQCAM-1P0u7_68zJiBBUIY6LUflLAAAAAHXYvYoAA")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002074744533"))
FROM_GRP = [int(channel_id) for channel_id in environ.get('FROM_GRP', '-1002216169351 -1002162221322 -1001619702173').split() if re.match(r'^-?\d+$', channel_id)]
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7908554280').split()]
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/MovieBots/Auto-Reply-Bot")
