from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def hello():
        return "Hello, World!"

@app.route("/index")
def index():
    name = request.args.get("name")
    return render_template("index.html",name=name)




if __name__ == "__main__":
    app.run(debug=True)                        
