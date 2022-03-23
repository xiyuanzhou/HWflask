from flask import Flask, render_template

def loop_list(mylist):
    string = "<ul>\n"
    for s in mylist:
        string += "<li>" + s + "</li>\n"
    string += "</ul>"
    return string

myObject = Flask(__name__)

name = "Lisa"
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myObject.route('/')
def home():
    #name = "Lisa"
    #city_names = ['Paris', 'London', 'Rome', 'Tahiti']

    return """
    <html>
    <head>
        <h1>Welcome""" + name + """!</h1>
    </head>
    <p><a href="www.google.com">not google</a></p>
    <body>
        """+loop_list(city_names)+"""
    </body>
    </html>
    """



if __name__ == '__main__':
    myObject.run(debug = True)
