import os

from dotenv import load_dotenv

load_dotenv(dotenv_path="./settings-tecobrary-slack/.env")

if os.getenv("ENVIRONMENT") == "test":
    AUTH_TOKEN = os.getenv("TEST_SLACK_AUTH_TOKEN")
    REQUESTED_CHANNEL = os.getenv("TEST_REQUESTED_CHANNEL")
    ENROLLED_CHANNEL = os.getenv("TEST_ENROLLED_CHANNEL")
elif os.getenv("ENVIRONMENT") == "deploy":
    AUTH_TOKEN = os.getenv("DEPLOY_SLACK_AUTH_TOKEN")
    REQUESTED_CHANNEL = os.getenv("DEPLOY_REQUESTED_CHANNEL")
    ENROLLED_CHANNEL = os.getenv("DEPLOY_ENROLLED_CHANNEL")
