from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = "yffJy2EGKvFKla5Bgk+H4jez+6qeexJe54oE4uyn3GGk4rW6DoeUT6hr+EMeY8rvTRhxUG9HTQQ+Z9l6H+Y+atNsIvOQsp026q2TdJnPVAybdrhJHd2ngNc5Lg6OUuQfOS7IALNEecrnO4X9p02yXwdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "Ud53dc27490532ac9eb93e3aba3bf6adb"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=["GETS","POST"])

def hatano():
    return "hatano world!"
	
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
#    app.run()
	app.run(host='0.0.0.0', port=3000, threaded=True)
