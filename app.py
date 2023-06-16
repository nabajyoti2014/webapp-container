from flask import Flask, render_template
import random

app = Flask(__name__)

# list of car images
images = ["https://demosta007.blob.core.windows.net/cars/Tesla-Model-3.jpg","https://demosta007.blob.core.windows.net/cars/Tesla-Model-S.jpg"]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")