from flask import Flask,render_template
app = Flask(__name__)


@app.route('/skill')
def show_skills():
    d = {
        "Python":82,
        "PHP":69,
        "Html/Css":75,
        "javascript":79,
        "versioning":89,
        "algorithm":69,
        "mongoDB":61,
        "mySQL":64
    }
    return render_template('skill.html', skill = d)

if __name__=='__main__':
    app.run(debug=True)