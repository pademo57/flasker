from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(debug=True)

