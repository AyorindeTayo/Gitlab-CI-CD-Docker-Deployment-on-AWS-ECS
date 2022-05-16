import flask

app =flask.Flask(__name__)

@app.route('/',methods=['Get'])
def home():
    return "<h1>Demo Flask App</h1>"

if __name__== '__main__':
    app.run(host="0.0.0.0")