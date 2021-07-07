from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/programmes_investissement')
def programmes_investissement():
    return render_template('programmes_investissement.html')


if __name__ == '__main__':
    app.run(debug="true")