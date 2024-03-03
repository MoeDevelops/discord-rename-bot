import os
from dotenv import load_dotenv
from bot import start

def main():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    start(TOKEN)


if __name__ == '__main__':
    main()
