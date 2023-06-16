from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def hello_playground():
    return 'Hello Playground!'

@app.route('/play')                           
def play():
    return render_template("play.html")

@app.route('/play/<int:num>')                           
def play_num(num):
    return render_template("play_num.html", num=num)

@app.route('/play/<int:num>/<string:color>')                           
def play_num_color(num, color):
    return render_template("play_num_color.html", num=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)