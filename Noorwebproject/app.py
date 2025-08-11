from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
<<<<<<< HEAD
def home():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(debug=True)


## In python, they updated the app to application then app. is not accepted anymore ;)
=======
def hello_world():
        return 'Hello, Noor web app!'

if __name__ == '__main__':
        application.run(debug=True)
>>>>>>> e5fdc87d8a8c2e88a171ea0ac245f6adfa7e1f80
