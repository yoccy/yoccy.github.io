from flask import Flask, render_template
from data import get_work , get_all_works

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
    all_works = get_all_works()
    return render_template('/portfolio.html', all_works=all_works)

@app.route('/work/<work_name>.html')
def work(work_name):
    work = get_work(work_name)
    return render_template('/portfolio/work.html', work=work)

@app.route('/interested.html')
def interested():
    return render_template('/interested.html')

if __name__ == "__main__":
    app.run(debug=True)