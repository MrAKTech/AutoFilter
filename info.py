import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '22225617'))
API_HASH = environ.get('API_HASH', 'ef16f7597376f1689663304c954e4493')
BOT_TOKEN = environ.get('BOT_TOKEN', "7508746268:AAFNxdfx3wxAOkmhkvwziPycbvvU29GkWio")
PM_SEARCH = bool(environ.get('PM_SEARCH', True))

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://envs.sh/Cio.jpg https://envs.sh/Cis.jpg https://envs.sh/Ci9.jpg https://envs.sh/Civ.jpg https://envs.sh/CiN.jpg https://envs.sh/CiH.jpg https://envs.sh/CiJ.jpg https://envs.sh/Cig.jpg https://envs.sh/Cif.jpg https://envs.sh/Cia.jpg https://envs.sh/CiO.jpg https://envs.sh/Cim.jpg https://envs.sh/CiM.jpg https://envs.sh/Cio.jpg')).split() #SAMPLE PIC
SEARCHGIF = (environ.get('SEARCHGIF', 'https://envs.sh/CiL.gif https://envs.sh/Ci5.gif https://envs.sh/CiG.gif https://envs.sh/Ciz.gif https://envs.sh/Ci3.gif https://envs.sh/CiR.gif https://envs.sh/Ci1.gif https://envs.sh/Ci4.gif https://envs.sh/CiU.gif https://envs.sh/Cil.gif https://envs.sh/Ci8.gif')).split()
NOR_IMG = environ.get("NOR_IMG", "https://envs.sh/_uv.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://envs.sh/Cbv.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/54339913c153df35e5a54.jpg'))
CODE = (environ.get('CODE', 'https://graph.org/file/f96562518138b9132abf8.jpg'))

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'modijiurl.in'))
STREAM_API = (environ.get('STREAM_API', 'da3325d5fbd605b4bfe461a28ff6fc4b3eec7a6d'))
STREAMHTO = (environ.get('STREAMHTO', 'https://telegram.me/HowToDownload_Tutorial_MrAK/3'))

#Shortner Variables
VERIFY = bool(environ.get('VERIFY', False)) # Verification On ( True ) / Off ( False )
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://telegram.me/HowToDownload_Tutorial_MrAK/3') # How to open tutorial link for verification
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'modijiurl.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'da3325d5fbd605b4bfe461a28ff6fc4b3eec7a6d')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

USERNAME = environ.get('USERNAME', "https://telegram.me/IamMrAK_bot") # ADMIN USERNAME
MICL = environ.get('MICL', 'https://telegram.me/MrAK_LinkZzz')
BMICL = environ.get('BMICL', 'https://telegram.me/+P-oPdYbUDWIwNjI9')
BMCL = environ.get('BMCL', 'https://telegram.me/+skgCIvzceP44NTM1')
MCL = environ.get('MCL', 'https://telegram.me/+5qxYQpqg8KY2ZmY1')
MGL = environ.get('MGL', 'https://telegram.me/New_Movies_Request_Group_MrAK')
BMGL = environ.get('BMGL', 'https://telegram.me/+QAdjuRtIXf0xMDk1')
ACL = environ.get('ACL', 'https://telegram.me/addlist/YtriDZhDyVViZjY9')
BACL = environ.get('BACL', 'https://telegram.me/MrAK_AnimeZz')
AGL = environ.get('AGL', 'https://telegram.me/MrAK_AnimeZz_Tamil')
WCL = environ.get('WCL', 'https://whatsapp.com/channel/0029VaZbVwQGU3BJt3IfFr2Q')
TSCL = environ.get('TSCL', 'https://telegram.me/+4_Uq4L95R00yODll')
BMB = environ.get('BMB', 'https://telegram.me/MrAKLinkZbot')
MRAKBOTS = environ.get('MRAKBOTS', 'https://telegram.me/MrAK_BOTS')
MYBOT = environ.get('MYBOT', 'https://telegram.me/MrAK_Movie_bot')

#REFERAL
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '15')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002141251057'))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6072149828 5773687944').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002467628368').split()] #Channel id for auto indexing ( make sure bot is admin )
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1002467628368') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001955218723') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002345928160') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True)) # True if you want no results messages in Log Channel

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://akmonsterprogrammer:S.Aruna1155182089@ben10.akgdh.mongodb.net/?retryWrites=true&w=majority&appName=Ben10")
DATABASE_NAME = environ.get('DATABASE_NAME', "Ben10")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
TUTORIAL = environ.get('TUTORIAL', 'https://telegram.me/HowToDownload_Tutorial_MrAK/3') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Hello Nanbha and Nanbis ❤️')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002360721674')) #Log channel id ( make sure bot is admin )
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://telegram.me/New_Movies_Request_Group_MrAK') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["Tamil", "Tam", "Telugu", "Tel", "Kannada", "kan", "Malayalam", "Mal", "Hindi", "Hin", "English", "Eng", "Korean", "Kor", "Japanese", "Jap", "Chinese", "Chi", "Dual", "Multi"]
YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "4K", "HQ", "HD","HQPreDVD","PreDVD"]

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME', 'mrak-2a7526a285ee')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME', 'mrak-2a7526a285ee'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
