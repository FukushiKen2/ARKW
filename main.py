from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def hello():
        return "Hello, World!"

@app.route("/index")
def index():
	return render_template("index.html")

@app/route("/index",method=["GETS"])
def receive_get():
	name = request.args["my_name"]
	if len(name) == 0:
		return "名前が未入力"
	else:
		return "名前は" + str(name) + "です"


if __name__ == "__main__":
    app.run(debug=True)                        
