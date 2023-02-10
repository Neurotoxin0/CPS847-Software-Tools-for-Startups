import logging, os, random
from slack_bolt import App
from auth import auth


# --------------------------------------------------
# Change working dir
Path = (os.path.split(os.path.realpath(__file__))[0] + "/").replace("\\\\", "/").replace("\\", "/")
os.chdir(Path)

# Set token as env vars
auth()

# Initialize a Bolt for Python app
app = App()
# --------------------------------------------------


# --------------------------------------------------
"""
@param user: user id
@param channel: channel id
@param client: slack client
@param text: text of the message
@param msg: the message in slack format
"""

def send_msg(client, msg):
    response = client.chat_postMessage(**msg)
    logger.info(f"Send the message at {response['ts']}")


def empty_msg(user, channel, client):
    response_list = \
    [
        f"<@{user}> Yes?",
        f"<@{user}> How may I help?",
        f"<@{user}> Wabby Wabbo?"
    ]
    response = response_list[random.randint(0, len(response_list)-1)]

    msg = \
    {
        "ts": "",
        "channel": channel,
        "username": user,
        "blocks": \
        [
            {
                "type": "section",
                "text": \
                {
                    "type": "mrkdwn",
                    "text": response
                }
            }
        ],
    }
    send_msg(client, msg)


def unknown_cmd(user, channel, client):
    response_list = \
    [
        f"<@{user}> I do not know how to process your command, maybe try adding `echo`?",
        f"<@{user}> Wabby Wabbo?"
    ]
    response = response_list[random.randint(0, len(response_list)-1)]

    msg = \
    {
        "ts": "",
        "channel": channel,
        "username": user,
        "blocks": \
        [
            {
                "type": "section",
                "text": \
                {
                    "type": "mrkdwn",
                    "text": response
                }
            }
        ],
    }
    send_msg(client, msg)


def echo_cmd(user, channel, client, text):
    #filter = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    #filtered = filter.sub(' ', text)
    filtered = text.strip("")

    response_list = \
    [
        f"<@{user}> I agree! {filtered}!",
        f"<@{user}> {filtered}?"
    ]
    response = response_list[random.randint(0, len(response_list)-1)]

    msg = \
    {
        "ts": "",
        "channel": channel,
        "username": user,
        "blocks": \
        [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": response
                }
            }
        ],
    }
    send_msg(client, msg)
# --------------------------------------------------


# --------------------------------------------------
# when bot name is mentioned
@app.event("app_mention")
def message(event, client):
    """
    :param event: event payload
    :param client: slack client
    :return: none
    """
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text").replace('<@U04LBCW6FU7>', '')    # remove '@bot-itself'

    if text.strip() == '':
        return empty_msg(user_id, channel_id, client)
    if text and "echo" in text: 
        return echo_cmd(user_id, channel_id, client, text.strip("echo "))
    return unknown_cmd(user_id, channel_id, client)



if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.start(847)  # port
# --------------------------------------------------