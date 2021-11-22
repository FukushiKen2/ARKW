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

import csv
import datetime
from datetime import date
import pytz


app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = "yffJy2EGKvFKla5Bgk+H4jez+6qeexJe54oE4uyn3GGk4rW6DoeUT6hr+EMeY8rvTRhxUG9HTQQ+Z9l6H+Y+atNsIvOQsp026q2TdJnPVAybdrhJHd2ngNc5Lg6OUuQfOS7IALNEecrnO4X9p02yXwdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET = "ee66fe29987b4811e91c4a88e4d5b0fd"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    f = open("konishi.csv",'r')
    tanzawa = f.read()
    f.close()
    return tanzawa



@app.route("/callback", methods=['POST'])
	
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
    profile = line_bot_api.get_profile(event.source.user_id)
    
    f = open("konishi.csv",'a')
    add_tan = profile.display_name
    add_sentence = event.message.text 
    d_today = datetime.datetime.today(pytz.timezone('Asia/Tokyo'))
    add_hat = d_today.strftime('%Y-%m-%d %H:%M:%S')

    f.write(add_tan + " " + add_sentence + " " + add_hat)
    f.write("\n")
    f.close()

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

    

if __name__ == "__main__":
#    app.run()
	app.run(host='0.0.0.0', port=3000, threaded=True)
