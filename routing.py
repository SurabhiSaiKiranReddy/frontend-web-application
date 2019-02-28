from flask import Flask, render_template,url_for
app = Flask(__name__)
@app.route("/")
@app.route("/login")
def login():
    return render_template('index.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/quote_history")
def quote_history():
    return render_template('quote_history.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/Fuel_quote")
def Fuel_quote():
    return render_template('Fuel quote.html')

if __name__=='__main__':
    app.run(debug=True)