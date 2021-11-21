from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = "yffJy2EGKvFKla5Bgk+H4jez+6qeexJe54oE4uyn3GGk4rW6DoeUT6hr+EMeY8rvTRhxUG9HTQQ+Z9l6H+Y+atNsIvOQsp026q2TdJnPVAybdrhJHd2ngNc5Lg6OUuQfOS7IALNEecrnO4X9p02yXwdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "ee66fe29987b4811e91c4a88e4d5b0fd"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)



@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']

   
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)


    try:
        handler.handle(body, signature)
        
if __name__ == "__main__":
    app.run(debug=True)


    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)) 
if __name__ == "__main__":
    app.run(debug=True)

