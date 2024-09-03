from flask import Flask

app = Flask(__name__)

@app.route("/")
def myself_vikas():
    return "<p>I am Vikas Jalane <p>"

if __name__ == '__main__':
    app.run (host="0.0.0.0", port=2000)
