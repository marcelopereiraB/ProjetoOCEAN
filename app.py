from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")
posts = [
    {"" 
           "title": "o meu post",
            "body": "aqui é texto do post",
            "autor": "celonerda",
            "created": datetime(2022,7,25)
    },
    {
            "title": "o meu post",
            "body": "aqui é texto do post",
            "autor": "sest",
            "created": datetime(2022,7,26)
    },
    {"title": "o meu post",
            "body": "aqui é texto do post",
            "autor": "marcelo silva",
            "created": datetime(2022,7,27)
    },
    {
            "title": "o meu post",
            "body": "aqui é texto do post",
            "autor": "fernando silva",
             "created": datetime(2022,7,28)
    }
        
]
@app.route("/")
def index():
    return render_template("index.html", posts=posts)
