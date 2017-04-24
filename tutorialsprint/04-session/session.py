from flask import Flask, request, session, redirect, url_for, escape
app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('login'))
    return '''
        <form action = "" method = "post">
            <p><input type=text name = username></p>
            <p><input type=submit value = Login></p>
        </form>
    '''
@app.route('/logout')
def logout():
    #remove the username from session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)

    # trouble with tutorial