from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mauriziocontatto@gmail.com'
app.config['MAIL_PASSWORD'] = 'Sn1p3r1992'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    msg = Message('mail con <b>Flask</b>', sender='mauriziocontatto@gmail.com', recipients=['maurizio.bussi@hotmail.it'])
    msg.body = "ahhahaha ti faccio un while di mail.send(msg)... funny arrivooooooo :P"
    mail.send(msg)
    return 'Sent'

if __name__=='__main__':
    app.run(debug=True)