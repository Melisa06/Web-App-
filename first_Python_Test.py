from flask import Flask, render_template
app = Flask(__name__)

@app.route('/datos')
def datos():
    return render_template("datos.html")

if __name__ == "__main__":
    app.run(debug=True)
