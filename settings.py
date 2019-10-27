import os

from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv("SLACK_AUTH_TOKEN")
REQUESTED_CHANNEL = os.getenv("REQUESTED_CHANNEL")
ENROLLED_CHANNEL = os.getenv("ENROLLED_CHANNEL")
