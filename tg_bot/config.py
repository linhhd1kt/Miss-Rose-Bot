if not __name__.endswith("config"):
    import sys
    print("The READMEXXXX is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1714273741:AAGSG3cG73cJeXpz8RXens1AKw5VutOAIRw"
    OWNER_ID = "1714273741" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "TAGSupportBot"

    # RECOMMENDED
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/tgbot'  # needed for any database modules
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@localhost/tgbot'
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
#     ['admin', 'afk', 'antiflood', 'backups', 'bans', 'blacklist', 'connection', 'cust_filters', 'disable', 'extras', 'global_bans', 'global_kick', 'global_mutes', 'keyboard', 'locks', 'log_channel', 'markdown', 'misc', 'msg_deleting', 'muting', 'notes', 'reactions', 'remote_cmds', 'reporting', 'rules', 'sed', 'special', 'translator', 'tts', 'ud', 'userinfo', 'users', 'warns', 
# 'welcome', 'zalgo']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 3306
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
