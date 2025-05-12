import os
from dotenv import load_dotenv

load_dotenv()

# MTM3MTM3NTM0NTYwMDU2MTI2NA.GqIDZw.vc69RLQ2LDVkJGOJuQHohZXbWo-qoKOTPVnPAo
def get_discord_token():
    return os.getenv("DISCORD_TOKEN")
