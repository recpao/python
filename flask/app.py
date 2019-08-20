# Da: https://code.tutsplus.com/it/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()