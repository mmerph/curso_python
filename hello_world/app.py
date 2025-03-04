from flask import Flask

app = Flask(__name__)

@app.route("/") #home or root of website
def index():
    return '<html><head><title>HELLO WORLD</title></head></html><h1>Hello world</h1><p>Ir a<a href = "/about">about</a></p></body></html>'
@app.route("/about") #info about this site
def about():
    '<html><head><title>About this page </title></head><body> Everything about this website. Back to <a href="/"> Hello World </a></body></html>'
 
if __name__ == '__main__':
    app.run(debug=True)