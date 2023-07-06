from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Borda Academy 2023'

