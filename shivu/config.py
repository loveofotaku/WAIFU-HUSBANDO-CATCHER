class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5143645152"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1002030481292
    TOKEN = "7292911935:AAGe2y2WGi40O68n_wVMh1I6bluosstlotE"
    mongo_url = "mongodb+srv://Bankaieditz8:Ald4O4nBkhL2q5MQ@gurubhai.pkocnim.mongodb.net/?retryWrites=true&w=majority&appName=Gurubhai"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "toman_gang_official"
    UPDATE_CHAT = "toman_gang_official"
    BOT_USERNAME = "Toman_waifu_bot"
    CHARA_CHANNEL_ID = "-1002033375935"
    api_id = 10422108
    api_hash = "3f5669f843ceaebe022b858474dc7b26"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
