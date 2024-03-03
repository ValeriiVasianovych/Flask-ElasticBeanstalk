from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
       <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Document</title>
          <style>
             body {
                background-color: black;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
             }
             p {
                color: gold;
                font-size: 48px;
                text-align: center;
                margin-top: 200px;
             }
          </style>
       </head>
       <body>
          <p>Hello world!</p>
       </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)
