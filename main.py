from flask import Flask
app = Flask('app', static_folder="images/")

@app.route('/')
def hello_world():
  return f'<img src="{image_url}"> <h2>{name}</h2>'

app.run(host='0.0.0.0', port=8080)
