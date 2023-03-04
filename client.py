from flask import Flask, render_template, request
from generate_html import generate_html
from time import sleep
from pronote import get_homeworks


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    
    username = request.args.get('username')
    password = request.args.get('password')
    url = request.args.get('url')
    homeworks = get_homeworks(
        url=url,
        username=username,
        password=password
    )
    generate_html(homeworks)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()