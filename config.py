# mrz bot
# ultra forward bot 

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", 23310880))
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "KRForwardBot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://SK:SK@mrtamilkid.cybnk0e.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Forwd")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", "6955294614").split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
