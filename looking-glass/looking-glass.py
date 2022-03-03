import json
import requests

from os import environ as env

SLACK_API_URL = "https://slack.com/api/"
SLACK_MESSAGE_URL = SLACK_API_URL + "chat.postMessage"
SLACK_FEEDBACK_CHANNEL = "feedbacks"


def lambda_handler(event, context):
    try:
        slack_token = env.get("SLACK_TOKEN")

        feedback_message = "this is fake feedback pls disregard!"

        message_response = requests.post(
            SLACK_MESSAGE_URL,
            {
                "token": slack_token,
                "channel": SLACK_FEEDBACK_CHANNEL,
                "text": feedback_message,
            },
        )

        assert message_response.status_code == 200

        print("done")

    except Exception as LOOKING_GLASS_EXCEPTION:
        print(LOOKING_GLASS_EXCEPTION)

    return ""
