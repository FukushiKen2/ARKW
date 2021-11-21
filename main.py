from flask import Flask, request, abort



app = Flask(__name__)

@app.route("/")
def index():
       print("hatano")
    




if __name__ == "__main__":
    app.run(debug=True)                        
