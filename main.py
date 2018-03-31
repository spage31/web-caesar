from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

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
        <form action="/" method="post">
            
            <label for="rotator">Rotate by</label>
            <input id="rotator" type="text" name="rot" value="0" />
            <div>
            
            <textarea id="rotator" name="text" >{0}</textarea>
            <input id="rotator" type="submit">
            
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotate_amount = request.form['rot']
    rotate_text = request.form['text']
    new_phrase = rotate_string(rotate_text, int(rotate_amount))
    
    return form.format(new_phrase)

app.run()