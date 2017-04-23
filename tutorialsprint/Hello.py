#setting application
from flask import Flask
app = Flask(__name__)


#routing application
@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/home')
def hi():
    return 'hi i\'m home '


#tutorialsprint variable name
@app.route('/hello/<name>')
def hello_name(name):
    return 'hello {}'.format(name)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'blog number {}'.format(postID)

@app.route('/revision/<float:number>')
def revision(number):
    return 'revision number {}'.format(number)




#running application
if __name__ == '__main__':
    app.run(debug=True)

