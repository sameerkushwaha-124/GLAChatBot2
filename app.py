from flask import Flask , render_template , request
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/home')
# def home():
#     return render_template("home.html")

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/submit' , methods=["post"])
def submit():
    username = request.form["abc"]
    password = request.form["password"]
    file = request.form["form"]
    print(username)
    print(password)
    x = 10
    return render_template("after.html", data=x )


if __name__ == "__main__":
    app.run(port=5100)