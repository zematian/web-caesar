from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""

<!DOCTYPE html>
<html>

    <head>

        <style>

            form {{

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }}

            textarea {{

                margin: 10px 0;

                width: 540px;

                height: 120px;

            }}

        </style>

    </head>

    <body>

        <form action="/" method="POST">Rotateby value
            <input id="text" type="text" name="rot" value=0 />
            <textarea name="text">{0}</textarea> 
            <input type="submit" />
        </form>
    </body>
   

</html>"""
@app.route("/")
def index():
    return form.format("")
@app.route("/",methods=['POST'])
def encrypt():
    int_value = int(request.form["rot"])
    original_text=str(request.form["text"])
    rotated_text= str(rotate_string(original_text,int_value))
    return form.format(rotated_text)
app.run()
