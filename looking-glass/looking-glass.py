import json
import requests

from os import environ as env

PRODUCTION = "prod"

SLACK_API_URL = "https://slack.com/api/"
SLACK_MESSAGE_URL = SLACK_API_URL + "chat.postMessage"

SLACK_FEEDBACK_CHANNEL = "feedbacks"
SLACK_FEEDBACK_CHANNEL_DEV = "dev-feedbacks"


def get_feedback_channel(stage):
    if stage == PRODUCTION:
        return SLACK_FEEDBACK_CHANNEL
    else:
        return SLACK_FEEDBACK_CHANNEL_DEV


def lambda_handler(event, context):
    try:
        slack_token = env.get("SLACK_TOKEN")
        stage = event.get("stage")
        data = event.get("feedback")

        message = data["message"]
        user = data["user"]

        feedback_message = f"""App Feedback from {user}:\n{message}"""

        message_response = requests.post(
            SLACK_MESSAGE_URL,
            {
                "token": slack_token,
                "channel": get_feedback_channel(stage),
                "text": feedback_message,
            },
        )

        assert message_response.status_code == 200

    except Exception as LOOKING_GLASS_EXCEPTION:
        print(LOOKING_GLASS_EXCEPTION)

    return ""
