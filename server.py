from flask import Flask, render_template
app = Flask (__name__)

@app.route('/play')
def level():
    return render_template("index.html", x=4, y=4, color= "purple", color2= "grey")


@app.route('/play/<int:x>')
def level1(x):
    x = int(x/2) #converting userinput to half and converting float into int 
    return render_template("index.html", x=x, y=x, color= "red", color2= "blue")

@app.route('/play/<int:x>/<int:y>')
def level2(x, y):
    x = int(x/2) 
    y = int(y/2)
    return render_template("index.html", x=x, y=y,color= "Black", color2= "yellow")

@app.route('/play/<int:x>/<int:y>/<string:color>/<string:color2>')
def level3(x,y,color, color2):
    x = int(x/2)
    y = int(y/2)
    return render_template("index.html", x=x, y=y,color=color, color2= color2)


if __name__ == "__main__":
    app.run(debug=True)