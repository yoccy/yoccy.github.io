from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "yoccy"
    return render_template('/index.html', name=name)

@app.route('/skill.html')
def skill():
    return render_template('/skill.html')

@app.route('/portfolio.html')
def portfolio():
    return render_template('/portfolio.html')

@app.route('/interested.html')
def interested():
    return render_template('/interested.html')

if __name__ == "__main__":
    app.run(debug=True)