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

@app.route("/")
def index():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)                        
